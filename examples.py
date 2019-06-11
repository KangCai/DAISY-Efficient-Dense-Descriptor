# coding=utf-8

from skimage import color
from skimage.feature import daisy
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt
import time

R = 120 # Distance from center pixel (radius)
E = 40 # Distance between descriptor sampling points (step)
Q = 2 # Number of layers (rings)
T = 6 # Number of histograms at a single layer (histograms)
H = 8 # Number of bins in the histogram (orientations)
S = Q * T + 1 # Total number of histograms
D = S * H # Total size of descriptor vector

def ExtractDaisy(dataInput):
    """
    descs : array
        Grid of DAISY descriptors for the given image as an array
        dimensionality  (P, Q, R) where

            ``P = ceil((M - radius*2) / step)``
            ``Q = ceil((N - radius*2) / step)``
            ``R = (rings * histograms + 1) * orientations``

    descs_img : (M, N, 3) array (only if visualize==True)
        Visualization of the DAISY descriptors.
    :param dataInput:
    :return:
    """
    if isinstance(dataInput, np.ndarray):  # examinate input type
      img = dataInput.copy()
    else:
      img = scipy.misc.imread(dataInput, mode='RGB')
    image = color.rgb2gray(img)
    t_start_1 = time.clock()
    descs = daisy(image, step=E, radius=R, rings=Q, histograms=T, orientations=H)
    print('Time used: %r' % (time.clock() - t_start_1))
    t_start_2 = time.clock()
    descs, descs_img = daisy(image, step=E, radius=R, rings=Q, histograms=T, orientations=H, visualize=True)
    print('Time used: %r' % (time.clock() - t_start_2))
    plt.imshow(img)
    plt.figure()
    plt.imshow(descs_img)
    plt.show()

if __name__ == "__main__":
    ExtractDaisy('.\\images\\4.jpg')