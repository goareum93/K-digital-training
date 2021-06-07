# 실습문제

#1.
def print_coin(text):
    print(text)

def coin():
    coin = "비트코인"
    return coin

# #2 1번에서 정의한 함수를 호출하시오.
# print(coin())
# print_coin('비트코인')
#
# def print_coins():
#     for _ in range(100):
#         print("비트코인")
#
# for i in range(100):
#     print_coin('비트코인')

# 11.
def a(x,y):
    return x * y

# x = int(input('숫자 1 : '))
# y = int(input('숫자 2 : '))

# print(a(x,y))
#
#
# # 12.
# def transCapital():
#     ticker = input('소문자 문자열 입력 : ')
#     return ticker.upper()
#
# print(transCapital())
#
#
# def upp(a):
#     res = a.upper()
#     return res
# res = upp(input("ticker 입력"))
# print(res)


#13.

# def sootja():
#     e=[]
#     while 1:
#         n= int(input('숫자를 입력하세요.(엔터키 누르면 종료) : '))
#         if n=='':   #엔터키 누르면 종료하게 하는것
#            break
#         else:
#            e.append(n)
#     return e

def sootja():
    e=[]
    while 1:
        n= input('숫자를 입력하세요.(엔터키 누르면 종료) : ')
        if n=='':   #엔터키 누르면 종료하게 하는것
           break
        else:
           e.append(int(n))
    return e

def pickup_even():
    e = sootja()
    f=[]
    for i in e:
        if i % 2==0 :
            f.append(i)
        else:
            continue
    return f

print(pickup_even())
