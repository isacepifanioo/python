data = int(input('Escreva o ano que você nasceu: '))
idade = 2023 - data
if idade <= 17:
    dm = 18 - idade
    print('Você não pode se alistar ainda, falta {} anos'.format(dm))
elif idade == 18:
    print('Ja estar na hora de se alistar para o exercito brasileiro!!')
else:
    dma = idade - 18
    print('Você ja ultrapassou um tempo de {} anos, preocure se alista mais rapido possivel'.format(dma))
