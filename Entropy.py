import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import math

original = img.imread('Parrots-680x680.jpg')
cropped=img.imread('Cropped Image.jpg')
decompres=img.imread('Decompress Image Original.jpg')

def entropy(image):
    img_1d = image.reshape((1, -1))[0]
    hist, bins = np.histogram(img_1d, bins=8, range=(0, 7))
    probabilities = hist / np.sum(hist)
    entropy=0
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log2(1/prob)
    return entropy

print("Original Image Entropy: ",entropy(original))
print("Cropped Image Entropy: ",entropy(cropped))
print("Decompress Image Entropy: ",entropy(decompres))