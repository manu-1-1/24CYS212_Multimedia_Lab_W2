import cv2
import numpy as np
from scipy.signal import fftconvolve
from PIL import Image
img=cv2.imread("Torgya - Arunachal Festival.jpg")

#box filter 5*5 normalised
b,g,r=cv2.split(img)
kernel5=np.ones((5, 5))
kernel5n=(1/25)*kernel5
rb=fftconvolve(b,kernel5n,mode='same')
rg=fftconvolve(g,kernel5n,mode='same')
rr=fftconvolve(r,kernel5n,mode='same')
res=cv2.merge([rb,rg,rr])
res = np.clip(res, 0, 255).astype(np.uint8)
res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
res=Image.fromarray(res)
res.save("5.5_normlised.jpg")

#box filter 5*5 non normalised
rb=fftconvolve(b,kernel5,mode='same')
rg=fftconvolve(g,kernel5,mode='same')
rr=fftconvolve(r,kernel5,mode='same')
res=cv2.merge([rb,rg,rr])
res = np.clip(res, 0, 255).astype(np.uint8)
res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
res=Image.fromarray(res)
res.save("5.5_non_normlised.jpg")


#box filter 20*20 normalised
b,g,r=cv2.split(img)
kernel20=np.ones((20, 20))
kernel20n=(1/400)*kernel20
rb=fftconvolve(b,kernel20n,mode='same')
rg=fftconvolve(g,kernel20n,mode='same')
rr=fftconvolve(r,kernel20n,mode='same')
res=cv2.merge([rb,rg,rr])
res = np.clip(res, 0, 255).astype(np.uint8)
res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
res=Image.fromarray(res)
res.save("20.20_normalised.jpg")

#box filter 20*20 non normalised
rb=fftconvolve(b,kernel20,mode='same')
rg=fftconvolve(g,kernel20,mode='same')
rr=fftconvolve(r,kernel20,mode='same')
res=cv2.merge([rb,rg,rr])
res = np.clip(res, 0, 255).astype(np.uint8)
res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
res=Image.fromarray(res)
res.save("20.20_non_normalised.jpg")
