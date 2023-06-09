class Programa:
    def __init__(self,nome,ano) :
        self._nome = nome.title()
        self.ano =ano

        self._likes = 0

    def __str__(self):
        return(f'Nome: {self.nome}  Likes: {self.likes}')
    
    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,novo_nome):
      self.__nome = novo_nome.title()
    



class Filme(Programa):
    def __init__(self,nome,ano,duracao) :
        super().__init__(nome,ano)
        self.duracao = duracao
        
    def __str__(self):
        return(f'Nome: {self.nome} - Likes: {self.likes}')
    
      


class Serie(Programa):
    def __init__(self,nome,ano,temporada) :
        super().__init__(nome,ano)
        self.temporada = temporada

    def __str__(self):
        return(f'Nome: {self.nome} - Likes: {self.likes}')
        

   

vingadores = Filme('vingadores-guerra infinita',2018, 160 )
lost = Serie('Lost', 2008,4)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

lost.dar_like()
lost.dar_like()

filmes_e_series = [vingadores,lost]


for programa in filmes_e_series:
   print(programa)