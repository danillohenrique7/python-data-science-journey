import pandas as pd 

df = pd.read_excel("laboratorio_excel_vendas.xlsx",sheet_name="Vendas")

valores_ausentes = df.isna().sum()

vendas_validas = df.dropna(subset=["Quantidade","Preco_Unitario"])

vendas_validas["Total"] = vendas_validas["Quantidade"] * vendas_validas["Preco_Unitario"]
 
faturamento_vendas_validas = vendas_validas["Total"].sum()

registro_descartado = len(df) - len(vendas_validas)


print("-="*29)
print(vendas_validas)
print("-="*29)
print(f"FATURAMENTO DAS VENDAS VALIDAS\n{faturamento_vendas_validas}")
print("-="*29)
print(f"QUANTIDADE DE REGISTRO DESCARTADOS: {registro_descartado}")
print("-"*29)
print(f"COLUNAS DE VALORES AUSENTES\n{valores_ausentes}")

vendas_validas.to_excel("relatorio_vendas.xlsx",index=False)