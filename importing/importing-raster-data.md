# Importing Raster Data

## Introduction

***

Importing raster data is very similar to importing vector (shapefile) data, with some minor changes to menu options and placement.

This section assumes that you've **set a scene CRS**. To read more about that view the [Importing Vector Data](importing-vector-data.md) page.

We'll be using the BlenderGIS add-on for this section, so make sure it's **installed and enabled**.

If you're planning on rendering your program using Adroit, **make sure to put these raster files in a location that can be transferred to a new directory** and maintain its connection to the original Blender file with a relative path (i.e. make a folder in the same location as the Blender file for all the raster images, so that when you need to transfer files to Adroit, your files are all in one place and the relative path to those files is maintained).&#x20;

### Of Note:

An important note about .tif files in Blender is about their transparency. At times, we'd like to have a .tif with a transparent background. However, in Blender, **image transparency is complicated and often difficult to achieve depending on the original file format**.&#x20;

For this tutorial, the one-size-fits-all workaround I'm using relies on "keying out" a color and changing it to the background color to appear "transparent". This can sometimes create conflict for .tif files where the background color is repeated in the actual image data. In fact, for one of the images used in my render, this problem occurred. To create a workaround for the workaround, I adjusted the color scale of the .tif file to not use any of the background colors. However, if this isn't possible or if the data just doesn't work with the "keying out" method, consider adopting a more custom solution from online, or finding another way to deal with creating transparency in Blender.

## Importing Raster Data in Blender

***

Like we did earlier for shapefiles, we'll select the GIS menu on the top of the 3D viewport:

<figure><img src="../.gitbook/assets/image (22) (1).png" alt=""><figcaption></figcaption></figure>

From here, we'll select Import -> Georeferenced raster. In the file selector, we'll select a .tif (not .tiff) file. I'll start with the heatmap of all the dead trees, appropriately named "[dead\_treev1.tif](https://github.com/nikhilc52/blender\_gis\_nyc\_trees/blob/b8e2d3d38b7b5c7a72589d1dc124ea76433ad9f1/gis\_data/raster\_files/dead\_tree\_v1.tif)".

Before we select the "Import georaster" option, **ensure that the settings on the right column are correct**, since the BlenderGIS add-on places the settings for raster files here instead of after selecting the file (like for .shp files):

<figure><img src="../.gitbook/assets/image (23) (1).png" alt="" width="563"><figcaption></figcaption></figure>

While the placement of the settings is different, the actual settings are essentially the same as the .shp import, except for the "Mode", which can be changed based on your goals for the image. For us, we'll leave it as the default, which is to make a new plane that contains an image corresponding to the .tif.

After importing, verify that the .tif lines up with the rest of our data:

<figure><img src="../.gitbook/assets/image (24) (1).png" alt="" width="563"><figcaption></figcaption></figure>

If we turn off viewport visibility for the other objects, we can verify that the colors imported correctly:

<figure><img src="../.gitbook/assets/image (26) (1).png" alt="" width="563"><figcaption></figcaption></figure>

We can repeat this process for the two other raster files used in this render: the [alive tree heatmap](https://github.com/nikhilc52/blender\_gis\_nyc\_trees/blob/b8e2d3d38b7b5c7a72589d1dc124ea76433ad9f1/gis\_data/raster\_files/tree\_heatmap\_v1.tif) and the [temperature deviation map](https://github.com/nikhilc52/blender\_gis\_nyc\_trees/blob/b8e2d3d38b7b5c7a72589d1dc124ea76433ad9f1/gis\_data/raster\_files/temperature\_deviation\_parsed.tif). The temperature deviation map is originally from the [New York City Council](https://github.com/NewYorkCityCouncil/heat\_map/blob/main/data/output/f\_deviation.tif), but parsed to multiple bytes (since the original format, though containing the same data, was just one byte) with QGIS. The CRS was also transformed from its original EPSG:4326 to EPSG:2263 when I parsed it, so we don't need to specify the raster CRS.

## Conclusion

***

Once those two additional rasters are also imported, the outliner should contain these files, and look something like this:

<figure><img src="../.gitbook/assets/image (27) (1).png" alt=""><figcaption></figcaption></figure>
