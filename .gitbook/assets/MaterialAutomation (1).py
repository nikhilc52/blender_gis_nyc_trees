import bpy
import time
#timer
start_time = time.time()

#list of map_xx.osm collection numbers to cycle through
collectionList = [20,21,22,23,24,25,26,27]

#delete the objects provided in object list for each collection
def deleteObjects(objectList):
    #cycle through all collections and all objects in that collection
    for o in objectList:
        for c in collectionList:
            #using a try catch in the case of certain objects not being present in certain collections
            #the program should still continue if it cant find the object to delete (if it doesn't exist)
            try:
                bpy.data.objects.remove(bpy.data.objects["map_"+str(c)+".osm_"+o])
            except:
                continue
                
#convert certain objects to "wires"
def convertObjectsWire():
    #deselect all objects so that the object.convert call later is not thrown off
    for o in bpy.context.selected_objects:
        o.select_set(False)

    #cycle through all collections and all objects in that collection
    for c in collectionList:
        for o in bpy.data.collections["map_"+str(c)+".osm"].all_objects:
            #I'm converting all non-coastline (we'll do these later) and non-building objects
            if(o.name != "map_"+str(c)+".osm_coastlines" and o.name != "map_"+str(c)+".osm_buildings"):
                #select non-coast and non-build objects
                o.select_set(True)
                #adding this line for object.convert, which needs to have an active object - this line makes it the last
                bpy.context.view_layer.objects.active = o
    
    #if there is at least 1 object selected
    if(len(bpy.context.selected_objects) != 0):
        #convert to mesh
        bpy.ops.object.convert(target='MESH')
        #add wireframe modifier
        bpy.ops.object.modifier_add(type='WIREFRAME')
        #set the wireframe modifier thickness
        bpy.context.object.modifiers["Wireframe"].thickness = 0.5
        #apply the modifier to all the objects we have selected
        bpy.ops.object.modifier_copy_to_selected(modifier="Wireframe")
    
#convert coastline objects to "wires" in a new method since they start as meshes
def convertCoastlines():
    #deselect all objects so that the object.convert call later is not thrown off
    for o in bpy.context.selected_objects:
        o.select_set(False)
    
    #cycle through collections, choosing all the coastline objects
    for c in collectionList:
        #using a try catch since buildings might not exist for a collection
        try:
            bpy.data.objects["map_"+str(c)+".osm_coastlines"].select_set(True)
            #adding this line for object.convert, which needs to have an active object - this line makes it the last
            bpy.context.view_layer.objects.active = bpy.data.objects["map_"+str(c)+".osm_coastlines"]
        except:
            continue
    
    #if there is at least 1 object selected
    if(len(bpy.context.selected_objects) != 0):
        #convert to curve
        bpy.ops.object.convert(target='CURVE')
        #for all the selected objects, change the bevel depth
        #need to do this in a loop since it is an individal object property
        for o in bpy.context.selected_objects:
            o.data.bevel_depth = 0.5
        #scale to make it 2D (0 along the Z)
        bpy.ops.transform.resize(value=(1,1,0))
        #convert to mesh
        bpy.ops.object.convert(target='MESH')
        #add wireframe modifier
        bpy.ops.object.modifier_add(type='WIREFRAME')
        #apply the modifer to all the objects we have selected
        bpy.ops.object.modifier_copy_to_selected(modifier="Wireframe")

#sets materials for the buildings and the roads
def setMaterials():
    #make a new building material
    mat = bpy.data.materials.new(name="Buildings")
    #cycle through collections
    for c in collectionList:
        #using a try catch since buildings might not exist for a collection
        try:
            #choose the building object in each collection
            o = bpy.data.objects["map_"+str(c)+".osm_buildings"]
            
            #see if material slost exists
            if o.data.materials:
                #if material slots exists, then prepend the material to make it active
                o.data.materials[0] = mat
            else:
                #else, if this is the first material, append it
                o.data.materials.append(mat)
        except:
            continue
            
    #make a new road material
    mat = bpy.data.materials.new(name="Roads")
    #cycle through collections and objects
    for c in collectionList:
        for o in bpy.data.collections["map_"+str(c)+".osm"].all_objects:
            #if the object is not a building, set it to a road material
            if(o.name != "map_"+str(c)+".osm_buildings"):
                #if material slots exists, then prepend the material to make it active
                if o.data.materials:
                    o.data.materials[0] = mat
                else:
                    #else, if this is the first material, append it
                    o.data.materials.append(mat)
            
    
######################

deleteObjects(["areas_cycleway","areas_footway","areas_pedestrian","forest","paths_bridleway","areas_service",
    "paths_cycleway","paths_steps","vegetation","water"])
print('--- Deleted Objects ---')

convertObjectsWire()
print('--- Converted Objects to Wires ---')

convertCoastlines()
print('--- Converted Coastlines ---')

setMaterials()
print('--- Set Materials ---')

print('Finished in %s seconds' % (time.time() - start_time))