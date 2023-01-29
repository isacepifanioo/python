print('-=' * 10)
print('   GERADOR DE PA')
print('-=' * 10)
t = int(input('Primeiro termos: '))
r = int(input('Razão da Pa: '))
c = 1
while c != 11:
    print('{} - '.format(t), end='')
    t += r
    c += 1
print('Fim')