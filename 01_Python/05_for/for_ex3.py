# 두 숫자를 입력받아서 이 수 사이의 숫자의 합을 구하기
'''
num1 = int(input('숫자1 입력 : '))
num2 = int(input('숫자2 입력 : '))
sum = 0

if(num1<= num2):
    for i in range(num1, num2+1):
        sum += i
else:
    for i in range(num2, num1+1):
        sum += i

print('%d과 %d사이의 합은 %d' %(num1, num2, sum))


# 단 수를 입력받아서 해당 구구단 출력

dan = int(input('단 수 입력 : '))
for n in range(1, 10):
    print('%d * %d = %2d' %(dan, n, dan*n))

'''
# 카운트 다운 프로그램 작성

count =int(input('시작 숫자를 입력하시오 : '))
for n in range(count,0,-1):
    print("%d" % n, end=' ')
print('발사')
