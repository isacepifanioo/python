import time
print('-=-' * 8)
print('  \033[36mContagem regressiva\033[m')
print('-=-' * 8)
time.sleep(1)
for c in range(10, 0 - 1, -1):
    print(c)
    time.sleep(1)
print('-=-' * 8)
print('\033[34mFeliz ano Novo\033[m!!')