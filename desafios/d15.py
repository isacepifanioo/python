d = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
dia = d * 60
k = km * 0.15
r = dia + k
print('O total a pagar e R${}'.format(r))
