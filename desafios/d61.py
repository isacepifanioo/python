print('Digite um números para')
num = int(input('Calcular seu fatorial: '))
c = num
f = 1
print('calculando {}! = '.format(c), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)