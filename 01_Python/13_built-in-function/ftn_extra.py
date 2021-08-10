# 재귀함수

# def selfCall():
#     print('ha', end='')
#     selfCall()

def selfCall(num):
    if num == 0:
        return
    else:
        print('ha', end='')
        selfCall(num-1)

# selfCall(5)


# 팩토리얼 계산
def fact(num):
    if num==1 :
        return 1
    else:
        return num*fact(num-1)

# print(fact(5))

# 실습: 자연수를 입력받으면 해당하는 자연수까지 출력하는 재귀함수
# 49 입력하면 49~1으로 출력

def count(num):
    pass

def count(num):
    if num == 0:
        return True
    else:
        print(num, end=' ')
        return count(num-1)

def count(num):
    if num == 1:
        return print(1)
    else:
        print(num, end=' ')
        return count(num-1)

count(24)

# 내부함수 : 함수 내에서 정의된 함수
def outFunc(x, y):
    def inFunc(a, b):
        return a + b
    return inFunc(x, y)

# print(outFunc(10, 20))
# print(inFunc(10,20))

# lambda 함수(표현식)
# 방법1.
#   (lambda 매개변수들: 식)(인수들)

# 방법2.
#  객체명 = lambda 매개변수들: 식
#  객체명(인수들)

# def hap(x,y):
#     return x+y
#
# print(hap(10,50))
#
# print((lambda x, y:x+y)(10,50))
# hap2 = lambda x, y:x+y
# print(hap2(5, 10))

# def hap(x=10,y=20):
#     return x+y
# print(hap())
# print(hap(30, 100))
#
# hap3 = lambda x=10, y=20 : x+y
# print(hap3())
# print(hap3(9,10))
#
# # 람다함수 안에서 변수를 생성할 수 없다
# # print((lambda x: y=10, x+y)(10))
# y=10
# print((lambda x: x+y)(1))
#
# # 람다함수 list 사용
# # 리스트의 값에 각각 10을 더하는 람다함수를 작성
# def addTen(x):
#     return x + 10
# # myL = [1,3,4]
# print(list(map(addTen, [1,3,4])))
# print(list(map(lambda x:x+10, [1,3,4])))

# 실습문제. 두개의 리스트의 같은 요소의 값들을 더해서 하나의 리스트로 반환
# 1) def 함수 정의
# 2) lambda 표현식 정의

list1 = [1,2,3,4]
list2 = [10,20,30,40]

def addList(x, y):
    pass

# 1) def 함수 정의
def sumList(a,b):
    for i in range(a):
        a += b
    return a

# print(sumList(list1, list2))

# 2) Lamda 표현식 정의
#y = [10,20,30,40]
print(list(map(lambda x,y: (x + y),[1,2,3,4],[10,20,30,40])))


def addList(x, y):
    newList = []

    for i in range(len(x)):
        newList.append(x[i] + y[i])

    return print(newList)

addList(list1, list2)

# 2) Lambda 표현식 정의
newList = list(map(lambda x, y: x + y,list1, list2))
print(newList)

def hap(a, b):
    return [x + y for x, y in zip(a, b)]

print(hap(list1, list2))
