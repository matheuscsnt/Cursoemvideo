from random import choice
n0 = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
lista = [n0, n1, n2, n3, n4,n5]

escolhido = choice(lista)
num_escolhido = int(input('Tende adivinhar qual foi o número escolhido de 0 a 5: '))
if num_escolhido == escolhido:
    print(f'Parabéns, você acertou! O número escolhido pelo PC foi {escolhido}!')
else:
    print(f'Infelizmente você errou, o número escolhido foi {escolhido}. Tente novamente!')
