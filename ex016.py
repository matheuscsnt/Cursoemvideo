qnt_dias = int(input('Por quantos dias o carro ficou alugado? '))
km_percorrido = float(input('Quantos KMs foram percorridos? '))

valor_dia = qnt_dias * 60
valor_km = km_percorrido * 0.15

print(f'O total a pagar é de R${(valor_dia + valor_km):.2f}!')