ini = int(input('Inicio'))
fim = int(input('Fim'))
raz = int(input('passo'))
for c in range(ini, fim, raz):
    print(c)
print('-=-' * 10)
print('As 10 ultimo termo')
for n in range(0, 10):
    print(c)
    c -= raz
print('-=-' * 10)
print('O primeiro termo e {}'.format(ini))
print('E a razão e {}'.format(raz))
print(c)