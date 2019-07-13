import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import blackman
from scipy.fftpack import fft, ifft

x = np.asarray([1.0, 2.0, 1.0, -1.0, 1.5, -1.0])
print(x)

y = fft(x)
print(y)

y_i = ifft(y)
print(y_i)

N = 600
T = 1.0 / 800.0
x = np.linspace(0.0, N * T, N)
y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)
yf = fft(y)
xf = np.linspace(0.0, 1.0 / (2.0 * T), N / 2)
plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
plt.grid()
plt.show()

w = blackman(N)
ywf = fft(y * w)
xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
plt.semilogy(xf[1:N // 2], 2.0 / N * np.abs(yf[1:N // 2]), '-b')
plt.semilogy(xf[1:N // 2], 2.0 / N * np.abs(ywf[1:N // 2]), '-r')
plt.legend(['FFT', 'FFT w. window'])
plt.grid()
plt.show()
