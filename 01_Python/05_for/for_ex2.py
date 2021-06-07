# 1에서 20까지의 정수 중 3의 배수 출력하고 합계 구하기


total = 0
for n in range(0,20,3):
    print(n, end=' ')
    total += n

print('\n1~20사이의 3의 배수 합 : %d ' %total)

# range()의 step 인수를 사용하지 않고
# 3의 배수 출력하고 합계 구하기
'''
total = 0
for n in range(20):
    if n % 3 == 0:
        print(n, end=' ')
        total += n
'''
total = 0
for n in [1,2,3,4,5,6]:
    x = n*3
    print(x, end=' ')
    total += x
print('\n1~20사이의 3의 배수 합 : %d ' %total)
