import pandas as pd

df = pd.read_csv("vendas.csv")
df["total"] = df["quantidade"] * df["preco"]
faturmento_geral = df["total"].sum()

print("=-"*25)
print(df)
print("=-"*25)
print(f"FATURAMENTO GERAL\n{faturmento_geral:.2f}")

df.to_csv("relatorio.csv",index=False)