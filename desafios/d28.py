n = input('Qual seu nome? ')
d = n.split()
print('E um prazer te conhecer {}!'.format(n))
print('Seu primeiro nome e {}'.format(d[0]))
print('Seu ultimo nome e {}'.format(d[len(d) - 1]))