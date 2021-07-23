class Programa: # Classe mãe
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes
    
    def dar_like(self):
        self._likes += 1
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    def __str__(self): # Define como a classe se comporta em str
        return f'Nome: {self._nome} Likes: {self._likes}'

class Filme(Programa): # class Filho(Mae)
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # super() -> Referencia a classe mãe
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} | Duração: {self.duracao} | Likes: {self.likes}'    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'Nome: {self.nome} | Temporadas: {self.temporadas} | Likes: {self.likes}'

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self, item): # Torna o objeto iterável
        return self._programas[item]
    
    def __len__(self): # Define o resultado para um len(objeto)
        return len(self._programas)

# Objetos

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

playlist = [vingadores, atlanta, tmep, demolidor]
pl_fim_de_semana = Playlist("Final de Semana", playlist)

# Likes

for i in range(0, 3):
    vingadores.dar_like()

for i in range(0, 2):
    atlanta.dar_like()

for i in range(0, 4):
    tmep.dar_like()

for i in range(0, 5):
    demolidor.dar_like()

# Output

print(f"A Playlist {pl_fim_de_semana.nome} contém {len(pl_fim_de_semana)} programas")

for programa in pl_fim_de_semana:
    print(programa)