s = '1'
while s != 'pare':
    s = str(input('Sexo [M/F]')).upper()
    if s == 'F' or s == 'M':
        print('Seu {} foi registrado com sucesso'.format(s))
        s = 'pare'
print('fim')