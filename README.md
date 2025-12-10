# Bit Plane Splicing

## Low Light Results
### Original  
<img src="low_original.png" width="350">

### Reconstructed (Bits 0–2)  
<img src="low_reconstructed.png" width="350">

### Difference  
<img src="low_difference.png" width="350">

---

## Bright Light Results
### Original  
<img src="bright_original.png" width="350">

### Reconstructed (Bits 0–2)  
<img src="bright_reconstructed.png" width="350">

### Difference  
<img src="bright_difference.png" width="350">

---

## Question
Take photos in low light and bright light, extract all bit-planes, reconstruct the image using only the three lowest bit-planes (bits 0, 1, 2), and compute the difference from the original.

---

## Explanation
The task is to take photos in low light and bright light, extract all bit-planes from each image, reconstruct the image using only the three lowest bit-planes (bits 0, 1, and 2), and then compute the difference between the reconstructed image and the original. Each pixel in a grayscale image is represented by 8 bits, and bit-plane slicing separates the image into these individually layered bits. When reconstructing using only the lowest three bits, the resulting image contains only the most basic structural information. The difference image highlights the finer details stored in the higher bit-planes (bits 3 to 7). Low-light images usually contain less high-bit detail, while bright-light images tend to show stronger differences because they contain more information in the higher bits.
