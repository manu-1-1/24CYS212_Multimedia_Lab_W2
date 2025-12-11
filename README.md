# Q5 – Spatial Filtering (Box & Gaussian)

## Original Image
<img src="Q5/Torgya - Arunachal Festival.jpg" width="450">

---

## 5×5 Box Filter
### Normalized  
<img src="Q5/5.5_normlised.jpg" width="350">

### Non-Normalized  
<img src="Q5/5.5_non_normlised.jpg" width="350">

---

## 20×20 Box Filter
### Normalized  
<img src="Q5/20.20_normalised.jpg" width="350">

### Non-Normalized  
<img src="Q5/20.20_non_normalised.jpg" width="350">

---

## Gaussian Filter (σ = 3)
### Non-Normalized  
<img src="Q5/sigma_3_non_normalised1.jpg" width="350">

### Sum-Normalized Gaussian  
<img src="Q5/sigma_3_normalised_sum.jpg" width="350">

### Area-Normalized Gaussian  
<img src="Q5/sigma_3_normalised_area.jpg" width="350">

---

## **Question**
**Spatial Filtering:**  
Implement 5×5 and 20×20 box filters with and without normalization for  
*Torgya – Arunachal Festival.jpg*.  
Since this is a color image, filtering must be applied on all RGB channels.  
Compute σ, use it to determine filter size, and then apply a **separable Gaussian filter** and a **separable normalized Gaussian filter**.

---

## **Explanation**
A box filter replaces each pixel with the sum or average of neighboring pixels inside an N×N window.  
A **normalized** box filter divides by the window area, preserving brightness.  
A **non-normalized** filter sums raw values, causing the output to brighten significantly.  
A 20×20 filter blurs much more than a 5×5 because it covers a larger neighborhood.

A Gaussian filter uses weights that decrease with distance from the center.  
If not normalized, its kernel sum exceeds 1 and the image becomes brighter.  
Normalizing by the kernel sum preserves proper brightness.  
Gaussian filters blur more smoothly and preserve edges better than box filters.  
A separable Gaussian splits the filter into horizontal + vertical passes, making it faster.

---

# Q6 – Bit-Plane Slicing

## Low-Light Image Results

### Original  
<img src="Q6/low_original.png" width="350">

### Reconstructed (Bits 0–2)  
<img src="Q6/low_reconstructed.png" width="350">

### Difference  
<img src="Q6/low_difference.png" width="350">

---

## Bright-Light Image Results

### Original  
<img src="Q6/bright_original.png" width="350">

### Reconstructed (Bits 0–2)  
<img src="Q6/bright_reconstructed.png" width="350">

### Difference  
<img src="Q6/bright_difference.png" width="350">

---

## **Question**
Take photos in low light and bright light.  
Extract all bit-planes, reconstruct the image using only the three lowest bit-planes (bits 0, 1, 2), and compute the difference between the reconstructed image and the original.

---

## **Explanation**
Each pixel is stored using 8 bits (bit 0 = least significant, bit 7 = most significant).  
Bit-plane slicing separates these into 8 layers.  
Reconstructing with only bits **0–2** retains only coarse structure and removes high-detail information.  
The **difference image** shows the details lost in higher bit-planes (bits 3–7).  
Low-light images usually contain weaker high-bit detail, while bright images show stronger, clearer differences.

---

## **Reference Scripts**
- `boxfilter.py`
- `gaussian_filter.py`
- `bit_slicing.py`
