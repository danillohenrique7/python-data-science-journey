import numpy as np

notas = np.array([
    [8, 7, 9],
    [6, 5, 7],
    [10, 9, 8],
    [7, 8, 6]
])

media_aluno = np.mean(notas,axis=1)
media_prova = np.mean(notas,axis=0)
maior_nota = np.max(notas)


print("-="*25)
print(f"A quantidade de dimensões é {notas.ndim}")
print("-="*25)
print(f"O formato da matriz é {notas.shape}")
print("-="*25)
print(f"A media dos alunos é de {media_aluno}")
print("-="*25)
print(f"A media das provas é de {media_prova}")
print("-="*25)
print(f"A Maior nota foi de {maior_nota}")