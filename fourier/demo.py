import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 显示负号

"""
1111111111111111111111111111111
"""
# 采样点选择1400个，因为设置的信号频率分量最高为600赫兹，
# 根据采样定理知采样频率要大于信号频率2倍，所以这里设置采样频率为1400赫兹（即一秒内有1400个采样点，一样意思的）
x = np.linspace(0, 1, 1400)

# 设置需要采样的信号，频率分量有200，400和600
y = 7 * np.sin(2 * np.pi * 200 * x) + 5 * np.sin(2 * np.pi * 400 * x) + 3 * np.sin(2 * np.pi * 600 * x)

plt.figure()
plt.plot(x, y)
plt.title('原始波形')

plt.figure()
n = 50
plt.plot(x[0:n], y[0:n])
plt.title('原始部分波形（前50组样本）')
plt.show()

"""
22222222222222222222222222
"""

fft_y = fftpack.fft(y)
print(len(fft_y))
print(fft_y[0:5])

"""
33333333333333333333333333333
"""
N = 1400
x = np.arange(N)  # 频率个数

abs_y = np.abs(fft_y)  # 取复数的绝对值，即复数的模(双边频谱)
angle_y = np.angle(fft_y)  # 取复数的角度

plt.figure()
plt.plot(x, abs_y)
plt.title('双边振幅谱（未归一化）')

plt.figure()
plt.plot(x, angle_y)
plt.title('双边相位谱（未归一化）')
plt.show()

"""
444444444444444444444444444
"""
normalization_y = abs_y / N  # 归一化处理（双边频谱）
plt.figure()
plt.plot(x, normalization_y, 'g')
plt.title('双边频谱(归一化)', fontsize=9, color='green')
plt.show()

"""
55555555555555555555555555555
"""

half_x = x[range(int(N / 2))]  # 取一半区间
normalization_half_y = normalization_y[range(int(N / 2))]  # 由于对称性，只取一半区间（单边频谱）
plt.figure()
plt.plot(half_x, normalization_half_y, 'b')
plt.title('单边频谱(归一化)', fontsize=9, color='blue')
plt.show()
