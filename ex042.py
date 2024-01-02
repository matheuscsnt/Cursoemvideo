nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print(f'A média do aluno é {media:.1f}!')

if media < 5:
    print('O aluno está REPROVADO.')
elif media >=5 and media < 7:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('Parabéns! Você foi APROVADO!')