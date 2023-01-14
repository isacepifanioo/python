ddp = float(input('Quantos km você deseja ir?'))
res1 = ddp * 0.50
if ddp <= 200:
    print('O valor da passagem e de R${}'.format(res1))
else:
    res2 = ddp * 0.45
    print('O valor da passagem e de R${}'.format(res2))
    print('Passagem que leva a mais de 200km, ganha 10% de desconto')
