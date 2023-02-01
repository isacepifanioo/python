c = prba = ''
print('-' * 40)
print('           LOJA SUPER BARATÃO')
print('-' * 40)
tots = totm = menor = cont = 0
while True:
    prot = str(input('Nome do Produtor: '))
    pre = float(input('Preço: R$'))
    cont += 1
    if cont == 1:
        prba = prot
        menor = pre
    else:
        if pre < menor:
            prba = prot
            menor = pre
    if pre >= 1000:
        totm += 1
    tots += pre
    c = str(input('Quer Continuar [S/N]')).upper()
    if c == 'N':
        break
print('----------- FIM DO PROGRAMA ------------')
print(f'O total da compra foi R${tots}')
print(f'Temos {totm} produtos custando mais de R$1000')
print(f'O produto mais barato foi {prba} que custa R${menor}')