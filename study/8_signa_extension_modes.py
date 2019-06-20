"""
https://pywavelets.readthedocs.io/en/latest/ref/signal-extension-modes.html
"""

import pywt

print(pywt.Modes.modes)

# Notice that you can use any of the following ways of passing wavelet and mode parameters
a, d = pywt.dwt([1, 2, 3, 4, 5, 6], 'db2', 'smooth')
print(a)
print(d)
a, d = pywt.dwt([1, 2, 3, 4, 5, 6], pywt.Wavelet('db2'), pywt.Modes.smooth)
print(a)
print(d)
