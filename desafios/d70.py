c = ''
tot18 = toth = totm = 0
while c != 'N':
    conf = ''
    print('-' * 30)
    print('    CADASTRE UMA PESSOA')
    print('-' * 30)
    id = int(input('Idade: '))
    if id >= 18:
        tot18 += 1
    while conf != 's':
        sx = str(input('Sexo [M/F] ')).upper()
        if sx == 'F' or sx == 'M':
            conf = 's'
        if sx == 'M':
            toth += 1
        if sx == 'F' and id < 20:
            totm += 1
    print('-' * 30)
    conf = ''
    while conf != 'S':
        c = str(input('Que continua [S/N]')).upper()
        if c == 'S' or c == 'N':
            conf = 'S'
        if c == 'N':
            print('======= FIM DO PROGRAMA =======')
print(f'Total de pessoa com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrado.')
print(f'E temos {totm} mulheres com menos de 20 anos')