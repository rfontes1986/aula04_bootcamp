produto_01: dict = {
    "nome": "Sapato",
    "quantidade": 39,
    "preço": 10.38,
    "disponibilidade": True
}

produto_02: dict = {
    "nome": "televisão",
    "quantidade": 5,
    "preço": 1500.00,
    "disponibilidade": False
}

carrinho: list = []
carrinho.append(produto_01)
carrinho.append(produto_02)

print(carrinho)