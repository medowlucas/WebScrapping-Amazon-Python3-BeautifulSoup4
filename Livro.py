class Livro:
    def __init__(self, id, obra, autor, stars, preco):
        self.id = id
        self.obra = obra
        self.autor = autor
        self.stars = stars
        self.preco = preco

    def __str__(self):
        return "Livro {} : \n" \
               "   Obra: {}\n" \
               "   Autor: {}\n" \
               "   Stars: {}\n" \
               "   Preço: {}\n".format(self.id, self.obra, self.autor, self.stars, self.preco)
