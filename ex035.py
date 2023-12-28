primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Degite o segundo valor: '))
terceiro = int(input('Digite o terceiro valor: '))
# If que verifica o menor número inserido.
menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro
# If que verifica o meior número inserido.
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
print(f'O menor valor digitado foi {menor}.')
print(f'O maior valor digitado foi {maior}.')