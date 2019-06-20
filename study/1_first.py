import pywt

cA, cD = pywt.dwt([1, 2, 3, 4], "db1")

print(cA)
print(cD)

