# 함수의 개요

# 함수 정의
def printHello():
    print('Hello')

def printName(name):
    print(name)

def area_sqaure(width, height):
    area = width * height
    return area

# 함수 호출
w = 10; h = 20
area = area_sqaure(w, h)
print(area)
printHello()
printName('Lee')

# 연습문제
# 함수이름 : show_info()

# 이경미
# 20
# 010-1234-1234
# def show_info():
#     print('안지해\n80\n010-444-2523')

def show_info():
    a = '이경미'
    b= '20'
    c= '010 28030354'
    print(a)
    print(b)
    print(c)
    return 0

result = show_info()
print(result)

# 함수이름 sum()
# 숫자 2개를 키보드로 입력받아서 두 수의 합을 출력

# 숫자1 입력 : 10
# 숫자2 입력 : 20
# 합 : 7

def sum():
    a=input('숫자 1 입력 :')
    b=input('숫자 2 입력 :')
    hap=int(a)+int(b)
    print(hap)
    #print(a+b)

sum()