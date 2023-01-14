vel = int(input('Em que velocidade você esta dirigindo? '))
print('Você esta dirigindo a {}km/h'.format(vel))
if vel <= 80:
    print('Dirija sempre com cinto de segurança!')
else:
    din = (vel - 80) * 7
    print('Você foi multado! o valor da multa e de R${}'.format(din))