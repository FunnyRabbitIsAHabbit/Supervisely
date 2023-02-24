# Supervisely
*Test task for **Python Developer** role*

## Initial challenge #1

Write two scripts: 'split' and 'merge'. 'split' script takes a picture as input,
size (h, w) windows in pixels or percent, displacement by X and Y, and cuts
images with Sliding Window approach. The result is stored in the directory - all
The settings should be sewn into the names of the resulting pictures. Script
Merge takes a folder with chopped pictures to the input and constructs
the original from them. At the end, it is necessary to validate that resulting pixels
are same as in the original image.

## Findings #1

[This particular Stackoverflow answer](https://stackoverflow.com/questions/61051120/sliding-window-on-a-python-image) helped divise my approach.

Scripts [split.py](split.py) and [merge.py](split.py) solve the challenge 100%.
File [Unknown.jpg](Unknown.jpg) has been tested as input and [new.jpg](new.jpg) is the output.
