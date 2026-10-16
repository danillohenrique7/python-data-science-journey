import pandas as pd

df = pd.read_csv("vendas_brasil.csv",sep=";",decimal=",")

valor_ausente = df.isna().sum()

vendas_validas = df.dropna(subset=["quantidade","preco"]).copy()

vendas_validas["total"] = vendas_validas["quantidade"] * vendas_validas["preco"]

faturamento_vendas_validas = vendas_validas["total"].sum()

quantidade_descartado = len(df) - len(vendas_validas)

print("=-"*25)
print(vendas_validas)
print("=-"*25)
print(f"FATURAMENTO DAS VENDAS VALIDAS:\n{faturamento_vendas_validas:.2f}")
print("=-"*25)
print(f"QUANTIDADE DE RESGISTRO DESCARTADO:\n{quantidade_descartado}")

vendas_validas.to_csv("vendas_limpas.csv", index=False, sep=";",decimal=",")