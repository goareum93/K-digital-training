# while을 이용하여 1~100까지의 정수 중 3의 배수의 합을 출력

n = 1
sum = 0
'''
while n<=100:
    if n % 3 == 0:
        sum += n
    n = n + 1
'''
while n*3 <= 100:
    sum = sum + n*3
    n = n + 1

print('1부터 100까지 중 3의 배수의 합은 %d' %sum)
