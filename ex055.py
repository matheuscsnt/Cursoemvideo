# primeiro fizemos o exercicio com o for, mas é possível fazer com o fatiamento de string.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = juntos[::-1]

'''inverso = ''
for letra in range(len(juntos) -1, -1, -1):
    inverso += juntos[letra]'''

print(f'O inverso de {juntos} é {inverso}.')
if juntos == inverso:
    print(f'Parabéns, essa frase é um palindromo.')
else:
    print(f'Essa frase NÃO é um palindromo.')
