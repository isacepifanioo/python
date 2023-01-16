kg = float(input('Quantos kg você tem atualmente? '))
altura = float(input('Quando você tem de altura? '))
alm = altura ** 2
imc = kg / alm
if imc < 17:
    print('imc {:.1f} Você esta muito abaixo do peso'.format(imc))
elif imc > 17 and imc < 18.8:
    print('imc {:.1f} Você esta abaixo do peso'.format(imc))
elif imc > 18.5 and imc < 25:
    print('imc {:.1f} Pesso ideal'.format(imc))
elif imc > 25 and imc < 30:
    print('imc {:.1f} Você esta em sobrepeso'.format(imc))
elif imc > 30 and imc < 35:
    print('imc {:.1f} Você esta com obesidade'.format(imc))
elif imc > 35 and imc < 40:
    print('imc {:.1f} Você esta com obesidade severa'.format(imc))
else:
    print('imc {:.1f} Obesidade morbida. Você vai Morre'.format(imc))

