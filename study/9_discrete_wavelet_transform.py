import pywt


# Single level
cA1, cD1 = pywt.dwt([1, 2, 3, 4, 3, 2, 1], "db1")
print(cA1)
print(cD1)
rec = pywt.idwt(cA1, cD1, "db1")
print(rec)
print()


# Multilevel decomposition using
from pywt import wavedec
cA2, cD2, cD1 = wavedec([1, 2, 3, 4, 3, 2, 1], "db1", level=2)
print(cA2)
print(cD2)
print(cD1)
print()


# Partial Discrete Wavelet Transform data decomposition
# Similar to pywt.dwt, but computes only one set of coefficients.
# Useful when you need only approximation or only details at the given level.
coeffs = pywt.downcoef(part="a", data=[1, 2, 3, 4, 3, 2, 1], wavelet="db1", level=2)
print(coeffs)
print()


# Maximum decomposition level
w = pywt.Wavelet("sym5")
l = pywt.dwt_max_level(data_len=1000, filter_len=w.dec_len)
print(l)
l = pywt.dwt_max_level(data_len=1000, filter_len=w)
print(l)
print()


# Result coefficients length
l = pywt.dwt_coeff_len(data_len=1000, filter_len=w, mode="per")
print(l)
