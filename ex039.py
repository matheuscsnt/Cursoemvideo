numero = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input('Digite a opção escolhida: '))

if escolha == 1:
    print(f'{numero} convertido para binário é igual a {bin(numero)[2:]}.')
elif escolha == 2:
    print(f'{numero} convertido para octal é igual a {oct(numero)[2:]}.')
elif escolha == 3:
    print(f'{numero} convertido para hexadecimal é igual a {hex(numero)[2:]}.')
else:
    print('Opção inválida, tente novamente.')
