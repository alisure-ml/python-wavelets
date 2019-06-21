import pywt
import cv2
import numpy as np

"""
+---------------+---------------+-------------------------------+
|               |               |                               |
|     c[0]      |  c[1]['da']   |                               |
|               |               |                               |
+---------------+---------------+           c[2]['da']          |
|               |               |                               |
| c[1]['ad']    |  c[1]['dd']   |                               |
|               |               |                               |
+---------------+---------------+ ------------------------------+
|                               |                               |
|                               |                               |
|                               |                               |
|          c[2]['ad']           |           c[2]['dd']          |
|                               |                               |
|                               |                               |
|                               |                               |
+-------------------------------+-------------------------------+
"""

cam = pywt.data.camera()
coeffs = pywt.wavedecn(cam, wavelet="db2", level=3)

# Concatenating all coefficients into a single n-d array
arr, coeff_slices = pywt.coeffs_to_array(coeffs)

# Splitting concatenated coefficient array back into its components
coeffs_from_arr = pywt.array_to_coeffs(arr, coeff_slices)

cam_recon = pywt.waverecn(coeffs_from_arr, wavelet='db2')

# Raveling coefficients to a 1D array
arr, coeff_slices, coeff_shapes = pywt.ravel_coeffs(coeffs)

# Unraveling coefficients from a 1D array
coeffs_from_arr = pywt.unravel_coeffs(arr, coeff_slices, coeff_shapes)

cam_recon2 = pywt.waverecn(coeffs_from_arr, wavelet='db2')

# Multilevel: n-d coefficient shapes
shapes = pywt.wavedecn_shapes((64, 32), 'db2', mode='periodization')

# Multilevel: Total size of all coefficients
size = pywt.wavedecn_size(shapes)
print(size)

print()

