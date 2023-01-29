r = 1
numbp = 0
numbi = 0
while r != 0:
    r = int(input('Digite um numero: '))
    if r != 0:
        if r % 2 == 0:
            numbp += 1
        else:
            numbi += 1
print('Você digitou {} par e {} impa'.format(numbp, numbi))