# Appendix

## Errors in Original Blender File

In the original Blender file in [GitHub](nyc\_trees.blend.zip), there are a few minor discrepancies between what's within that file and what's explained here. In general, **you should tend to follow the directions specified within this book** rather than copying any errors that exist in the original file:

* The alignment of the buildings to the rest of the BlenderGIS imports was done manually rather than using the CRS and alignment provided in Blosm
  * I only discovered the very elusive solution to Blosm projections after the final render was complete
* There are several unneeded keyframes for the render visibility keying - they make no difference in the final product
  * The keyframes are structured as if render visibility can be interpolated between frames, even though it is binary (i.e. no need to have keyframes that are adjacent to each other to switch between on/off)

## Video Tutorial

It might be useful to see a video tutorial going through the steps outlined in here for further clarity. This tutorial is currently a work in progress and **will be published soon**.

## Rendered Video Editing

Here are some notes about the final video:

* The final rendered output in Blender was then editing using Adobe Premiere Pro&#x20;
* The voiceover was recorded using Voice Memos and processed using Adobe Podcast&#x20;
* The Wiki table for the demographics in the Bronx was created in R, using the script found in the [repo](other\_resources/demographics.R)
  * The data is originally from [Wikipedia](https://en.wikipedia.org/wiki/Race\_and\_ethnicity\_in\_New\_York\_City)
* The reference for some of the statistics about the percentage of dead trees within Hunts Point comes from manipulating the data as described in this R script in the [repo](other\_resources/tree\_analysis.R)
* The source for the statistic about Black New Yorkers dying at twice the rate as white ones comes from [NYC Environment and Health](https://a816-dohbesp.nyc.gov/IndicatorPublic/data-features/heat-report/)
* The source for the information about trees and runoff comes from the [EPA](https://19january2017snapshot.epa.gov/soakuptherain/soak-rain-trees-help-reduce-runoff\_.html)

## About

This reference book was developed in 2024 by **Nikhil Chinchalkar** under the guidance of **Carolina Roe-Raymond** and **Eliot Feibush** for Princeton University's Research Computing department.

<figure><img src=".gitbook/assets/lotus.png" alt="" width="146"><figcaption></figcaption></figure>
