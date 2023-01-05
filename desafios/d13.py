sa = float(input('Qual e o salario do funcionario? R$'))
c1 = sa * 15
c2 = c1 / 100
c3 = sa + c2
print('O salario do funcionario e R${} com com aumento de 15% ele ficou por R${:.2f}'.format(sa, c3))