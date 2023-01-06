import math
an = float(input('Qual e o valor do ângolo? '))
seno = math.sin(math.radians(an))
print('o valor do seno {:.2f}'.format(seno))
cos = math.cos(math.radians(an))
print('o valor do cosseno {:.2f}'.format(cos))
tag = math.tan(math.radians(an))
print('o valor do tangente {:.2f}'.format(tag))
