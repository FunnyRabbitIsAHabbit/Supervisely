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

### Findings and solution (100%)

[This particular Stackoverflow answer](https://stackoverflow.com/questions/61051120/sliding-window-on-a-python-image) helped divise my approach.

Scripts [split.py](split.py) and [merge.py](merge.py) solve the challenge 100%.
File [Unknown.jpg](Unknown.jpg) has been tested as input and [new.jpg](new.jpg) is the output.

Package [Slidingwindow](https://github.com/adamrehn/slidingwindow) would be an overkill, IMO.

## Initial Challenge #2

Write a visualizer for the DAVIS dataset. The script should output such a [result](https://davischallenge.org/images/DAVIS-2017-TrainVal.mp4): take N videos, glue them into one after another or in the form of [such
grids](https://davischallenge.org/images/teaser/montage-2017.jpg).

### Findings and solution (100%)

[This page](https://mlhive.com/2021/05/write-videos-from-images-using-scikit-video) and [this](https://www.scikit-video.org/stable/io.html#writing) helped divise current 100% *non-grid* - continuous - solution ([process_davis_videos.py](process_davis_videos.py)) for video making from images.
Solution produces [output.mp4](output.mp4) video file from N (10 by default) random categories.

There might occur an AssertionError:

> AssertionError: Cannot find installation of real FFmpeg (which comes with ffprobe).

For Debian derivatives of Linux this error can be resolved as follows:

`apt-get install --no-install-recommends ffmpeg`

### *Note*

* You might want to run

    `pip install -r requirements.txt`

* Paths are Unix-like

* Python version used in development is 3.10.7

* [This DAVIS zip](https://data.vision.ee.ethz.ch/csergi/share/davis/DAVIS-2019-Unsupervised-test-challenge-480p.zip) has been used in development (Unsupervised, Test-Challenge 2019 - Images, 480p)


