altura_parede = float(input('Digite a altura da parede: '))
largura_parede = float(input('Digite a largura da parede: '))

area_parede = altura_parede * largura_parede

print(f'Essa parede possui {area_parede:.2f}m².')

litro_tinta = area_parede / 2
tinta_margem = litro_tinta + 0.5

print(f'Para pintar essa parede você vai precisar de {tinta_margem:.2f}l de tinta.')

# Cálculo de area para saber a quantidade de tinta necessária. Adicionei também uma margem de erro de 0.5 para mais.