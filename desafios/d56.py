for c in range(1, 6):
    peso = float(input('Digite o {}º peso: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior peso foi de {}kg'.format(maior))
print('Menor peso foi de {}kg'.format(menor))