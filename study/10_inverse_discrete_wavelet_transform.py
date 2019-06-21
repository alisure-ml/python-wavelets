import pywt
import numpy as np


# Inverse Discrete Wavelet Transform (IDWT): Single level
cA, cD = pywt.dwt([1, 2, 3, 4, 5, 6], 'db2', 'smooth')
rec = pywt.idwt(cA, cD, 'db2', 'smooth')
print(rec)
print()

(cA, cD) = pywt.dwt([1, 2, 3, 4, 5, 6], 'db1', 'smooth')
A = pywt.idwt(cA, None, 'db1', 'smooth')
print(A)
D = pywt.idwt(None, cD, 'db1', 'smooth')
print(D)
print(A + D)
print()


# Multilevel reconstruction
coeffs = pywt.wavedec([1, 2, 3, 4, 5, 6], 'db1', level=2)
cA2, cD2, cD1 = coeffs
print(cA2)
print(cD2)
print(cD1)
coeffs[-1] = np.zeros_like(coeffs[-1])
rec = pywt.waverec(coeffs, 'db1')
print(rec)
print()


# Direct reconstruction: Direct reconstruction from coefficients.
data = [1, 2, 3, 4, 5, 6]
cA, cD = pywt.dwt(data, 'db2', 'smooth')
rec = pywt.upcoef('a', cA, 'db2') + pywt.upcoef('d', cD, 'db2')
print(rec)
rec = pywt.upcoef('a', cA, 'db2', take=len(data)) + pywt.upcoef('d', cD, 'db2', take=len(data))
print(rec)
