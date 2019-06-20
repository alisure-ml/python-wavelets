import pywt

wavelet = pywt.ContinuousWavelet("gaus1")
print(wavelet)

psi, x = wavelet.wavefun(level=5)
print(psi)
print(x)
