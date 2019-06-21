"""
Stationary Wavelet Transform (SWT), also known as Undecimated wavelet transform or 
Algorithme à trous is a translation-invariance modification of the Discrete Wavelet Transform 
that does not decimate coefficients at every transformation level.
"""
import pywt

# Multilevel 1D
coeffs = pywt.swt([1, 2, 3, 4, 5, 6, 7, 8], wavelet="db2", level=2)
rec = pywt.iswt(coeffs, "db2")

# Multilevel 2D
cam = pywt.data.camera()
coeffs2 = pywt.swt2(data=cam, wavelet="db1", level=5)
rec2 = pywt.iswt2(coeffs2, "db1")

# Multilevel n-dimensional
coeffs3 = pywt.swtn([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 'db1', level=2)
rec3 = pywt.iswtn(coeffs3, 'db1')

print()
