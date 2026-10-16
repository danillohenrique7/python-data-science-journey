vendas = [
    {"produto": "Mouse", "quantidade": 10, "preco": 75},
    {"produto": "Teclado", "quantidade": 5, "preco": 150},
    {"produto": "Monitor", "quantidade": 3, "preco": 900},
    {"produto": "Webcam", "quantidade": 8, "preco": 200},
    {"produto": "Headset", "quantidade": 6, "preco": 250}
]

faturamento_geral = 0
soma = 0

for venda in vendas:
    venda["total"] = venda["quantidade"] * venda["preco"]
    faturamento_geral += venda["total"]
    soma += venda["quantidade"]
    print(f"O produto {venda["produto"]} vendeu um total de R$ {venda['total']:.2f}")

print("-="*26)
print(f"O faturamento Geral foi de R$ {faturamento_geral:.2f}")
print(f"A quantidade total vendida foi de {soma} unidades! ")

