# Keyframing for Animations

## Introduction

***

There are three main types of keyframes that we used in the final render and are universally applicable to similar Blender GIS situations:

* Camera
* Render Visibility
* Material

I'm not going to go over every single keyframe in the video, as they all involve repeating the same steps over and over again. Instead, in this section we'll go over some **foundational examples** of all these keyframing situations, so that you can apply them, if needed, across the animation.

### Of Note:

Note that you can only see the keyframes on the timeline for objects that are currently visible in the viewport. Also note that you can see all the keyframes that are currently within the scene in the Dope Sheet window, by turning off the "Only Show Selected Button":

<figure><img src="../.gitbook/assets/image (5).png" alt="" width="563"><figcaption></figcaption></figure>

## Camera Keyframing

***

Keyframing the camera is very simple and is the most common form of keyframing in Blender. We'll first add in a camera to the scene, then go into its view by pressing the camera icon on the right side of the 3D viewport. From here, we'll press the lock icon directly below the camera icon:

<figure><img src="../.gitbook/assets/image.png" alt="" width="37"><figcaption></figcaption></figure>

This locks our movement in the 3D viewport to the camera, making it very simple to move and position its view. Before we start with that, however, we'll need to change the clipping distance of the camera since our scene is very large. In the camera properties tab, make the clipping something like this (1m to 1000000m):

<figure><img src="../.gitbook/assets/image (1).png" alt="" width="375"><figcaption></figcaption></figure>

Now, at frame one on the Timeline, we'll set our camera at a good position, and keyframe it by pressing I when hovering about its location and rotation (making sure the camera is selected):

<figure><img src="../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure>

Let's now go to another position, at frame 100. Once there, press I on the location and rotation to keyframe that location:

<figure><img src="../.gitbook/assets/image (4).png" alt="" width="375"><figcaption></figcaption></figure>

If we played the animation starting from frame one, we'd now see the camera move towards the position at frame 100 as it progresses through the animation. This principle can be expanded upon and repeated to progress the camera to different positions through the scene.

## Render Visibility

***

Keyframing render visibility is how we can get certain objects to show only at certain frames.&#x20;

Suppose we wanted to only render the dead\_trees object from frames 90-100, and have it invisible for the rest of the frames. We can easily accomplish this with just three keyframes: one at frame 1 (render off), one at frame 90 (render on), and one at frame 101 (render off):

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

Because render visibility is a binary trait (meaning it can only be off or on) we don't need to worry about extrapolation in between keyframes (an object can't be half-shown), which makes the whole process a lot smoother.&#x20;

Once again, this principle can be expanded upon and repeated for the rest of the scene and animation.

## Material Keyframes

***

Material keyframes are very useful for this type of render. Specifically, if we're planning on using maps placed below buildings, we can keyframe the alpha value (opacity) of our buildings (to a lower value) to make the map more visible:

Here's a side by side of that effect for reference on its utility:

<div>

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption><p>Alpha = 1</p></figcaption></figure>

 

<figure><img src="../.gitbook/assets/Screenshot 2024-07-25 at 10.43.39 AM.png" alt=""><figcaption><p>Alpha = 0.1</p></figcaption></figure>

</div>

To keyframe the alpha value for our buildings, simply select any building object and navigate to the Material Properties tab. Once there, you should be able to keyframe the alpha value by hovering over it and pressing I for any given keyframe (if you don't see this, make sure you press "Use Nodes"):&#x20;

<figure><img src="../.gitbook/assets/image (9).png" alt="" width="363"><figcaption></figcaption></figure>

Let's try this with an example. Suppose we want the material to be solid (alpha of 1) for the first 50 keyframes. Then, for the next ten (51-60) we want it to be translucent (alpha of 0.1), and the rest of the animation, we want it to be solid again.&#x20;

We can do this with just five keyframes: one at the beginning with an alpha of 1, one at frame 50 also with an alpha of 1 (meaning we want an alpha of 1 between all those frames), one at frame 51 with an alpha of 0.1, one at frame 60 with an alpha of 0.1 (meaning we want an alpha of 0.1 between all those frames), and finally one at frame 61 with an alpha of 1:

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

The reason this keyframing set up differs from the previous (render visibility) is because of the interpolation that exists between frames (since alpha values aren't binary), so we need keyframes at more (adjacent) locations to prevent interpolation and make the alpha go from 1 to 0.1 immediately. If we wanted to have interpolation, however, we could just spread out the keyframes to have Blender smooth the alpha between different frames/values.

## Conclusion

***

By repeating these keyframes across the animation, we can create a template for a movie which can then be edited in another software. While the above is just a series of baseline actions, you can expand upon them to create cool effects and techniques that elevate a video.
