salario = float(input('Qual é o salário do funcionário? R$'))

if salario <= 1250:
    novo_salario = salario + (salario * 0.15)
else:
    novo_salario = salario + (salario * 0.10)

print(f'O salário era R${salario:.2f}, e agora passa a ser R${novo_salario:.2f}.')