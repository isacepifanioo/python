print('---Forme um Triangulo---')
a = int(input('digite um numero: '))
b = int(input('digite o segundo numero: '))
c = int(input('digite o terceiro numero: '))
if a + b > c and a + c > b and c + b > a:
    print('O valor {}, {}, {} podem forma um triangulo'.format(a, b, c))
else:
    print('O valor {}, {}, {} não podem forma um triangulo'.format(a, b, c))
