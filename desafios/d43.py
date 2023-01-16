a = int(input('primeiro valor: '))
b = int(input('segundo valor '))
c = int(input('terceiro valor '))
if a == b == c:
    print('Equilátero')
elif a == b or b == c or a == c:
    print('Isosceles')
else:
    print('Escaleno')
