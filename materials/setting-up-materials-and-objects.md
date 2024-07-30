# Setting Up OSM Materials and the Environment

## Introduction

***

Assigning pretty material colors and lighting can really elevate a render from good to great. Here, instead of following the instructions verbatim, consider experimenting with a new theme or feel. Still, I'll provide a baseline of actions to create a decent looking render, with some steps and features that will be useful to know for all renders.

The Material: Material Utilities add-on is required for this section, and can be enabled via Edit -> Preferences -> Add-Ons -> Material Utilities (Search)

Also make sure that we're in **Cycles** (with a GPU device if you have one). Cycles renders include ray tracing features and are generally more visually appealing. You can switch to Cycles in the Render Properties tab:

<figure><img src="../.gitbook/assets/image (13).png" alt="" width="375"><figcaption></figcaption></figure>

If the GPU device looks greyed out, go to Edit -> Preferences -> System and make sure that the Cycles Render Devices setting at the top of that page is set appropriately.

## Manipulating Objects for Shading

***

There are two ways we can manipulate objects (which involves removing unneeded ones, applying materials, and converting object meshes). One is by automating the manipulation using a Python script, and the other is committing the changes manually. While the Python script is **far easier**, to understand what each line is doing, I recommend you to look over (**but not necessarily actually complete**) the manual method, which can help understanding.

### Manually Editing:

#### Objects:

In my render, I chose to omit certain objects that I didn't like the look of. These objects are listed below:

<figure><img src="../.gitbook/assets/image (31) (1).png" alt="" width="375"><figcaption></figcaption></figure>

I've deleted these "type" (areas\_footway, areas\_pedestrian, etc.) of objects for every map\_xx.osm collection.&#x20;

With these objects out of the way, we need to do some conversions to make the rest of the objects appear visually appealing. First, we'll start by making all of the roads "hollow" with the wireframe modifier. This is because the current state of these objects makes them a bit too distracting, so lessening their visibility can help counter that. Again, that's just what I think - feel free to change course.

To apply the wireframe modifier we'll need to convert all the road objects (and paths\_footway) into meshes. We can do this by selecting them in the outliner, then pressing Object -> Convert -> Mesh at the top of the 3D viewport:

<figure><img src="../.gitbook/assets/image (32) (1).png" alt="" width="375"><figcaption></figcaption></figure>

Then, with the same objects selected, we can add a wireframe modifier with a thickness of 0.5m, and select "Copy to Selected" from the drop down menu.

<figure><img src="../.gitbook/assets/image (33) (1).png" alt="" width="563"><figcaption></figcaption></figure>

If we look in the viewport, all of the roads will now be "hollow" and only made up of thin lines:

<figure><img src="../.gitbook/assets/image (34).png" alt="" width="563"><figcaption></figcaption></figure>

**Repeat this process for all of the roads (and paths\_footways)** within the other map\_xx.osm collections, for consistency across the scene.

The last change we'll need to make before we start assigning materials is to the coastlines object. Since the coastlines objects are currently 1D (line) meshes, applying a wireframe modifier won't work. We'll have to convert **all of them** to curves, via the same menu: Object -> Convert -> Curve.

From here, in the Curve Properties menu, add a depth of 0.5 to the curve:

<figure><img src="../.gitbook/assets/image (35).png" alt="" width="563"><figcaption></figcaption></figure>

This makes the curve into a spherical model, which is a bit off what we had for other lines in our scene, which were 2D.&#x20;

<figure><img src="../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

So, **with all the coastline curves selected**, we can scale them to 0 along the Z axis (by pressing S -> Z -> 0) to remove its 3D dimension and have it match the other roads. Accordingly, we'll convert them back to a mesh (Object -> Convert -> Mesh), and then apply the same wireframe modifier (with a thickness of 0.02m this time) to make the objects similar to what we performed earlier with the roads.

Note that the difference in thickness is due to the fact that the conversion we did with the coastlines adds additional edges to the object, which makes the object thicker in its wireframe, and thus can be compensated for by decreasing the wireframe thickness.

**Make sure to apply this effect to all the coastline objects in the scene (under different .osm collections).**

#### Materials:

We'll now assign some start materials to our scene.

