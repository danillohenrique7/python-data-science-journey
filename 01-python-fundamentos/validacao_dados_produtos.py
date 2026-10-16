produtos = [
    {"nome": "Notebook", "quantidade": 3, "preco": 2500},
    {"nome": "Mouse", "quantidade": -4, "preco": 80},
    {"nome": "Teclado", "quantidade": 5, "preco": None},
    {"nome": "Monitor", "quantidade": "dois", "preco": 900},
    {"nome": "Webcam", "quantidade": 2, "preco": 150}
]
def produtos_nulos():
    for produto in produtos:
        if produto["preco"] == None:
            print(f"OS produtos que estão com os valores nulos são os {produto["nome"]}")


def quantidades_negativos():
    for produto in produtos:
        if isinstance(produto.get("quantidade"), int) and produto["quantidade"] < 0:
            print(f"{produto['nome']} tem {produto['quantidade']} quantidade negativas")

def indentificar_produtos_invalidos():
    for produto in produtos:
        quantidade = produto.get("quantidade")

        if not isinstance(quantidade,int):
            print(f"O produto {produto.get("nome")}; possivel a quantidade em string {quantidade} ")





produtos_nulos()
quantidades_negativos()
indentificar_produtos_invalidos()



