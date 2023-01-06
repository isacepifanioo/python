co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adiacente: '))
val = (co ** 2 + ca ** 2) ** (1/2)
print('Valor da Hipotenusa e {:.2f}'.format(val))