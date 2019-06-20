import pywt

wavelet = pywt.DiscreteContinuousWavelet('db1')
print(wavelet)

wavelet = pywt.DiscreteContinuousWavelet('gaus1')
print(wavelet)
