soma = 0
cont = 0
for contagem in range(1, 501, 2):
    if contagem % 3 == 0:
        soma = soma + contagem
        cont = cont + 1
print(f'A soma de todos os {cont} valores solicitados é igual a {soma}.')
