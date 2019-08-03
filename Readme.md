# Manga Image Classifier

An image classifier built around the desire to match two images, one a real life portrait and the other an artificial manga drawing. **shown here**: https://imgur.com/a/GWV0IOw


It runs different similarity checks such as:
1. Structural similarity indexes
  * MSE
  * SSIM
2. Edge detection and tracer into black & white
  * Laplace Transforms
3. Shape and object tracing
  * Contours

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

1. Two images, required to be the **exact** same dimensions.

### Prerequisites

What things you need to install the software and how to install them

1. Python3 is required, please upgrade from Python2 if you have not already done so.


1. Make sure to have the following modules installed: `skimage` and `python-opencv`.

## Running the tests

1. Drop in your own images to the `./images/` directory and run the classifier:
```
python3 compare.py
```

2. A matlab plotter GUI will popup indicating the similarity factor between the two input images.

## Agenda

1. Neural networking infrastructure to create layers to classify the edges (similarity)

## Articles

* https://docs.opencv.org/3.2.0/d5/d69/tutorial_py_non_local_means.html
* http://www.robindavid.fr/opencv-tutorial/chapter5-line-edge-and-contours-detection.html
* https://people.eecs.berkeley.edu/~aramdas/reports/DBreport.pdf
* https://www.ml.uni-saarland.de/code/GraphDemo/HeinLuxburg_SlidesSimilarityGraphs.pdf
* http://www.cs.cornell.edu/~dph/papers/HKR-TPAMI-93.pdf