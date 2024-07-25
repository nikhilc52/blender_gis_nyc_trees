# Importing Vector Data

## Introduction

***

Importing vector and raster data is simple to do, but there are complications that can make things difficult to understand, so it's important to go through this section step-by-step.

We'll be using the BlenderGIS add-on for this section, so make sure it's installed and enabled.

## Setting a Scene CRS

***

The first step in setting up a scene for GIS data in Blender is to set a CRS.&#x20;

There are two main ways to set a scene CRS. One way is to set it before the initial import, and have the initial import (and all those after) be transformed to that CRS.&#x20;

We can do this by going into View -> Geoscene, and setting **both** the CRS and Geo/Proj rows accordingly:

<figure><img src="../.gitbook/assets/image (11) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

However, this approach comes with the caveat of having the data slightly offset from the origin, since the origin becomes the mid point of the specified CRS area and not the mid point of the data we're importing.&#x20;

For instance, if we set the CRS to EPSG:2263, the origin in Blender (0,0,0) would be somewhere in the middle of New York, even though we're only dealing with data from NYC.&#x20;

<figure><img src="../.gitbook/assets/image (10) (1) (1) (1) (1).png" alt="" width="398"><figcaption></figcaption></figure>

Our data would still be accurately placed, but slightly annoying to work with, since we'd have to move and tweak a  few settings to accomodate from the offset. Still, this is a viable option depending on the data, but for the work we're doing, instead of dealing with that, I find it is much easier to just have the initial import be the baseline CRS, and have objects import relative to that.

Note that changing a scene CRS after it has been set and objects have been imported, will not re-align the already imported objects, and only affect the new ones.

## Importing Vectors (Shapefiles) in Blender

***

### Initial import:

For our initial import, we'll make sure to choose a file that has a CRS we'd like all the other files to follow. Click on the GIS drop down on the top menu bar of the 3D viewport.

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1).png" alt="" width="350"><figcaption></figcaption></figure>

From here, go to Import -> Shapefile and select the .shp file you want to import. We'll start with the NYC 2020 Census Tracts file, which you can download from [here](https://www.nyc.gov/site/planning/data-maps/open-data/census-download-metadata.page).

Once selected, a menu should pop up showing some options for projecting.

<figure><img src="../.gitbook/assets/image (12) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

We can leave that first field as is: even though we don't want any elevation, since the shapefile we're using isn't 3D, the geometry z-value will be 0 anyway. We can leave the next two boxes unchecked as well, since those options don't fit the purpose of this import (which is just to be a background map). Next, the CRS is very important.

Since this is our initial import, and we haven't yet specified the scene CRS, this import will set the scene CRS. We can click the "+" to add a new CRS, since by default, the BlenderGIS addon doesn't come with EPSG:2263. From there, we can query our file's CRS. Note that you can find any .shp file's CRS by looking in its .prj (projection) file with a text editor.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt="" width="235"><figcaption></figcaption></figure>

If we click "OK", then select the CRS from the drop down, then press "OK" again and wait a few seconds, we'll see our map in the 3D viewport:

<figure><img src="../.gitbook/assets/image (19) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Note that since we have access to the System Console (see introduction page for more details), we can see a "progress bar" for importing the shp:

```
0%, 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%
INFO:BlenderGIS-master.operators.io_import_shp:Build in 0.358552 seconds
```

While this file went too fast for us to make good use of this information, other files will take longer.

### Additional imports:

We'll now repeat this exact process for the [flooding data](https://data.cityofnewyork.us/City-Government/NYC-Stormwater-Flood-Map-Moderate-Flood-with-2050-/5rzh-cyqd/about\_data), with some slight changes to the import menu.&#x20;

Once we've selected a file, we'll see a different menu pop-up:

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Note that a scene georeferencing section is now visible, which matches our shapefile CRS, so we don't need to "Specify shapefile CRS". So, without changing anything, if we press "OK" we should see this in our 3D viewport:

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="548"><figcaption></figcaption></figure>

Note how the flooding is nearly perfectly aligned with our background map.

### Separate objects and different CRS:

For other .shp files, we'll need to change a few settings. When we import our [borough boundaries](https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm) file, we need to specify that we want to import our data as separate objects, separated by the "boro\_name" attribute, which is one of the few attributes within our .shp file. This is so that we can easily separate different boroughs for specific, individual analysis.&#x20;

Note that the more objects we need to separate, the longer the import will take. Luckily, there are only 5 boroughs in NYC, so this is a very quick import.

Note that the CRS for this file is different from the others, so we'll need to specify that in the "Specify shapefile CRS" dropdown:

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Importing the file under these settings should result in this object within the 3D viewport:

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

We can repeat this same process with the [2009 CHS survey](https://www.nyc.gov/site/doh/data/data-sets/maps-gis-data-files-for-download.page), but we'll swap out the field for "FIRST\_BORO", and since the survey has the same CRS as the scene, we don't need to specify it. If you're curious about what all the attributes mean, you can look at the corresponding .xml file for more information, or look at the website for their methodology and descriptions.

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Importing points

The last set of files we need to import are sets of points for each location of each tree. We have one file for all the alive trees and one file for all the dead ones (the [original file](https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/pi5s-9p35) isn't split - I've linked the split files in the [Data Sources](../data-sources.md) page, but you can create them yourself in QGIS). Since the [dead ones](https://github.com/nikhilc52/blender\_gis\_nyc\_trees/tree/b8e2d3d38b7b5c7a72589d1dc124ea76433ad9f1/gis\_data/vector\_files/nyc\_tree\_census\_2015\_dead) will take less time (there are fewer dead trees, so fewer points), we'll start with that.&#x20;

The steps we take to import the points are the exact same as before - the only difference is that the resulting object is going to be a set of verticies instead of a plane.

<figure><img src="../.gitbook/assets/image (13) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (18) (1) (1).png" alt="" width="504"><figcaption></figcaption></figure>

This looks good, so we can move on to the [alive set](https://github.com/nikhilc52/blender\_gis\_nyc\_trees/blob/b8e2d3d38b7b5c7a72589d1dc124ea76433ad9f1/gis\_data/vector\_files/nyc\_tree\_census\_2015\_alive.zip) of trees, which will take a little longer to import. Remember that you can see progress on the Terminal/Console Output page.

<figure><img src="../.gitbook/assets/image (19) (1) (1).png" alt="" width="482"><figcaption></figcaption></figure>

Note that you if we were to render this right now, we wouldn't actually be able to see the points - verticies aren't visible in a 3D space. To see them, we'll have to attach objects to each of the points, which we'll go over in the [Setting Up Materials and Objects](../materials/setting-up-materials-and-objects.md) page.

## Conclusion

***

<figure><img src="../.gitbook/assets/image (20) (1).png" alt=""><figcaption></figcaption></figure>

These six shapefiles are all we need on the vector side of things for this animation. Next, we'll import raster data, which will prove to also be fairly simple.
