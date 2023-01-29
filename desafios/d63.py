print('-=' * 10)
print('   GERADOR DE PA')
print('-=' * 10)
t = int(input('Primeiro termos: '))
r = int(input('Razão da Pa: '))
c = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} - '.format(t), end='')
        t += r
        c += 1
    print('pausa')
    mais = int(input('Quantos termos você que mostrar a mais? '))
c -= 1
print('progressão finalizada com {} termos mostrado'.format(c))
print('fim')