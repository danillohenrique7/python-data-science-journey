import numpy as np

temperaturas = np.array([25, 28, np.nan, 30, 27, np.nan, 26])

posicao_ausente = np.isnan(temperaturas)
quantidade_ausentes = np.sum(posicao_ausente)
media = np.nanmean(temperaturas)
maior = np.nanmax(temperaturas)




print(f"POSIÇÃO DO VALORES AUSENTES\n{posicao_ausente}")
print("-="*20)
print(f"QUANTIDADE DE AUSENTES \n{quantidade_ausentes}")
print("-="*20)
print(f"MEDIA DE VALOR DAS TEMPERATURAS\n{media}")
print("-="*20)
print(f"MAIOR TEMPERATURA\n{maior}")