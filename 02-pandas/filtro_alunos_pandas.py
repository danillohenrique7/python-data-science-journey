import pandas as pd

alunos = [
    {"nome": "Ana", "idade": 18, "nota": 8.5},
    {"nome": "Carlos", "idade": 20, "nota": 7.0},
    {"nome": "Julia", "idade": 19, "nota": 9.2},
    {"nome": "Pedro", "idade": 21, "nota": 6.5}
]

df = pd.DataFrame(alunos)

de_maior = df[df["idade"]>18]
print(de_maior)