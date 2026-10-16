vendas_diarias = [35, 48, 22, 61, 40]

if len(vendas_diarias)>0:
    maior = vendas_diarias[0]
    menor = vendas_diarias[0]
    for venda in vendas_diarias:
        if venda > maior:
            maior = venda

        if venda < menor:
            menor = venda

print(f"O maior valor é de {maior}")
print(f"O menor valor é igual a {menor}")    
