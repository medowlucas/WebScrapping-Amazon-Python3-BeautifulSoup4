class Livro:
    def __init__(self, id, obra, autor, stars, preco):
        self.id = id
        self.obra = obra
        self.autor = autor
        self.stars = stars
        self.preco = preco

    def __str__(self):
        formatedPreco = '{:.2f}'.format(round(self.preco, 2)).replace('.', ',') \
            if self.preco != '' else '----'
        formatedStars = '\u2605' * int(round(self.stars, 0)) if self.stars != '' else self.stars

        return "Livro {} : \n" \
               "   Obra: {}\n" \
               "   Autor: {}\n" \
               "   Stars: {} {}\n" \
               "   Preço: R$ {}\n"\
            .format(self.id, self.obra, self.autor, formatedStars, self.stars, formatedPreco)
