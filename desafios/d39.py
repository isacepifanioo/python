a = int(input('\033[32mescolha um numero: \033[m'))
b = int(input('\033[33mescolha um segundo numero: \033[m'))
if a > b or b < a:
    print('\033[32mO primeiro valor e maior\033[m')
elif b > a or a < b:
    print('\033[33mO segundo valor e maior\033[m')
else:
    print('\033[4;29mO valor e igual\033[m')