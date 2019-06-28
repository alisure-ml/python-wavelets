import pywt
import numpy as np

"""
                            -------------------
                            |        |        |
                            | cA(LL) | cH(LH) |
                            |        |        |
(cA, (cH, cV, cD))  <--->   -------------------
                            |        |        |
                            | cV(HL) | cD(HH) |
                            |        |        |
                            -------------------
"""

# 2D Single level
data = np.ones((4, 4), dtype=np.float64)
print(data)
coeffs = pywt.dwt2(data, 'haar')  # decomposition
cA, (cH, cV, cD) = coeffs
print(cA)
print(cH)
print(cV)
print(cD)
rec = pywt.idwt2(coeffs, 'haar')  # reconstruction
print(rec)
print()


# 2D multilevel
coeffs = pywt.wavedec2(np.ones((4, 4)), 'db1')  # decomposition
print(len(coeffs)-1)
rec = pywt.waverec2(coeffs, 'db1')  # reconstruction
print(rec)
