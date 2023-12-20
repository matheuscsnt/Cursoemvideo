nomecompleto = str(input('Digite seu nome completo: ')).strip()

nome = nomecompleto.split()
print('Muito prazer em te conhecer!')
print(f'O seu primeiro nome é: {nome[0]}.')
print(f'O seu último nome é: {nome[len(nome) - 1]}.')
