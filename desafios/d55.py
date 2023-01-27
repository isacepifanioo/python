idadeM = 0
idadeMN = 0
for c in range(0, 7, 1):
    ano = int(input('digite um ano de nascimento: '))
    idade = 2023 - ano
    if idade >= 18:
        idadeM += 1
    else:
        idadeMN += 1
print('A quantidade de pessoa que atigiu a maior idade e {}'.format(idadeM))
print('E a menor idade e {}'.format(idadeMN))

