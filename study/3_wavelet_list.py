import pywt

"""
Currently the built-in families are:
    * Haar (``haar``)
    * Daubechies (``db``)
    * Symlets (``sym``)
    * Coiflets (``coif``)
    * Biorthogonal (``bior``)
    * Reverse biorthogonal (``rbio``)
    * `"Discrete"` FIR approximation of Meyer wavelet (``dmey``)
    * Gaussian wavelets (``gaus``)
    * Mexican hat wavelet (``mexh``)
    * Morlet wavelet (``morl``)
    * Complex Gaussian wavelets (``cgau``)
    * Shannon wavelets (``shan``)
    * Frequency B-Spline wavelets (``fbsp``)
    * Complex Morlet wavelets (``cmor``)
"""


# 得到支持的小波
wavelet_list = pywt.families()
wavelet_list_long = pywt.families(short=False)

print(wavelet_list)
print(wavelet_list_long)


# 得到所有可利用的小波
wave_haar = pywt.wavelist(family="haar")
print(wave_haar)
wave_coif = pywt.wavelist(family="coif")
print(wave_coif)
wave_continuous = pywt.wavelist(kind="continuous")
print(wave_continuous)




