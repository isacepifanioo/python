print('-=-' * 10)
ano = int(input('em que ano você nasceu? '))
idade = 2023 - ano
print('-=-' * 10)
if idade < 9:
    print('Mirin')
elif idade < 14:
    print('Infantil')
elif idade < 19:
    print('Junior')
elif idade < 20:
    print('senior')
else:
    print('Master')
print('-=-' * 10)