import pandas as pd

funcionarios = [
    {"nome": "Ana", "idade": 25, "salario": 3000},
    {"nome": "Carlos", "idade": None, "salario": 4000},
    {"nome": "Julia", "idade": 28, "salario": None},
    {"nome": "Pedro", "idade": 32, "salario": 5000},
    {"nome": "Mariana", "idade": None, "salario": None}
]

df = pd.DataFrame(funcionarios)

valor_ausente = df.isna().sum()
func_dado_ausente = df[df.isna().any(axis=1)]
registro_incompleto = len(func_dado_ausente)


print(f"{valor_ausente}\n")
print(f"{func_dado_ausente}\n")
print(f"O total de registros incompleto é de {registro_incompleto}")