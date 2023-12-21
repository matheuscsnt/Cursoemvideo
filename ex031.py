velocidade = float(input('Qual a velocidade do veículo? '))

if velocidade > 80.0:
    print(f'Você foi multado, pois estava a {velocidade}Km/h.')
else:
    print(f'Velocidade dentro do permitido. Passou a {velocidade}Km/h.')
# A multa vai custar 7$ por km/h a mais. Adicionarei essa parte no momento da correção.
