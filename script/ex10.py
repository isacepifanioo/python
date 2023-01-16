nome = str(input('Qual seu nome? '))
if nome == 'isac':
    print('\033[1;36mQue nome daora\033[1;36m')
elif nome in 'ana maria joao lucas':
    print('\033[1;33mSeu nome e bem popular\033[m')
elif nome == 'jessica' or nome == 'vitor':
    print('\033[29mConheço varias pessoa que tem esse nome\033[m')
else:
    print('\033[34mmds, Que nome esquisito você tem!\033[m')
print('\033[35mTenha um bom dia\033[m {}{}{}!'.format('\033[4:30;39m', nome, '\033[m'))