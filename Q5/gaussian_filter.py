import cv2
from PIL import Image
from scipy.signal import fftconvolve
from scipy.ndimage import gaussian_filter
import numpy as np


img = cv2.imread("Torgya - Arunachal Festival.jpg")

sigma = 3

# 1) Custom non-normalized Gaussian via explicit kernel
K = int(round(2 * np.pi * sigma))
if K % 2 == 0:
    K += 1

r = K // 2
x = np.arange(-r, r + 1)
y = np.arange(-r, r + 1)
X, Y = np.meshgrid(x, y)

# non-normalized Gaussian kernel
G = np.exp(-(X**2 + Y**2) / (2 * sigma**2))

b, g, r = cv2.split(img)
r = fftconvolve(r, G, mode='same')
g = fftconvolve(g, G, mode='same')
b = fftconvolve(b, G, mode='same')

res = cv2.merge([b, g, r])
res = np.clip(res, 0, 255).astype(np.uint8)
Image.fromarray(cv2.cvtColor(res, cv2.COLOR_BGR2RGB)).save("sigma_3_non_normalised1.jpg")

# 2) Normalized Gaussian using your G (correct normalization) ie total sum=1
G_norm = G / G.sum()

b, g, r = cv2.split(img)
r = fftconvolve(r, G_norm, mode='same')
g = fftconvolve(g, G_norm, mode='same')
b = fftconvolve(b, G_norm, mode='same')

res = cv2.merge([b, g, r])
res = np.clip(res, 0, 255).astype(np.uint8)
#print(res[:, :5, :])
Image.fromarray(cv2.cvtColor(res, cv2.COLOR_BGR2RGB)).save("sigma_3_normalised_sum.jpg")

# 3) normalising by dividing with matrix area 
G_norm = G / (K*K)

b, g, r = cv2.split(img)
r = fftconvolve(r, G_norm, mode='same')
g = fftconvolve(g, G_norm, mode='same')
b = fftconvolve(b, G_norm, mode='same')

res = cv2.merge([b, g, r])
res = np.clip(res, 0, 255).astype(np.uint8)
#print(res[:, :5, :])
Image.fromarray(cv2.cvtColor(res, cv2.COLOR_BGR2RGB)).save("sigma_3_normalised_area.jpg")
