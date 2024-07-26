# Rendering on Adroit

## Introduction

***

While rendering on one's own computer is simple, you can also render on a cluster with multiple parallel batches to speed up rendering. For instance, you can use a super computer to render frames 0 to 1000, 1000 to 2000, etc. all at the same time (in simultaneous commands).

**This page is only applicable if you have a Princeton University NetID.**

## Rendering on Adroit

***

We'll be using the Adroit super computer for this process. The first step in rendering Blender files is to login to Adroit on a web browser. Go to [https://myadroit.princeton.edu/](https://myadroit.princeton.edu/) and log in using your NetID.

Once you're logged in, go to the top bar and press Files and click on your home directory. From here, create a new folder somewhere that is going to hold your Blender files:

<figure><img src="../.gitbook/assets/image (40).png" alt="" width="563"><figcaption></figcaption></figure>

**Make sure to add in your image files for the raster data in the same location as it is locally**, so that the Blender file on Adroit can reference the same images with the same relative path. I'm also adding the PNG files I used to make the trees, since they are required for loading the alive\_trees texture within our model.

**Be sure that the Blender file you're inputting has all the proper settings**, since we won't be able to edit them from Adroit (don't worry about the file output path or the render engine, we'll coordinate those with Adroit later ).

Next, open up a terminal on your local computer. We'll first need to ssh into adroit-vis:

```
ssh NETID@adroit-vis.princeton.edu
```

Now, we'll need to run (**and edit**) one command to render a set of frames:

```
/home/efeibush/blender/blender-4.2.0-linux-x64/blender -b file.blend -o /home/NETID/Blender/nyc_trees/images -E CYCLES  -s 1 -e 5 -a  --  --cycles-device OPTIX+CPU
```

This command uses the Blender application in the efeibush directory to open the blender file in the background (-b file.blend), sets an output path (-o /home/NETID/) , uses the Cycles render engine (-E), starts at frame 1 (-s 1), ends at frame 5 (-e 5), renders all frames between (-a), and uses the OPTIX cycles device along with the CPU to render out frames (-- --cycles-device OPTIX+CPU). Change the variables to match your scene. You can read more about how to customize the settings of this command [here](https://docs.blender.org/manual/en/latest/advanced/command\_line/arguments.html#command-line-args-cycles-render-options).&#x20;

Make sure that you're in the working directory where the .blend file is located.

When you run this command, you'll see a bunch of text outputted that marks how far along Blender is when rendering each frame. You can make sure each frame is being rendered properly by looking back in the home directory on [https://myadroit.princeton.edu/](https://myadroit.princeton.edu/).

### Of Note

Note that you can also open up the Blender GUI from Adroit:&#x20;

On [https://myadroit.princeton.edu/](https://myadroit.princeton.edu/), go to My Interactive Sessions and click on Desktop under the Interactive Apps section to the left. You should request an appropriate amount of time.

Once you're able to launch the desktop, open it up and click on the middle terminal icon at the top left:

<figure><img src="../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

This should open up a terminal within the virtual desktop titled "Mate Terminal".

Next, run the following command on the terminal:

```
/home/efeibush/blender/blender-4.2.0-linux-x64/blender
```

This opens up a copy of Blender that is stored within the efeibush directory. You should now see a copy of Blender within your virtual desktop. Within Blender, go to File -> Open and open the Blender file you stored at the start of this section. You'll now see the Blender file running on Adroit, and you can edit the file and render it from here (though it would take up more resources).&#x20;

## Conclusion

***

This process can then be duplicated in a new terminal, by following the exact same steps above. From this, you would be able to split up a render into multiple parallel execution statements to very easily simplify the rendering process and get a final render much faster. For instance, one command could render frames 1 to 100, then you could open another terminal and command for from frames 101 to 200, etc.

To save the images you outputted to your directory on Adroit, you can use this command on a local terminal:

```
scp -r adroit:/home/NETID/Blender/nyc_trees/images/ /Users/XXXXXX/Documents/images/
```

This takes the all files from Adroit and saves them to the local directory, where you can then import them into a video editing software.
