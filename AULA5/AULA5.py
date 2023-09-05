class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.editora = 'editora bunda'

    def identidade(self):
        return (f'Sou o livro {self.nome}, e estou salvo'
                f'no endereço de memoria: {id(self)}')


if __name__ == '__main__':
    livro_1 = Livro('Super Aprendizado', 'Daniel Bundinha')
    livro_2 = Livro('Senhor do Zoio de Porco', 'Picantro Avantajeni')

    print('livro 1 :', vars(livro_1))
    print(livro_1.nome)
    print(livro_1.autor)
# print('livro 2 :', vars(livro_2))