The first thing we can do to manage materials is a bit blunt, but works well for the goals of our scene. We're going to remove all the materials in our scene. This makes it much easier to work with materials for all objects, since we won't have to deal with thousands of different materials and material slots that are automatically assigned from the Blosm import.&#x20;

We can easily get rid of these materials and slots by going to the Blender File section of the Outliner:

<figure><img src="../.gitbook/assets/image (29) (1).png" alt="" width="536"><figcaption></figcaption></figure>

From here, we can expand the materials tab, select the first option, scroll to the bottom and hold Shift+Left Click, to select all the materials. From here, we can simply delete the materials. Our scene looks a lot more barren now, but it's ready to be shaded.

<figure><img src="../.gitbook/assets/image (30) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Note that this will also get rid of the materials we're using for the three raster files, but since we want to edit those anyway, it's fine if we delete them for now.

The next step we'll take is to assign a solid color to all the buildings and another solid color to all the roads. This is so that we can easily edit all the meshes at once.

Select **all** the non-building (road) objects in a collection. Make sure that the active material is a road too - you can check this by looking at the top of the Material Properties tab and ensuring that it shows an object we'd like to be assigned a road material:

<figure><img src="../.gitbook/assets/image (37).png" alt="" width="563"><figcaption></figcaption></figure>

From here, just add a new material by pressing "New" and rename it "Roads". Then, click the drop down on the right and select "Copy Material to Selected". We're not going to edit the colors of this material right now, but by assigning it properly here, we've just made it much easier for us to do so later. Repeat this process for the rest of the collections.

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt="" width="171"><figcaption></figcaption></figure>

We'll now repeat this process for the buildings. As you go through the building objects, you might see this in your material properties tab when you go to create a new material:

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

We'll get rid of these empty material slots (which mess with our buildings by making some faces the default material) with the Material Utilities add-on. With our add-on enabled, go into the drop down menu again, and press "Remove All Material Slots". **Make sure to do this for every building object**:

<figure><img src="../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

After that's done, add in the Building material and copy it to all the other buildings (by selecting the other buildings and pressing "Copy Material to Selected") as usual.

### Automated Editing:

While manually editing each of the collections will provide you with a greater understanding of the steps were taking in our rendering preparations, it is **much easier** to generate and run a Python script to do everything for us.

The following script will accomplish the exact same steps that we did above, but much quicker. While I won't go over every line of code in this notebook, the comments within the Python file make it intuitive to understand. **Remember that the steps taken here are just a baseline** - you can edit the .py file to accommodate for any changes you make (like not wanting to delete a certain object or wanting a different material for certain roads).

{% file src="../.gitbook/assets/MaterialAutomation (1).py" %}

