# Para armazenar informações de um livro,
# Incluindo título, autor e ano de publicação. Imprima cada informação.

from typing import Dict, Any

livro: Dict [str, Any] = {

    "Título": "Harry Potter e a Pedra Filosofal",
    "Autor": "J.K. Rowling",
    "Ano de Publicação": 1997
}

lista_de_livros_usando_dict: dict = {
    "Livro 01": {
        "Título": "Harry Potter e a Pedra Filosofal",
        "Autor": "J.K. Rowling",
        "Ano de Publicação": 1997},

    "Livro 02": {
        "Título": "Harry Potter e a Câmara Secreta",
        "Autor": "J.K. Rowling",
        "Ano de Publicação": 1998},

}

print(lista_de_livros_usando_dict["Livro 02"]["Título"])
print(lista_de_livros_usando_dict["Livro 02"]["Autor"])
print(lista_de_livros_usando_dict["Livro 02"]["Ano de Publicação"])