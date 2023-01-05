ba = input('O que você pretende pinta? ')
la = float(input('qual é a largura da {} que você que pintar? '.format(ba)))
al = float(input('E a altura? '))
print('A {} tem uma largura de {}m² é {}m² de altura'.format(ba, la, al))
res = la * al
co = res / 2
print('O balde de tinta pinta 2m², então para pinta a sua {} você precisa de {}l de pintas'.format(ba, co))