import numpy as np
import pywt
import matplotlib.pyplot as plt

# dwt
x = np.linspace(-5,5,100)
y = np.sin(x)
(cA, cD) = pywt.dwt(y, "db1")

plt.subplot(311)
plt.plot(y)

plt.subplot(312)
plt.plot(cA)

plt.subplot(313)
plt.plot(cD)

plt.show()