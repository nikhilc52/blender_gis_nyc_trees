# Appendix

## Errors in Original Blender File

In the original Blender file in [GitHub](nyc\_trees.blend.zip), there are a few minor discrepancies between what's within that file and what's explained here. In general, you should tend to follow the directions specified within this book rather than copying any errors that exist in the original file:

* The alignment of the buildings to the rest of the BlenderGIS imports was done manually rather than using the CRS and alignment provided in Blosm
  * I only discovered the very elusive solution to Blosm projections after the final render was complete
* The coastlines are not scaled to 0 along the Z axis
* The building height for all non map\_20.osm collections is unadjusted
* There are several unneeded keyframes for the render visibility keying - they make no difference in the final product
  * The keyframes are structured as if render visibility can be interpolated between frames, even though it is binary (i.e. no need to have keyframes that are adjacent to each other to switch between on/off)

## Video Tutorial

It might be useful to see a video tutorial going through the steps outlined in here for further clarity. This tutorial is linked here:



## About

This reference book was developed in 2024 by Nikhil Chinchalkar under the guidance of Carolina Roe-Raymond and Eliot Feibush for Princeton University's Research Computing department.

<figure><img src=".gitbook/assets/lotus.png" alt="" width="146"><figcaption></figcaption></figure>
