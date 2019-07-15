"""
Discrete Sine Transforms
https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html#discrete-sine-transforms
"""
import numpy as np
from scipy.fftpack import dst, idst

x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

idst_1_dst_1 = idst(dst(x, type=1), type=1)
print(idst_1_dst_1)

idst_2_dst_2 = idst(dst(x, type=2), type=2)
print(idst_2_dst_2)

idst_3_dst_3 = idst(dst(x, type=3), type=3)
print(idst_3_dst_3)

idst_2_norm_dst_2_norm = idst(dst(x, type=2, norm='ortho'), type=2, norm='ortho')
print(idst_2_norm_dst_2_norm)

idst_3_norm_dst_3_norm = idst(dst(x, type=3, norm='ortho'), type=3, norm='ortho')
print(idst_3_norm_dst_3_norm)
