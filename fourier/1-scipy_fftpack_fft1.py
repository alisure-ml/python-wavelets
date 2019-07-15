"""
One dimensional discrete Fourier transforms
https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html#one-dimensional-discrete-fourier-transforms
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import blackman
from scipy.fftpack import fft, ifft

# 0
_x = np.asarray([1.0, 2.0, 1.0, -1.0, 1.5, -1.0])
print(_x)

# 1.快速傅里叶变换
x = _x
y = fft(x)
print(y)

# 2.快速傅里叶逆变换
y_i = ifft(y)
print(y_i)

# 3.Example
N = 600
T = 1.0 / 800.0
x = np.linspace(0.0, N * T, N)
y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)
yf = fft(y)
xf = np.linspace(0.0, 1.0 / (2.0 * T), N / 2)
plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
plt.grid()
# plt.show()

# 4.Example
w = blackman(N)
ywf = fft(y * w)
xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
plt.semilogy(xf[1:N // 2], 2.0 / N * np.abs(yf[1:N // 2]), '-b')
plt.semilogy(xf[1:N // 2], 2.0 / N * np.abs(ywf[1:N // 2]), '-r')
plt.legend(['FFT', 'FFT w. window'])
plt.grid()
# plt.show()

# 5.FFT sample frequency points
from scipy.fftpack import fftfreq
freq = fftfreq(8, d=0.125)
print(freq)
freq = fftfreq(8, d=0.5)
print(freq)
print()

# 6.irfft
from scipy.fftpack import rfft, irfft
x = _x
print(x)
x_fft = fft(x)
print(x_fft)
x_rfft = rfft(x)
print(x_rfft)
x_rfft_irfft = irfft(x_rfft)
print(x_rfft_irfft)
