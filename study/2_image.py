import numpy as np
import matplotlib.pyplot as plt
import pywt
import pywt.data


# Load image
original = pywt.data.camera()

titles = ['Approximation', ' Horizontal detail', 'Vertical detail', 'Diagonal detail']

LL, (LH, HL, HH) = pywt.dwt2(original, 'bior1.3')

fig = plt.figure(figsize=(12, 3))
for i, a in enumerate([LL, LH, HL, HH]):
    ax = fig.add_subplot(1, 4, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
    ax.set_title(titles[i], fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])
    pass

fig.tight_layout()
plt.show()
