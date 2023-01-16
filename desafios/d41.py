n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('sua media foi {} infelizmente você foi reprovado'.format(media))
elif media > 5.0 and media <= 6.9:
    print('sua nota foi {} você ficou de recuperação'.format(media))
else:
    print('sua media foi {} parabens você passou de ano!'.format(media))