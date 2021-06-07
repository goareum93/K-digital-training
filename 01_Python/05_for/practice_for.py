# print('*****')
# print('****')
# print('*', end=''); print('*',end='') ; print('*')
# print('*', end=''); print('*')
# print('*')

# for j in range(5, 0, -1):
#     for i in range(j):
#         print('*', end='')
#     print()

# for j in range(5, 0, -1):
#     for i in range(j):
#         print(' ', end='')
#     for i in range(j):
#         print('*', end='')

for i in range(1,6):
    print(' '*(6-i)+'*'*(2*i-1))

#
# n = '*'
# for i in range(1,6):
#     for j in range (5-i):
#       print(end=' ')
#     for j in range (1, 2*i):
#         print(n,end='')
#     # for j in range(i,5):
#     #     print(end='-')
#
#     print( )
#
# 2.
num = int(input('숫자 입력 : '))
while True:
    if num == 7:
        print(num, '입력! 종료')
        break
    else:
        num = int(input('다시 입력 : '))
