from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''ESCOLHA A SUA OPÇÃO:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

opcao = int(input('Qual a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO..')
sleep(1)

if opcao != 0 and opcao != 1 and opcao != 2:
    print('JOGADA INVÁLIDA, JOGUE NOVAMENTE.')
    quit()
else:
    print('-=' * 11)
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[opcao]}')
    print('-=' * 11)

if computador == 0:  # O computador jogou PEDRA
    if opcao == 0:
        print('Acontceu um EMPATE.')
    elif opcao == 1:
        print('O Jogador VENCEU.')
    elif opcao == 2:
        print('O Computador VENCEU.')
elif computador == 1:  # O computador jogou PAPEL
    if opcao == 0:
        print('O Computador VENCEU.')
    elif opcao == 1:
        print('Aconteceu um EMPATE.')
    elif opcao == 2:
        print('O Jogador VENCEU.')
elif computador == 2:  # O computador jogou TESOURA
    if opcao == 0:
        print('O Jogador VENCEU.')
    elif opcao == 1:
        print('O Computador VENCEU.')
    elif opcao == 2:
        print('Aconteceu um EMPATE.')
else:
    print('Escolha um numero entre 0 e 2.')
