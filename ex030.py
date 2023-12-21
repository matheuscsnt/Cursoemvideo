from random import randint
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')

escolhido = randint(0,5)
# RANDINT sorteia um número. A principio tinha feito com choice.
num_escolhido = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
if num_escolhido == escolhido:
    print(f'Parabéns, você acertou! O número escolhido pelo PC foi {escolhido}!')
else:
    print(f'Infelizmente você errou, o número escolhido foi {escolhido}. Tente novamente!')
