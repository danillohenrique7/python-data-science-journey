import numpy as np

salarios = np.array([1800, 2500, 3200, 1500, 4100, 2800])

salarios_altos = salarios[salarios > 2500]

filtro = (salarios >= 1800) & (salarios <= 3200)

media_salarios_altos = np.mean(salarios_altos)

salarios_intermediarios = salarios[filtro]


print("-="*25)
print(f"Os Salarios altos acima de R$ 2500\n{salarios_altos}")
print("-="*25)
print(f"Salarios intermediarios entre R$ 1800 e R$ 3200 \n{salarios_intermediarios}")
print("-="*25)
media_salarios_altos = (np.round(media_salarios_altos, 2))
print(f"Media dos Salarios Altos {media_salarios_altos}")