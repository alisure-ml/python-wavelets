"""
Two and n-dimensional discrete Fourier transforms
https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html#two-and-n-dimensional-discrete-fourier-transforms
"""
from scipy.fftpack import ifft2
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

N = 30
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex="col", sharey="row")

xf = np.zeros((N, N))
xf[0, 5] = 1
xf[0, N - 5] = 1

Z = ifft2(xf)
ax1.imshow(xf, cmap=cm.Reds)
ax4.imshow(np.real(Z), cmap=cm.gray)
xf = np.zeros((N, N))
xf[5, 0] = 1
xf[N - 5, 0] = 1

Z = ifft2(xf)
ax2.imshow(xf, cmap=cm.Reds)
ax5.imshow(np.real(Z), cmap=cm.gray)
xf = np.zeros((N, N))
xf[5, 10] = 1
xf[N - 5, N - 10] = 1

Z = ifft2(xf)
ax3.imshow(xf, cmap=cm.Reds)
ax6.imshow(np.real(Z), cmap=cm.gray)

plt.show()
