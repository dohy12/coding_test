# medianFilter

import numpy as np
from scipy import signal
from skimage import io
from matplotlib import pyplot as plt

def myConvolutionMedian(image, filter_size):    
    xImageShape = image.shape[1]
    yImageShape = image.shape[0]

    newImg = np.zeros(((yImageShape//filter_size),(xImageShape//filter_size)))
    
    for y_idx in range(image.shape[0]//filter_size):
        for x_idx in range(image.shape[1]//filter_size):
            tmp = []
            for k in range(filter_size):
                tmp += image[y_idx*filter_size+k][x_idx*filter_size:x_idx*filter_size+filter_size].tolist()            
            newImg[y_idx][x_idx] = sorted(tmp)[(filter_size*filter_size)//2]

    newImg = newImg.astype(np.uint8)
    return newImg

img  = io.imread('/content/cv-datasets/einstein.jpeg')[:,:,0]
img2 = myConvolutionMedian(img, 3)

fig, axs = plt.subplots(1,2,figsize=(8,4))
axs[0].imshow(img, cmap='gray')
axs[1].imshow(img2, cmap='gray')