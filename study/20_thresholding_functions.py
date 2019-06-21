import numpy as np
import pywt

data = np.linspace(-3, 3, 9)
soft = pywt.threshold(data, 2, 'soft')
hard = pywt.threshold(data, 2, 'hard')
garrote = pywt.threshold(data, 2, 'garrote')
greater = pywt.threshold(data, 2, 'greater')
less = pywt.threshold(data, 2, 'less')

print(data)
print(soft)
print(hard)
print(garrote)
print(greater)
print(less)
