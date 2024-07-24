# Importing and Aligning OSM Data

## Introduction

***

Importing 3D Open Street Map data is where the magic happens in this visualization. Up until this point, importing the vector and raster data was something that all other programs could do (more efficiently too, probably). From now on, however, as we deal with 3D data, Blender is in a league of its own, with its customizability, beauty, and power, second-to-none.

We'll be using the Blosm extension in this module, so make sure it's installed and enabled.

Most of the difficulty in this project lies here, since the details for projection get really intricate. In fact, the changes we have to make are so slight that the creator of the Blosm add-on themselves didn't recognize that a projection method exists:&#x20;

> &#x20;Unfortunately it \[CRS projection] works only in Blender 2.8x due to external dependencies introduced in the recent version of the binaries used by the _bpyproj_ addon. Some technical details can be found [here](https://github.com/JeremyBYU/bpyproj/issues/18#issuecomment-1099333797).

With the step's we'll follow here, there will be no reason to downgrade our software.&#x20;

## Setting Up Custom Properties

***

If we go within the "Scene Properties" tab, under "Custom Properties", we can see all the values that are used to generate our scene's CRS:

<figure><img src=".gitbook/assets/image (15).png" alt="" width="333"><figcaption></figcaption></figure>

We're going to use Blosm to import OSM data. However, Blosm uses a different set of fields for its CRS alignment: "lat" and "lon", corresponding to latitude and longitiude. Right now, the fields only correspond to the parameters interpreted by BlenderGIS.

Without these parameters in place, the initial Blosm OSM import would create it's own CRS, as the mesh for whatever arbitrary location we select would **always** be placed at the (0,0,0) point of the scene, as opposed to its corresponding location on the map.

To prevent this from happening, we need to tell Blosm that there is already a CRS in place, by changing the parameter names to something interpretable. Click on the settings icon next to latitude, and change the "Property Name" to "lat". Do the same for longitude (-> "lon"):

<figure><img src=".gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

However, it would still be useful to have the original "longitude" and "latitude" fields, incase we want to use BlenderGIS again, for whatever reason.&#x20;

To get them back automatically, we can just open up the side panel, and look under "View" and "Geoscene":

<figure><img src=".gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

We can click the "Constraint" button (which looks like a rubber band _constraining_ two objects), and then press "Geo" and "Proj" to add back our references for the Geoscene (which is a attribute defined by BlenderGIS).

Now, the two panels should look like this:

<figure><img src=".gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

Note how the latitude and longitude properties mirror the exact values provided by their respective abbreviations.

## Importing OSM Files from a Server

***

Now that our scene is set up, we can work on getting some Open Street Map data. With the Blosm add-on enabled, we can click on its side panel:

<figure><img src=".gitbook/assets/image (9) (1).png" alt="" width="108"><figcaption></figcaption></figure>

The default settings are good for most applications, but you can read more about them in the Blosm [documentation](https://github.com/vvoovv/blosm/wiki/Documentation). There are still a few changes we can make before we import. First, we need to set up a directory to store the OSM files. You can do this by going into Edit -> Preferences -> Add-Ons -> Blosm (search) -> Preferences -> Directory to store downloaded OpenStreetMap and terrain files:

<figure><img src=".gitbook/assets/image (10) (1).png" alt="" width="496"><figcaption></figcaption></figure>

With that done, we'll go back to the Blosm sidebar, and (with the bpyproj add-on enabled) scroll to "Projection".

<figure><img src=".gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure>

The SRID is just a identifier for the CRS we're using (i.e. EPSG:2263). We'll put that into the field:

<figure><img src=".gitbook/assets/image (12) (1).png" alt=""><figcaption></figcaption></figure>

From here, we can select the area we want to import. Scroll back up to the top, and press "select". This will open up a webpage where you can define a rectangular area to import and adjust it. For this example, we'll start with this small area at the bottom of Manhattan. Note that larger areas will take longer to fully import (around 2-5 minutes), but you'll probably want to scale up in size to cover more ground as you piece the city together. In fact, once you've tested that alignment works with a small set of buildings, you should delete that hierarchy and import a larger first file.

Once again, remember that we can track progress (though not as well as with BlenderGIS) via the Command Terminal.

<figure><img src=".gitbook/assets/image (13) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Press "Copy" on the left, then go back to Blender and press "paste" at the top. This should populate the coordinates right below it:

<figure><img src=".gitbook/assets/image (14) (1).png" alt=""><figcaption></figcaption></figure>

From here, we can just press "import" to align and bring in our data. After a few seconds, we'll see our mesh in the 3D viewport. If we zoom in, we'll see that it perfectly aligns with the backing map:

<figure><img src=".gitbook/assets/image (16).png" alt="" width="563"><figcaption></figcaption></figure>

We can now repeat this process for the rest of the city, selecting, copying, pasting, and importing the appropriate data (our settings save, so there's no need to change anything with the CRS). While not an issue right now, try to limit the number of overlaps of buildings/coordinate boxes. The fewer the number of overlaps, the less work we have to do later when generating material colors for the buildings  (since overlaps cause buildings to darken).

You might notice that the heights of the buildings are a bit shortened. While there isn't a way to get them 100% accurate, we can do one of two things to make them look more realistic. One is just to approximate the height by scaling up the "buildings" object along the z-axis only, until it looks "normal". Another, more complicated method is to find the real-world dimensions of a building, find the building in Blender, then measuring the x and y dimensions in Blender-units (using its verticies) and scaling the z-axis only, according to how the x and y are scaled, to make everything accurate. I imagine that the first method is more efficient, since the heights of buildings don't need to be 100% accurate for the point of the video to be understood. However, this varies case-to-case.

Make sure to apply whatever changes to sizing you do to one set of buildings, to all buildings, to preserve scale.

### From a Path/File

Note that we can also import OSM data from a file instead of the online server. Every time we import an OSM from the server, Blosm also saves a copy locally, to the file directory we specified in the add-on settings. If we ever need to import a file from there (say, if the file crashed or was left unsaved) we can just switch to a file import within the Blosm settings.&#x20;

<figure><img src=".gitbook/assets/image (18).png" alt="" width="375"><figcaption></figcaption></figure>

Also note that when Blosm saves a copy of our import locally, it does so in two parts: map\_x.osm and map\_x\_extra.osm. The majority of the mesh is stored within the base copy, and when we import the base copy, Blosm automatically looks for the extra.osm file to fill in any gaps in the data. This means that whenever we select a file to import (through Blosm), we should always select the base .osm file.

<figure><img src=".gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

## Conclusion

***

After filling in our city with small (but large enough to limit overlaps) .osm files, we'll end up with something like this:

<figure><img src=".gitbook/assets/image (28).png" alt="" width="375"><figcaption></figcaption></figure>
