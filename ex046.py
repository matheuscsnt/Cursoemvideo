total = float(input('Total das compras? R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista (dinheiro/cheque)
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
escolha = int(input('Qual é a melhor opção? '))

avista = total - (total * 0.1)
av_cartao = total - (total * 0.05)
cartao2x = total
cartao3x = total + (total * 0.2)

if escolha == 1:
    print(f'Sua compra é de R${total:.2f} e com desconto vai ficar R${avista:.2f}!')
elif escolha == 2:
    print(f'Sua compra é de R${total:.2f} e com desconto vai ficar R${av_cartao:.2f}!')
elif escolha == 3:
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x SEM JUROS de R${parcela} com o total de R${cartao2x:.2f}!')
elif escolha == 4:
    parcelas = int(input('Quantas parcelas? '))
    p1 = total / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${p1:.2f} COM JUROS.')
    print(f'Sua compra de R${total:.2f} vai custar R${cartao3x:.2f} no total.')
else:
    print('Opção inválida, por favor escolha outra.')
