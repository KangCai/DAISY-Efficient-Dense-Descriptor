# DAISY-Efficient-Dense-Descriptor

[中文](https://github.com/KangCai/DAISY-Efficient-Dense-Descriptor/blob/master/README_zh_CN.md)

Kang is glad you find me. This is an project for realization of paper "DAISY: An Efficient Dense Descriptor Applied
to Wide-Baseline Stereo". Any suggestions or comments well be welcome.

---

### Abstract

In this paper, we introduce a local image descriptor, DAISY, which is very efficient to compute densely. We also present an
EM-based algorithm to compute dense depth and occlusion maps from wide-baseline image pairs using this descriptor. This yields
much better results in wide-baseline situations than the pixel and correlation-based algorithms that are commonly used in narrowbaseline stereo. Also, using a descriptor makes our algorithm robust against many photometric and geometric transformations. Our
descriptor is inspired from earlier ones such as SIFT and GLOH but can be computed much faster for our purposes. Unlike SURF,
which can also be computed efficiently at every pixel, it does not introduce artifacts that degrade the matching performance when used
densely. It is important to note that our approach is the first algorithm that attempts to estimate dense depth maps from wide-baseline
image pairs, and we show that it is a good one at that with many experiments for depth estimation accuracy, occlusion detection, and
comparing it against other descriptors on laser-scanned ground truth scenes. We also tested our approach on a variety of indoor and
outdoor scenes with different photometric and geometric transformations and our experiments support our claim to being robust
against these.

---

### Algorithm

**1. For each pixel, calculate the 1-D gradient on axis of X and Y, then calculate the direction and magnitude of the gradient,
and calculate its contribution to histogram of directions (weight proportion)**

The gradient in different directions can be calculated by one-dimensional gradient, which is efficient, as shown in the figure below

<img src="https://raw.githubusercontent.com/KangCai/DAISY-Efficient-Dense-Descriptor/master/images/doc/1.png"/>

**2. For each pixel, calculate its contribution to histogram of directions after the gaussian smooth with different 
scale (sigma, standard deviation).**

Not only the histogram of the same pixel can be reused by multiple sampling points around it, which speeds up the calculation efficiency; 
The outer histogram of the same pixel can also be calculated from the inner histogram, as shown in the figure below,

<img src="https://raw.githubusercontent.com/KangCai/DAISY-Efficient-Dense-Descriptor/master/images/doc/2.png"/>

**3. For a pixel, take the histogram of different layers and directions as the descriptor, assuming that the dimension is D.**

Dimension D = number_of_rings * d(h) = (rings * histograms + 1) * orientations, as shown in the figure below,

<img src="https://raw.githubusercontent.com/KangCai/DAISY-Efficient-Dense-Descriptor/master/images/doc/3.png"/>

**4. Sampling with a width and height step to get P samples. So the total data of a image descriptor is P * D**

Sampling with a width and height step, as shown below is a schematic of feature extraction with sampling,

<img src="https://raw.githubusercontent.com/KangCai/DAISY-Efficient-Dense-Descriptor/master/images/doc/4.png"/>





