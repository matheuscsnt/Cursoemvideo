print('Olá! Seja bem vindo a Financeira Matheus.')
imovel = float(input('Quanto custa o imóvel do seu interesse? R$'))
salario = float(input('Quanto você recebe de salário? R$'))
mensal = int(input('Em quantas vezes você pretende pagar o imóvel? '))

prestacao = imovel / mensal

if prestacao > (salario * 0.3):
    print('Infelizmente o seu empréstimo foi negado, pois a parcela mensal é maior que 30% do seu salário.')
else:
    print('O seu empréstimo para a compra do imóvel foi aprovado!')
    print(f'Você pagará a sua casa em {mensal}x de R${prestacao:.2f}.')
    print('Parabéns pela conquista.')
