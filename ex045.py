peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)

print(f'O seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('Parabéns! Você está no peso IDEAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está OBESO, vamos se cuidar.')
else:
    print('Você já está na faixa da OBESIDADE MÓRBIDA.')