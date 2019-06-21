"""
https://pywavelets.readthedocs.io/en/latest/ref/nd-dwt-and-idwt.html
"""

import pywt
import numpy as np


# nD Single level
data = np.ones((4, 4, 4, 4), dtype=np.float64)
print(data)
coeffs = pywt.dwtn(data, 'haar')  # decomposition: Single-level n-dimensional Discrete Wavelet Transform.
for key in coeffs.keys():
    print(coeffs[key])
rec = pywt.idwtn(coeffs, 'haar')  # reconstruction: Single-level n-dimensional Inverse Discrete Wavelet Transform.
print(rec)
print()


# nD Multi level
coeffs = pywt.wavedecn(np.ones((4, 4, 4, 4)), 'db1')  # decomposition
print(len(coeffs)-1)
for i in range(len(coeffs)):
    v = coeffs[i]
    if isinstance(v, np.ndarray):
        print(v)
    else:
        for key in v.keys():
            print(v[key])
        pass
    pass
rec = pywt.waverecn(coeffs, 'db1')  # reconstruction
print(rec)
