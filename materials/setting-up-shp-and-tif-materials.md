# Setting Up SHP and TIF Materials

## Introduction

***

With building and road materials in place, we can moving on to coloring the rest of our GIS data. **Make sure that you're saving the project as we go along**, since the steps in this module might cause an unexpected crash.

Be sure that you're labeling your materials appropriately, to stay organized with your work.

## Shapefile Polygon Materials

***

The CHS health survey shapefile provides several custom properties that represent survey data points. If we want to apply a color scale to the polygons based on a custom property, we can easily do that via the shader editor (using nodes). Here's where you can find the custom properties of all the CHS objects:

<figure><img src="../.gitbook/assets/image (16).png" alt="" width="280"><figcaption></figcaption></figure>

First, to get a better understanding of what the data represents, you can look through any data that accompanied the shapefile download - specifically the XML which provides definitions for all the abbreviated variables. I'll be using the "exercs2" attribute for this tutorial.

Back in Blender, open up a Shader Editor viewport, select any one of the objects under the CHS collection, and add a new material:

<figure><img src="../.gitbook/assets/image (1) (1).png" alt="" width="319"><figcaption></figcaption></figure>

From here, we'll need to add just three nodes to get it working:

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

The attribute node converts the "color" of the value of the custom object property "exercs2" into the map range node, which converts the original number, which has a range from 0 to 100 as indicated by the XML description of the data, into a number readable by Blender (0 to 1). From there, the numbers are converted to colors based on a color ramp node, and fed back into the Principled BSDF and finally into the Material Output.&#x20;

