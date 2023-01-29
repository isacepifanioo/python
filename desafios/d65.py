res = 0
c = ''
d = 0
while c != '999':
    numb = int(input('Digite um numero [999 para parar]: '))
    if numb == 999:
        c = str(numb)
    else:
        res += numb
        d += 1
print('Você digitou {} numeros e a soma entre eles foi {}'.format(d, res))
