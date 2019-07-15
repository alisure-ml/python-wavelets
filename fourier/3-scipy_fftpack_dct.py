"""
DCT: Discrete Cosine Transforms
https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html#discrete-cosine-transforms
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct

x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
print(x)

# dct
dct_1 = dct(x, type=1)
print(dct_1)
dct_2 = dct(x, type=2)
print(dct_2)
dct_3 = dct(x, type=3)
print(dct_3)

# dct norm
dct_2_norm = dct(x, type=2, norm='ortho')
print(dct_2_norm)
dct_3_norm = dct(x, type=3, norm='ortho')
print(dct_3_norm)

# idct
dct_1_idct_1 = idct(dct_1, type=1)
print(dct_1_idct_1)
dct_2_idct_2 = idct(dct_2, type=2)
print(dct_2_idct_2)
dct_3_idct_3 = idct(dct_3, type=3)
print(dct_3_idct_3)

# idct norm
dct_2_norm_idct_2_norm = idct(dct_2_norm, type=2, norm='ortho')
print(dct_2_norm_idct_2_norm)
dct_3_norm_idct_3_norm = idct(dct_3_norm, type=3, norm='ortho')
print(dct_3_norm_idct_3_norm)

# dct norm dct norm
dct_2_norm_dct_2_norm = dct(dct_2_norm, type=2, norm='ortho')
print(dct_2_norm_dct_2_norm)
dct_3_norm_dct_3_norm = dct(dct_3_norm, type=3, norm='ortho')
print(dct_3_norm_dct_3_norm)

"""

"""

N = 100
t = np.linspace(0, 20, N)
x = np.exp(-t / 3) * np.cos(2 * t)

y = dct(x, norm='ortho')

window = np.zeros(N)
window[:20] = 1
yr = idct(y * window, norm='ortho')

loss_20 = sum(abs(x - yr) ** 2) / sum(abs(x) ** 2)
print(loss_20)

plt.plot(t, x, '-bx')
plt.plot(t, yr, 'ro')

window = np.zeros(N)
window[:15] = 1
yr = idct(y * window, norm='ortho')

loss_15 = sum(abs(x - yr) ** 2) / sum(abs(x) ** 2)
print(loss_15)

plt.plot(t, yr, 'g+')
plt.legend(['x', '$x_{20}$', '$x_{15}$'])
plt.grid()
plt.show()
