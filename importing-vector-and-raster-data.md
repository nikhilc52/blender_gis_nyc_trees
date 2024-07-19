# Importing Vector and Raster Data

Importing vector and raster data is simple to do, but there are complications that can make things difficult, so it's important to go through this section step-by-step.

## Setting a Scene CRS

***

The first and most important step in using GIS data is setting up a scene CRS, so that all of our data imports can be aligned.

To do this, we'll open the view tab, and go to "Geoscene":

<figure><img src=".gitbook/assets/image.png" alt="" width="91"><figcaption></figcaption></figure>

Within here, select the settings icon, and then the plus sign to add a new CRS. Since we're using data from New York and most of our files use the New York Long Island NAD83 (EPSG:2263) projection, we'll set our scene to that.&#x20;

<figure><img src=".gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Once we select what we just added, we're ready to import files:

<figure><img src=".gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

## Vectors (Shapefiles) in Blender

***

With the BlenderGIS add-on enabled, click on the GIS drop down on the top menu bar of the 3D viewport.

<figure><img src=".gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

From here, go to Import -> Shapefile and select the .shp file you want to import. We'll start with the NYC 2020 Census Tracts file, which you can download from **FIXME**.

Once selected, a menu should pop up showing some options for projecting.&#x20;

<figure><img src=".gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

We'll change the first field to "None" since we don't want any elevation (our scene won't have any elevation data since NYC is fairly flat) and leave the next two boxes unchecked as well. The CRS is very important.

Since our data uses the same CRS as the scene's, we can leave "Specify shapefile CRS" unchecked. However, if our data was different, we'd need to specify the shapefile CRS using the same process as what we did to specify the scene georeferencing.

If we click "OK" and wait a few seconds, we'll see our map in the 3D viewport:

<figure><img src=".gitbook/assets/image (5).png" alt="" width="563"><figcaption></figcaption></figure>

Note that since we have access to the System Console (see introduction page for more details), we can see a "progress bar" for importing the shp:

```
0%, 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%
INFO:BlenderGIS-master.operators.io_import_shp:Build in 9.257671 seconds
```

We'll now repeat this process for the some of our other .shp files. Since all of these files contain the same&#x20;
