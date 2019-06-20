import pywt, math


# 1
c = math.sqrt(2) / 2
dec_lo, dec_hi, rec_lo, rec_hi = [c, c], [-c, c], [c, c], [c, -c]
filter_bank = [dec_lo, dec_hi, rec_lo, rec_hi]
myWavelet = pywt.Wavelet(name="myWavelet", filter_bank=filter_bank)

# 2


class MyWavelet2Bank(object):

    @property
    def filter_bank(self):
        c = math.sqrt(2) / 2
        dec_lo, dec_hi, rec_lo, rec_hi = [c, c], [-c, c], [c, c], [c, -c]
        return [dec_lo, dec_hi, rec_lo, rec_hi]

    pass


filter_bank = MyWavelet2Bank()
myWavelet2 = pywt.Wavelet(name="myWavelet2", filter_bank=filter_bank)
