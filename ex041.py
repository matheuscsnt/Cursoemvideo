from datetime import date

atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

print(f'Quemm nasceu em {nascimento} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem que se alistar imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem 18 anos, ainda faltam {saldo} anos para o alistamento.')
    ano = atual + saldo
    print(f'O seu alistamento será em {ano}.')
else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'O seu alistamento foi em {ano}.')