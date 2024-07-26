# Creating an Optimized Render

## Introduction

***

If we were to render a medium-length animation with the default settings, our render would take days to complete. This is due to the sheer size of our file, objects, and lights. The Blender file used to create the final render you saw in the introduction was just under 500 MB, with millions of vertices, faces, and triangles.

To compensate for this, we'll need to sacrifice some quality in our render. Still, **if we choose the right export settings** we can get a relatively fast render time with a good-looking quality.

### Of Note

When I rendered my image sequence for the final movie, **Blender crashed at whatever frame I turned off the render visibility for the alive\_trees object**, so I'd have to restart the animation to render the rest of the animation after it (since I saved the PNGs that outputted before the crash). Be mindful that the same might happen to you - there isn't a quick fix for it, just know that Blender might crash during the render and prepare to have to render the animation in two parts if needed (**be sure to save your file before you render**).

Also note that I had a bug where either the dead\_trees object or the alive\_trees object wouldn't show up in the final render. I believe this is due to the file overloading Blender's memory, and can be fixed by **saving the Blender file at the frame where the problem occurs and re-opening the Blender file at that same location** (then rendering).

## Understanding Time-Consuming Frames

***

The render for the final movie took over 12 hours (for 3,200 frames). However, some frames took significantly longer than others to render. Here's a graph of all the render times for each frame:

<figure><img src="../.gitbook/assets/image (12).png" alt="" width="375"><figcaption></figcaption></figure>

The frames that took the longest to render (0 - \~1100 and \~3100+) were the frames where all the alive trees were showing. This is most likely due to the fact that each of these (\~600,000) points were represented by a tree object with an emission material, meaning that Blender had to do light calculations (which are fairly expensive) for every visible tree, which adds to the render time.

The middle frames (\~1100 - 2300) only took a few seconds each, since all the trees were hidden, meaning Blender only had to do light calculations for the sun object. The latter part of the middle section (\~2300 - \~2700) were frames that showed all the dead trees (\~14,000 points). Though these were represented by emission materials, since they were significantly less points than the alive trees, the render time didn't take quite as long as the frames where alive trees were showing.

Knowing this information might help you understand where the of render time is spent, which can help you compensate for renders that are taking too long (by showing alive trees for a shorter time, for instance).&#x20;

Also keep in mind that certain frames that are just "held" in the animation (frames where there is no camera movement and the given frame is shown for the whole time) can be cut down to just one frame, and held in another video editing software. For example, if frames 100-150 had the same PNG output, you could shorten the sequence in Blender to just frame 100 and then copy that frame 50 times in another software, shortening the render time in Blender by 49 frames.

## Settings to Speed Up Renders

***

There are a few settings that we can change to help speed up renders. Here's a table of all of them, to see the render time when each one of them is turned on (all the other settings for each row are default, so the setting is isolated). The frame we're rendering is the first frame in the animation, which shows both the buildings and the alive trees (which is one of the more time-consuming frames in the animation).&#x20;

The first change I'm making is to the number of samples, which I'm taking down **from 4096 to 128**. This causes a very minor loss in quality, but is necessary since a single frame with 4096 samples would take hours to render. **This change will be applied in tandem with all the changes shown in the table:**

| Isolated Setting (w/ 128 samples)                                  | Frame 1 Render Time (S) | Setting Description                                                                                        | PNG Link                                                           |
| ------------------------------------------------------------------ | ----------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Default Cycles Settings                                            | 44.51                   | Default Cycles settings                                                                                    | [GitHub](../other\_resources/sample\_renders/default.png)          |
| 0.5 Noise Threshold (Render Properties -> Sampling -> Render)      | 25.83                   | Noise level to stop sampling at (higher means more image noise)                                            | [GitHub](../other\_resources/sample\_renders/noise\_threshold.png) |
| Persistent Data (Render Properties -> Performance -> Final Render) | 38.55                   | Keep data for re-renders (useful for files where rending might be done more than once) \[uses more memory] | [GitHub](../other\_resources/sample\_renders/persistent\_data.png) |

You can read more about these settings what they do [here](https://docs.blender.org/manual/en/latest/render/cycles/render\_settings/sampling.html).

Combining the two above settings as well as doing minor things like making sure all other computer applications are closed and that the **Blender file is in Solid Mode** in the 3D viewport (saves memory) can help to significantly speed up render times.

## Exporting As A PNG Sequence

***

When we render an animation, it's a good idea to render it as a PNG sequence:

<figure><img src="../.gitbook/assets/image (14).png" alt="" width="375"><figcaption></figcaption></figure>

In the case of an unexpected crash, exporting as a PNG is ideal, since a crash won't alter the already exported PNGs and you can pick up right where you left off (and easily see where to start from again by the PNG name, which contains a frame number).&#x20;

It's good practice to do a "dummy" render at a lower frame rate (so less frames/total render time) before the final product, to see if everything looks correct. To do so, edit the "Step" value in the Output Properties tab:&#x20;

<figure><img src="../.gitbook/assets/image (15).png" alt="" width="563"><figcaption></figcaption></figure>

The higher the value, the more frames will be skipped between each rendered frame, making the animation render quicker, but at a lower frame rate (rendering every nth frame). Having a Step of 10 is a good place to start, since it'll create an image sequence with one tenth the frames in one tenth of the time of the final render.

Make sure that the "dummy" render looks good before rendering the final product. Also make sure that you render the "dummy" render and the final render into two different locations to avoid files being overridden.

Once the sequence is rendered, if you wanted to turn the PNG sequence into a video, you can import the files into most video editing softwares as a image sequence, and it will automatically turn it into a video. If you don't want to do that in an external software, Blender also provides its own video editing.

While I won't go too in depth about it (since it really isn't the best platform for editing), you can go to File -> New -> Video Editing to generate a new video editing space. From there, press Add -> Image/Sequence and select the PNGs you want to import making sure that they are ordered correctly in the file manager (ordering by name).

You can edit the duration, frame rate, change the output file name, location, and format in the Output Properties (FFmpeg video is standard) tab at the top right.&#x20;

## Conclusion

***

We've now successfully set up settings for an optiminal render, and we can get that render of PNG sequences into a video format if needed.
