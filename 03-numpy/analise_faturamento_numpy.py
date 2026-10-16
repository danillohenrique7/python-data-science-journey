import numpy as np

faturamento = np.array([
    [1200, 1500, 1800],
    [2000, np.nan, 2500],
    [900, 1100, 1300],
    [3000, 2800, np.nan]
])

print("-="*20)
print(f"ndim da matriz: {faturamento.ndim}")
print("-="*20)
print(f"shape da matriz: {faturamento.shape}")
print("-="*20)



faturamento_total_lojas = np.nansum(faturamento, axis=1)
media_faturamento_mes = np.nanmean(faturamento, axis=0)
maior_faturamento = np.nanmax(faturamento)
valor_ausente = np.sum(np.isnan(faturamento))
faturamento_individuais = faturamento[faturamento > 1500]
faturamento_mes_media = np.round(media_faturamento_mes,2)





print(f"FATURAMENTO TOTAL POR LOJAS\n{faturamento_total_lojas}")
print("-="*20)
print(f"MÉDIA TOTAL POR MÊS \n{faturamento_mes_media}")
print("-="*20)
print(f"O MAIOR FATURAMENTO REGISTRADO\n{maior_faturamento}")
print("-="*20)
print(f"QUANTIDADE DE VALORES AUSENTES\n{valor_ausente}")
print("-="*20)
print(f"VALORES DE FATURAMENTOS INDIVIDUAIS MAIORES QUE R$ 1500\n{faturamento_individuais}")

