from time import sleep
numero = int(input('Digite um numero para ver sua tabuada: '))

for c in range(1, 11):
    print(f'{numero}x{c}= {numero * c}')
    sleep(0.25)
print('Fim!')