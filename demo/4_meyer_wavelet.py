"""
Meyer小波
"""
import pywt
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 数据
data = [1, 1, 1, 1, 2, 2, 3, 3]

# 获取Meyer小波
wave_meyer = pywt.Wavelet(name="dmey")

# （1级）1D离散小波变换
cA1, cD1 = pywt.dwt(data, wave_meyer)
print(cA1)
print(cD1)


# 图片数据
data_camera = pywt.data.camera()
# 对2D数据进行离散小波变换
cA, (cH, cV, cD) = pywt.dwt2(data_camera, wave_meyer)

# 可视化
Image.fromarray(np.asarray(data_camera, dtype=np.uint8)).save("./4_meyer_wavelet_camera.png")
# Image.fromarray(np.asarray(cA // (4 * 0.707), dtype=np.uint8)).save("./4_meyer_wavelet_cA.png")
Image.fromarray(np.asarray(cA // 4, dtype=np.uint8)).save("./4_meyer_wavelet_cA.png")
fig = plt.figure()
fig.suptitle("Meyer wavelet", fontsize=14)
titles = ["cA", "cH", "cV", "cD"]
for i, a in enumerate([cA, cH, cV, cD]):
    ax = fig.add_subplot(2, 2, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([])
# fig.show()
fig.savefig("./4_meyer_wavelet.png")

print()
