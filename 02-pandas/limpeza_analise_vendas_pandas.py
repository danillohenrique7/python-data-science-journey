import pandas as pd

vendas = [
    {"produto": "Mouse", "quantidade": 10, "preco": 75},
    {"produto": "Teclado", "quantidade": 5, "preco": 150},
    {"produto": "Monitor", "quantidade": 3, "preco": None},
    {"produto": "Webcam", "quantidade": None, "preco": 200},
    {"produto": "Headset", "quantidade": 6, "preco": 250},
    {"produto": "Mousepad", "quantidade": 12, "preco": 30}
]

df = pd.DataFrame(vendas)

valor_ausente = df.isna().sum()

vendas_validas = df.dropna(subset=["quantidade","preco"]).copy()
vendas_validas["total"] = vendas_validas["quantidade"] * vendas_validas["preco"]
faturamento_total = vendas_validas['total'].sum()
valor_medio = vendas_validas['total'].mean()

quantidade_descartado = len(df) - len(vendas_validas)

print(vendas_validas)
print(f"\n{quantidade_descartado} resgitro foram descartado\n")
print(f"O faturamento total foi de R$ {faturamento_total:.2f}")
print(f"O valor medio foi de R$ {valor_medio:.2f}")

