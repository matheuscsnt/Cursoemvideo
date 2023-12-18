preco_produto = float(input('Qual o preço do produto: '))

desconto = preco_produto * 0.05

produto_desconto = preco_produto - desconto

print(f'Você ganhou um desconto de 5%! O produto sairá por apenas R${produto_desconto:.2f}.')
