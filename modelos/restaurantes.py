class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_pizaa = Restaurante()

restaurante_praca.nome = 'Restaurante da Praça'
restaurante_praca.categoria = 'Comida Mineira'
restaurante_praca.ativo = True

print(vars(restaurante_praca))

