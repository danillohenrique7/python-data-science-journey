import numpy as np

quantidades = np.array([10, 20, 30, 40])

bonus = np.array([5,10,15,20])

total = bonus + quantidades

dobro = total * 2


print("-="*25)
print(f"Array Total\n{total}")
print("-="*25)
print(f"Array Dobro\n{dobro}")
print("-="*25)
print(total.shape)  