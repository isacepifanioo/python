print('-------------MERCADO-------------')
val = float(input('Qual o preço do produto? R$'))
print('O produto custa R${}'.format(val))
print('-----------------------------------------------------')
print('                 FORMA DE PAGAMENTO')
print('[Opção 1]: A vista Dinheiro/cheque: 10% de desconto')
print('[Opção 2]: A vista no cartão: 5% de desconto')
print('[Opção 3]: Em até 2x no cartão: preço normal')
print('[Opção 4]: 3x ou mais no cartão: 20% de juros')
opcao = int(input('Qual das opção acima você deseja paga seu produto? '))
print('-----------------------------------------------------')
if opcao == 1:
    desc = (val * 10) / 100
    valt = val - desc
    print('Bela escolha. valor do produtor vai custa R${}'.format(valt))
elif opcao == 2:
    desc = (val * 5) / 100
    valt = val - desc
    print('Bela escolha. O valor do produtor vai custa R${}'.format(valt))
elif opcao == 3:
    parc = val / 2
    print('Você vai paga 2 parcelas de R${}'.format(parc))
elif opcao == 4:
    juros = (val * 20) / 100
    valt = val + juros
    print('O valor total do produtor vai custa R${}'.format(valt))