The position of the white and black tickers in the color ramp node is very important, since placing either node too high or too low might cause "clipping" of values. For instance, if we placed the white ticker at 0.5 and there was a object with a exercs2 of 10 (.1 after map conversion) and another with an exercs2 of 40 (.4 after map conversion), they would both be mapped to the same color value, even though their values are much different. So, we should have the lower node placed at the lowest value of all the exercs2 values and the higher node placed at the highest of all the exercs2 values (placing the low ticker at 0 and the high ticker at 1 would certainly work, it wouldn't provide good enough precision).

So, to easily find the minimum and maximum values, we can run another Python script, which reads in our shapefile and prints out a list of all exercs2 values in order, which makes it easy to see where we should position our tickers:

{% file src="../.gitbook/assets/SHP_Reader.py" %}

You can run this program inside or outside of Blender, since it doesn't have anything to do with our Blender file's data. If you choose to run the file within Blender, you will need to install **both pandas and geopandas** with pip:

To install pandas through pip, we'll need to access the Python.exe (or python3.11 on Mac) file and use it to run a command through the Command Prompt or Terminal. The code should look something like this:

Windows:

```
"C:\Program Files\Blender Foundation\Blender 4.1\4.1\python\bin\python.exe" -m pip install pandas
```

Mac:

```
/Applications/Blender.app/Contents/Resources/4.1/python/bin/python3.11 -m pip install pandas
```

Once that runs (and you do the same for geopandas), we can run the code (if it doesn't work, just restart Blender, **making sure to save our progress so far** so that we don't have to re-do any steps).

If we now run the code (making sure to change the path file in the `gpd.read_file` call), we'll see that we get this output:

```
  FIRST_BORO                            FIRST_UHF_  exercs2
2       Bronx                  Fordham - Bronx Park     62.9
33      Bronx                           South Bronx     64.3
15        Man           Washington Heights - Inwood     65.3
0       Bronx               Kingsbridge - Riverdale     72.2
17        Man                           East Harlem     72.9
3       Bronx                  Pelham - Throgs Neck     75.9
16        Man  Central Harlem - Morningside Heights     78.5
29        Man         Union Square, Lower Manhattan     79.0
1       Bronx                       Northeast Bronx     79.2
27        Man            Upper East Side - Gramercy     85.9
18        Man                       Upper West Side     87.5
28        Man                     Chelsea - Village     88.3
```

We can now easily see that we want our lower ticker to be at .629 and the upper to be at .883. This ensures that we're not cutting anything off but still providing easily differentiable colors.

With our nodes in place, we might not immediately see a change in color, this might be because of overlaps in the viewport - we can fix them easily by either making the CHS collection the only object visible, or selecting all the collection objects (by right clicking the collection and pressing "select objects") and moving them up along the Z (G -> Z).&#x20;

To apply the material (and color scale) to all objects in this collection, simply navigate to the Material Properties tab, and with all of the objects in the CHS collection selected, press copy to selected. You should now see something like this in the viewport:

<figure><img src="../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

If you don't see this, make sure that your nodes match mine **exactly** (Name: exercs2, Type: Object, From Min: 0.000, From Max: 100.000):

<figure><img src="../.gitbook/assets/image (4) (1).png" alt="" width="259"><figcaption></figcaption></figure>

Note that the legend shown in the rendered video was created manually in Google Drawings, using gradients within that software, the numbers from our Python script output here, and the colors on the Color Ramp to match up the data.

## Shapefile Point Objects

***

As of right now, the individual points of the "dead\_trees" and "alive\_trees" objects won't be visible in our render, since they are just vertices. However, we can easily add 3D objects at the location of each vertex to make the data renderable. To do this, we'll need to append an object to put at each tree location.&#x20;

In the repo, you can download the [tree-blank.blend](../blender\_trees/tree\_blank.blend) and [tree\_leaves.blend](../blender\_trees/tree\_leaves.blend) to use as objects that represent dead and alive trees, respectively. Once they're downloaded, go to File -> Append and select the one of the .blend files. Then, go to Object -> Tree and press append. Do this for each file.

Now that we have the objects we want to be placed at each vertex, we can edit the geometry nodes of  the alive and dead tree shapefiles in the Geometry Node Editor. We'll start with the dead\_trees object, since it's smaller.

With the dead\_trees object selected, go to a Geometry Node Editor workspace, and add a new set of geometry nodes:

<figure><img src="../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

We'll now add Object Info, Transform Geometry and Instance on Points nodes to achieve our desired output:

<figure><img src="../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

All this set up is doing is taking the Geometry from an object in our scene (Tree), transforming it (though in this case I'm leaving it default), instancing that geometry at every point (given by the Group Input), and outputting that information.

While the Transform Geometry node isn't being used in this scenario, it's useful to have incase you'd like to change the location of each tree or scale the trees down or up, so I'll leave it in.

You'll now see trees at every location that was previously just a point:

<figure><img src="../.gitbook/assets/image (10) (1).png" alt=""><figcaption></figcaption></figure>

Right now, the trees don't have a color, but in the render their material is a red emission surface. You can change the material of the trees by editing the "original" tree that is duplicated at each point (the Tree object in this case). If we change the material there, it will automatically update across the scene (make sure you press "Use Nodes" if the surface options don't look like this):

<figure><img src="../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (14) (1).png" alt=""><figcaption></figcaption></figure>

If you would like to do any other conditional coloring, that would have to be done through the geometry nodes.

We can repeat this process entirely for the alive\_trees object, replacing the duplicated object and its material accordingly (making it green). However, there is one major caveat: the dead\_trees object duplication method had little to no lag since the number of duplicated objects was relatively small (about 14,000). However, the number of alive\_trees is substantially larger (around 650,000). If we were to try and duplicate the objects **and** see them in the viewport, it would tank our software's performance. So, before we perform the same action, **be sure that the alive\_trees object is turned off in the viewport**. This will allow Blender to do the duplicating calculations on the backend without actually having to display more than half a million objects at once.

To test that the trees have loaded in properly, render a random frame in the animation, positioning the camera close enough to the street to see the tree objects. Ensure that the alive\_trees object is set to be visible in the render. A minute or so later, you should see the tree.

Note that if you're not seeing the leaves correctly (showing as pink) this means that **the leaf texture didn't load properly**. To fix it, simply go to the original AliveTree object, go to the Materials tab, and click on the Tree Branch material and open it in a Shader Editor. Then, adjust the image texture to match the tree branch material in the [GitHub](../blender\_trees/tree\_branch.png). If you plan to render using Adroit, make sure that you place the tree branch PNG in a location whose relative path is transferrable.

## General Shapefile Materials

***

The easiest of changes to materials we have to make is to the flood2050 and nyct2020 objects. Since these shapefiles were imported as a singular objects, all we have to do is add a material to that singular object. We'll start with the flood2050 object: Simply select it, and add a new emission material, appropriately colored blue, and you'll immediately see the changes in the viewport (note that I'm moving the object up 2m in the Z, for visibility):

<figure><img src="../.gitbook/assets/image (24).png" alt="" width="563"><figcaption></figcaption></figure>

Do the same for the nyct2020 object. With it selected, add a new material with a somewhat darker shade than the base plane (like #E5D8CE, for instance). I'm also moving the object up along the Z, but only by 0.1m this time:

<figure><img src="../.gitbook/assets/image (25).png" alt="" width="563"><figcaption></figcaption></figure>

## Shapefile Border Materials

***

One of the more useful shapefile objects that we imported is for borough boundaries (titled "geo\_export\_b1e80c11-1f1f-419f-b92b-13fe75482d5d"). If we're planning to have the camera far away from the scene, having these outlines (along with the base map) to differentiate the base plane from the city is very useful.&#x20;

There's just a few things we have to get set up to use the boundaries effectively. **Make sure to follow these steps in order** (doing it out of order might cause our object to become 2D, where certain modifiers won't work).

First, assign a material to the object. Since this is meant to be an outline, I'm going to use a solid black color. Make sure to label the material accordingly:

<figure><img src="../.gitbook/assets/image (27).png" alt="" width="375"><figcaption></figcaption></figure>

Be sure to apply the material to all the selected objects in the collection via the dropdown on the left (Copy Material to Selected). Next, with all the objects selected, we'll press Tab -> 2 -> A -> E -> 100 and hit enter. This series of steps takes all the edges of our objects, and moves them up 100m so that we get a wall at each border location:

<figure><img src="../.gitbook/assets/image (29).png" alt="" width="310"><figcaption></figcaption></figure>

Then, still with all the objects selected (and in edit mode), press 3 and select any top **and** bottom face (i.e. a face above the city running horizontally across and the corresponding face below the city). Here's a top face (left) and a bottom face (right) simultaneously selected (by holding shift) for reference:

<div>

<figure><img src="../.gitbook/assets/image (30).png" alt="" width="290"><figcaption></figcaption></figure>

 

<figure><img src="../.gitbook/assets/image (31).png" alt="" width="277"><figcaption></figcaption></figure>

</div>

The, press Shift + G -> Normal -> X -> Only Faces. This selects and deletes all the faces that are going facing the same direction as the ones we selected, leaving just the vertical edges (what we want).

Next, we'll add a solidify modifier with a Thickness of 100m (remember, we're trying to make this visible from far away), making sure to press the drop down and select "Copy to Selected" to paste the modifier on all the border objects:

<figure><img src="../.gitbook/assets/image (28).png" alt="" width="375"><figcaption></figcaption></figure>

With all our border objects containing the right material and modifiers, we can now preview the desired border effect:

<figure><img src="../.gitbook/assets/image (32).png" alt="" width="260"><figcaption></figcaption></figure>

Make sure to hide this object in the render if the camera is positioned close enough to the city (where the viewer will be able to differentiate city from baseplane.

## Transparent Raster Materials

***

When we deleted all the materials to set up the materials for buildings and roads, we also deleted the materials corresponding to our three TIF files, so we'll have to re-do them here. We're also going to assign different color scales to the images and make their backgrounds transparent, since Blender cannot import geo-referenced tif images with transparent backgrounds.

Note that **you might want to move these three TIF files up 1m or so**, to make sure they won't collide/overlap with our base plane, which is located at Z=0m.

We'll start with "dead\_tree\_v1" which is a heatmap for dead trees in NYC. With this object selected, add a new material in the Shader Editor workspace. Add an Image Texture node and connect it to the Principled BSDF. Also add a UV Map with the rastUVmap value and connect it to the vector of the Image Texture node. The result should look like this and you should now see the raster image in the 3D viewport (barring object overlaps, and ensuring that you're in Rendered View):

<figure><img src="../.gitbook/assets/image (16) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Note that the UV Map node won't make a difference right now since our plane doesn't have an elevation/displacement. Still, it's good practice to leave the UV Map node connected incase we change the plane later. We'll now work on removing the image background, since its current state doesn't look too visually appealing. This node set up is based on this two minute [tutorial](https://www.youtube.com/watch?v=\_DYYlYrKvoE), where the set up is fully explained.&#x20;

First, we'll add in an emission node, a transparent node (with the color being the color of our base plane), and a mix shader connected to the material output:

<figure><img src="../.gitbook/assets/image (17).png" alt="" width="563"><figcaption></figcaption></figure>

The emission node instead of a Principled BSDF makes it such that the lighting of our scene won't affect the visibility of our plane object (since it itself is a light). Then, we combine that image emission with a transparent BSDF (with the default color) into our final image. With a Fac of 1, we won't notice any change in the 3D viewport, since the factor is what dictates how much influence each of the two Shaders has (1 means all the influence is from our emission, whereas 0 means all of the influence is from the transparent node).

With this set up in place, we'll add three more nodes: RGB, Vector Math, and a Math node. Change the Vector Math node to calculate distance, the Math node to "greater than" with a threshold of .150, and the RGB to the background color of the tif (black). Configure them like so:

<figure><img src="../.gitbook/assets/image (18).png" alt="" width="563"><figcaption></figcaption></figure>

This set up calculates the 3D distance between the background color (black) and each pixel in our tif image (3D is just how Blender interprets to colors). If that distance is greater than our threshold of .150, meaning the color is not black (.150 is a standard threshold I've found works well, but can be changed if needed), then the Fac is 1 (remember that this means the influence is with our tif emission). If the color distance is less than .150 (meaning the color is close to black), then the Fac is 0, and the pixel is colored transparent.&#x20;

This is the reason why using a TIF that contains actual data points with the same color as the background is problematic: they will get keyed out, even though we want them to retain their color. As stated in an earlier page, consider adjusting the colors in an external program to fit the requirements for Blender manipulation.

The last change we'll make is to the colors within our tif. We can add a color ramp like so to change the colors from the standard "magma" theme to something more fitting for dead trees:

<figure><img src="../.gitbook/assets/image (19).png" alt="" width="563"><figcaption></figcaption></figure>

The actual colors are from a reference scale online, but the locations of the ticks are fairly arbitrary - unfortunately, I don't think there's a way to map specific values in an image to colors, since the output of the Image Texture node is just the RGB values of the image, nothing else (meaning Blender isn't picking up on any of the data values within the tif).&#x20;

For the color ramp, I'm just placing the beginning tick at 0 for the lowest value in the color scale, then finding a good point to put the highest value (testing to see how it looks in the 3D viewport), then filling in the middle ticks evenly.

Ideally, you should change the color scale more accurately within another software like QGIS, but if that isn't an option, this also suffices. Within another software is also where you would be able to find the information to generate a scale for the image, like one that was shown in the final video (since generating that scale isn't possible in Blender alone).

To generate that scale, I used QGIS to find the range of values (-8 to 8) and then used Google Drawings to make a scale gradient that matched the color ramp in Blender. Obviously, if you didn't change the color ramp in Blender, you can just use the given scale from whatever external GIS program you choose.

We'll now repeat this node process for each of the other two raster objects (you can copy the nodes with Control/Command + C and paste them into another object), changing some of the values of the nodes slightly, to make them accommodate for the different background colors and image files that we're using:

temperature\_deviation\_parsed:

<figure><img src="../.gitbook/assets/image (20).png" alt="" width="563"><figcaption></figcaption></figure>

tree\_heatmap\_v1:

<figure><img src="../.gitbook/assets/image (21).png" alt="" width="563"><figcaption></figcaption></figure>

## Conclusion:

***

We've now added a material to every single object in our render, which means we're ready to keyframe objects for our final animation.&#x20;

Note that in my final render, I added three "cover planes" to hide raster and vector data that I didn't have OSM buildings for. This is as simple as adding a plane with the same material as our base plane, move and scaling it to the proper location, and moving it up 1m in the Z. You can repeat this process to cover as many areas as needed, making sure to try and avoid object overlap by positioning each plane on a different Z coordinate (i.e. have one plane at location 1.1m, one at 1.2m, etc.).
