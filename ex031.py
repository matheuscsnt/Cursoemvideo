velocidade = float(input('Qual a velocidade do veículo? '))

if velocidade > 80.0:
    print(f'Você foi multado, pois estava a {velocidade}Km/h.')
    multa = (velocidade-80) * 7
    print(f'Você deve pagar uma multa no valor de R${multa:.2f}.')
print(f'Velocidade dentro do permitido. Passou a {velocidade}Km/h.')
# A multa vai custar 7$ por km/h a mais. Adicionarei essa parte no momento da correção.
# Testando a condição simples, nao utilizando o else.