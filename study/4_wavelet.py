import pywt

wavelet = pywt.Wavelet("db1")

print(wavelet)

wavelet = pywt.Wavelet("db2")
phi, psi, x = wavelet.wavefun(level=5)
print(phi)
print(psi)
print(x)

wavelet = pywt.Wavelet('bior3.5')
phi_d, psi_d, phi_r, psi_r, x = wavelet.wavefun(level=5)
print(phi_d)
print(psi_d)
print(phi_r)
print(psi_r)
print(x)