Open up a new workspace and switch to the "Text Editor" space. Within that area, open up the MaterialAutomation.py file. Before we can run it, there are a few changes we need to make. First, its a good idea to get rid off all the materials in our scene. This will make our scene lag significantly less when we go to edit materials. Follow the steps [above](setting-up-materials-and-objects.md#materials) to delete materials from the Blender File section of the Outliner.

Second, we'll need to change a few of the lines within the Python file. First, update the `collectionList` on line 7 to match whatever map\_xx.osm collections you have in your scene (i.e. if one collection is called map\_1.osm, the collectionList should contain the number 1). This list represents the collections which will be iterated over.

```python
#list of map_xx.osm collection numbers to cycle through
collectionList = [20,21,22,23,24,25,26,27]
```

Next, make sure that all the objects in the OSM collections are visible in the 3D viewport, otherwise the Python file won't be able to access them.&#x20;

Lastly, be sure to **save a copy of your project** before you run the Python script - some of the changes we make will be difficult to easily reverse if needed.

If you press run, you should see some text outputted in the Console, and after a few seconds you should see the changes in the Blender environment.

```
--- Deleted Objects ---
--- Converted Objects to Wires ---
--- Converted Coastlines ---
--- Set Materials ---
Finished in 1.2009100914001465 seconds
```

<figure><img src="../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

Note that this Python file relies on the names of collections and objects being formatted in the default pattern given by Blosm, if you want to rename your objects, either do it after running the Python script or edit the script itself.

## Setting Up a Global Environment

***

Before we start editing the materials, we should probably set up a rendering environment that allows us to see our changes properly. We'll set up a sun light and baseplane.

In general, I'm modeling our environment based on this [render](https://www.matteoprati.com/progetti/manhattan/) by Matteo Prati.&#x20;

First, we'll make sure we're switched over to Cycles and use a GPU as our rendering device. Next, we'll add in a sun. I'm placing the sun (with a strength of 15) just below Manhattan, pointed towards the buildings.&#x20;

<figure><img src="../.gitbook/assets/image (5) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

I think this gives us enough definition while still brightening the scene - the shadows also don't look too shabby.&#x20;

After that, we'll need to set up a base plane object, to have our objects appear as if they're on a map instead of floating in space (since shadows will now be case on the plane). We'll first add a plane, and scale it up with Shift+A -> Plane -> S -> 100000. Align the plane so that our city is somewhat centered:

<figure><img src="../.gitbook/assets/image (7) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

We're trying to get a render that makes it appear as if this plane blends smoothly with the background. This is an effect we can achieve by mimicking something that happens in real life photography studios:

<figure><img src="../.gitbook/assets/AdobeStock_439304581.jpeg" alt="" width="563"><figcaption><p>Adobe Stock</p></figcaption></figure>

The curve at the bottom of the backdrop makes the transition between the floor to wall seamless, and we can accomplish this effect in a similar manner within Blender.

Simply select the plane, and extrude a backdrop edge upwards (Tab -> 2 -> E -> Z):

<figure><img src="../.gitbook/assets/image (8) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Then select the edge between the vertical and horizontal planes, press Control/Command + B, and drag out your cursor. Before clicking to confirm the placement of the plane, scroll down to add more segments to smooth out the new surface between the two planes. The resulting plane should look something like this:

<figure><img src="../.gitbook/assets/image (9) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

We can right click the plane and shade smooth to even out the surface even more. Now, with the camera pointing in the appropriate direction, the background will merge seamlessly into the base plane. The last thing we need to do is add a material to the plane. I'll be using a solid white color. Make sure that you label the material accordingly:

<figure><img src="../.gitbook/assets/image (10) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

If during your animation the camera is facing a direction that doesn't have the background plane in its view, you can keyframe the rotation of the plane object to move along with the camera view. That's all the set up we'll do for our background, with that set in place, we can move on to seeing how the foreground (buildings/roads) will look.

## Assigning Building and Road Materials

***

The last step in this process is actually assigning materials for our buildings and roads. Remember that when we ran the Python script, we set materials to all the building objects and road objects. This makes it very simple to change materials (since they all reference the same material object): simply select **any** building object, and all the other building objects will reflect any changes to the material.&#x20;

I find that the hex color #E5D8CE is suitable for all the buildings and #000000 is good for the roads:

So, with one building selected, simply change its material:

<figure><img src="../.gitbook/assets/image (41).png" alt="" width="375"><figcaption></figcaption></figure>

Do the same for any of the objects that use the road material:

<figure><img src="../.gitbook/assets/image (13) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

Note that if you want more control over the materials, simply press "Use Nodes" and more options will show up.

## Conclusion

***

After these changes take effect, we should be able to see them in the rendered view of the 3D viewport:

<figure><img src="../.gitbook/assets/image (12) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

You might notice that certain areas of the map have darker shaded materials:

<figure><img src="../.gitbook/assets/image (7) (1).png" alt=""><figcaption></figcaption></figure>

This is due to the overlaps between buildings that occurs when we bring in OSM data (only in Cycles). Normally, the boolean modifier would help us solve these overlaps and color errors, but since the buildings have such a complex geometry, applying the modifier **lags significantly** and is not as effective. A simple workaround I've found is just to add a meter or two to the dimensions of the buildings on one side of the overlap:

<figure><img src="../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

Adding 2 meters to the left buildings made the overlap look like this:

<figure><img src="../.gitbook/assets/image (9) (1).png" alt=""><figcaption></figcaption></figure>

Obviously, the change isn't perfect, but it gets rid of a lot of the dark spots that come from object overlaps (formally known as Z-Fighting). You can repeat this process for any buildings that cause overlaps.
