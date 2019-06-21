import pywt
import numpy as np
import matplotlib.pyplot as plt

# 1
x = np.arange(512)
y = np.sin(np.pi * x / 16)
coef, freqs = pywt.cwt(y, np.arange(1, 129), 'gaus1')
plt.matshow(coef)  # doctest: +SKIP
plt.show()  # doctest: +SKIP

# 2
t = np.linspace(-1, 1, 200, endpoint=False)
sig = np.cos(2 * np.pi * 7 * t) + np.real(np.exp(-7 * (t - 0.4) ** 2) * np.exp(1j * 2 * np.pi * 2 * (t - 0.4)))
widths = np.arange(1, 31)
cwtmatr, freqs = pywt.cwt(sig, widths, 'mexh')
plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',
           vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())  # doctest: +SKIP
plt.show()  # doctest: +SKIP

# 3
# A variety of continuous wavelets have been implemented.
wavlist = pywt.wavelist(kind='continuous')
print(wavlist)
