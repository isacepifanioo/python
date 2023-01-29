itot = 0
ftot = 0
for c in range(1, 5):
    print('------ {} pessoa --------'.format(c))
    nome = str(input('Nome? '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]')).upper()
    itot += idade
    media = itot / 4
    if c == 1:
        nov = nome
        velhor = idade
    else:
        if velhor < idade:
            nov = nome
            velhor = idade
    if sexo == 'F' and idade <= 20:
        ftot += 1
print('media de todos e {}'.format(media))
print('A pessoa mais velho(a) tem {} anos e o nome e {}'.format(velhor, nov))
print('Ao todos são {} mulheres com menos de 20 anos'.format(ftot))