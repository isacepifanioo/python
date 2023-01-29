r = 'S'
tot = 0
soma = 0
maior = 0
while r != 'N':
    n1 = int(input('Digite um numero: '))
    r = str(input('Que continuar? [S/N] ')).upper()
    tot += 1
    soma += n1
    media = soma / tot
    if tot == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
print('Você digitou {} números e a média foi {:.2f}'.format(tot, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
