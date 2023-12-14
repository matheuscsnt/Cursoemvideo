saldo_conta = float(input('Digite quanto você tem na carteira: '))

valor_dolar = 3.27
dol_possivel = saldo_conta / valor_dolar

print(f'Hoje o dolár está custando U${valor_dolar}, você pode comprar U${dol_possivel:.2f} doláres.')
