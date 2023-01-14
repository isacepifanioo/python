sal = float(input('Digite seu salario: '))
if sal >= 1250:
    cen = (sal * 10) / 100
    aum = sal + cen
    print('Parabens seu salario teve um aumento de 10%. seu novo salario e de R${}'.format(aum))
else:
    cen = (sal * 15) / 100
    aum = sal + cen
    print('Parabens seu salario teve um aumento de 15%. seu novo salario e de R${}'.format(aum))
