import pywt
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# 数据
data = [1, 1, 1, 1, 2, 2, 3, 3]

# Haar小波
# haar = pywt.Wavelet(name="haar")  # 规范化小波
haar = pywt.Wavelet(name="haar", filter_bank=((1, 1), (-1, 1), (1, 1), (1, -1)))  # 未规范化小波

# （1级）1D离散小波变换
cA1, cD1 = pywt.dwt(data, haar)
print(cA1)
print(cD1)

# 1级1D离散小波变换
result = pywt.wavedec(data, wavelet=haar, level=1)
print(result)

# 2级1D离散小波变换
result = pywt.wavedec(data, wavelet=haar, level=2)
print(result)

# 3级1D离散小波变换
result = pywt.wavedec(data, wavelet=haar, level=3)
print(result)

print()
print()


# data_2 = [[1, 1, 2, 2],
#           [1, 1, 2, 2],
#           [2, 2, 1, 1],
#           [2, 2, 1, 1]]
data_2 = [[1, 2, 3, 4],
          [1, 2, 3, 4]]
cA, (cH, cV, cD) = pywt.dwt2(data_2, haar)
"""++（水平低通，垂直低通）
--> [1+2, 3+4]
--> [1+2, 3+4] ==> [3+3, 7+7] ==> [6, 14]
"""
print(cA)

"""+-（水平低通，垂直高通）
--> [1+2, 3+4]
--> [1+2, 3+4] ==> [3-3,7-7] ==> [0, 0]
"""
print(cH)

"""-+（水平高通，垂直低通）
--> [1-2, 3-4]
--> [1-2, 3-4] ==> [-1+-1,-1+-1] ==> [-2, -2]
"""
print(cV)

"""--（水平高通，垂直高通）
--> [1-2, 3-4]
--> [1-2, 3-4] ==> [-1--1,-1--1] ==> [0, 0]
"""
print(cD)

# 图片数据
data_camera = pywt.data.camera()
# 对2D数据进行离散小波变换
cA, (cH, cV, cD) = pywt.dwt2(data_camera, haar)

# 可视化
Image.fromarray(np.asarray(data_camera, dtype=np.uint8)).save("./3_haar_wavelet_camera.png")
# Image.fromarray(np.asarray(cA // (4 * 0.707), dtype=np.uint8)).save("./3_haar_wavelet_cA.png")
Image.fromarray(np.asarray(cA // 4, dtype=np.uint8)).save("./3_haar_wavelet_cA.png")
fig = plt.figure()
fig.suptitle("Haar wavelet", fontsize=14)
titles = ["cA", "cH", "cV", "cD"]
for i, a in enumerate([cA, cH, cV, cD]):
    ax = fig.add_subplot(2, 2, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([])
# fig.show()
fig.savefig("./3_haar_wavelet.png")

print()
