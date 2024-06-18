class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    
    def __str__(self):
        return f'{self.nome} - {self.artista} - {self.duracao}'
    
    def listar_musicas():
        for m in Musica.musicas:
            print(f'{m.nome} - {m.artista} - {m.duracao}')

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

Musica.listar_musicas()