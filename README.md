# 3D Movies with GIS Data in Blender

Blender is a very powerful tool for making visualizations, especially those which can be elevated by a three dimentional presentation.&#x20;

With a passionate community of users and developers behind the software, there are a number of add-ons and tools that we can reference to generate professional-grade movies. In this workbook, we'll be going over how to produce this visual:

{% embed url="https://www.youtube.com/watch?v=0Ug4-aKhu2s" fullWidth="false" %}

As we generate this visual, I'll be introducing concepts that can be referenced to generate models of any geospatial data. **This tutorial is meant for those who have at least a beginner background in Blender and a basic understanding of GIS data.**

The following add-ons are required for this tutorial (and will probably be needed for any 3D geospacial project):

* [BlenderGIS](https://github.com/domlysz/BlenderGIS)
* [Blosm](https://prochitecture.gumroad.com/l/blender-osm)
* [Bpyproj](https://github.com/JeremyBYU/bpyproj)

You can add these by downloading the ZIP (without unzipping) and going to Edit -> Preferences -> Add-ons -> Install and selecting the files.

Within this menu, enabling the Material Utilities add-on might also be helpful (but not required) to manage the number of materials we have in our scene.

For this project and generally, it might be useful to have a third-party source to double check alignment and configure GIS data in ways that aren't possible in Blender. For this project, [QGIS](https://www.qgis.org/download/) is recommended, but not necessary.

Finally, it's going to be very useful to access the System Console to see print statements from our add-ons. On Windows, this can be done by clicking Window, then "Toggle System Console". On Mac, we'll have to open Blender from the Terminal to gain access to the system console, which will then print on the Terminal itself. You can look into a tutorial on how to do that on Blender's [website](https://docs.blender.org/manual/en/latest/advanced/command\_line/launch/index.html).
