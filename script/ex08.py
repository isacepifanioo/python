n1 = int(input('Qual sua primeira nota? '))
n2 = int(input('E a segunda? '))
me = (n1 + n2) / 2
print('Sua media foi {:.0f}'.format(me))
if me > 6:
    print('Você foi aprovado')
else:
    print('Você foi reprovado')