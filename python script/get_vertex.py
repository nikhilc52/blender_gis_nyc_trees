import bpy
import bmesh

# Get the active mesh
obj = bpy.context.active_object
me = obj.data

# Get a BMesh representation
bm = bmesh.from_edit_mesh(me)

# Ensure the selection history is not empty
if bm.select_history:
    # Get the active element (the last selected element)
    elem = bm.select_history.active
    
    if isinstance(elem, bmesh.types.BMVert):
        # Print coordinates of the selected vertex
        co = elem.co
        print(f"{co.x}, {co.y}, {co.z}")
    else:
        print("Please select a vertex.")
else:
    print("No elements selected.")

# Free the BMesh and update the mesh
bmesh.update_edit_mesh(me)
