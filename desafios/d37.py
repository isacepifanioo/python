print('-=-' * 16)
casa = float(input('Qual e o valor da casa? '))
salario = float(input('Quanto você recebe mensalmente? '))
ano = float(input('Quantos anos você que financiar a casa? '))
print('-=-' * 16)
mes = (casa / ano) / 12
po30 = (salario * 30) / 100
if mes >= po30:
    print('\033[31mNão foi possivel, pois o valor que você tem que paga ao banco tira 30% do seu salario\033[m')
else:
    print('Parabens você conseguiu um emprestimo do banco de R${}'
          '\nVocê tera que paga um valor de {} todos o mes durante {} anos'.format(casa, mes, ano))
    