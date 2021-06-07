#

# 팩토리얼 계산 함수 factorial()
# n! = n*(n-1)*(n-2)*...*2*1

# def factorial(n):
#     a = n
#     for i in range(a-1, 0, -1):
#         a *= i
#     return a
#
# def fact(n):
#     start = 1
#     for x in range(1, n+1):
#         start *= x
#
#     return print(start)

#재귀함수 :
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
# f(4) : 4*f(3) = 4*3*2*1
# f(3) : 3*f(2) = 3*2*1
# f(2) : 2*f(1) = 2*1
# f(1) : 1
#
# print(factorial(3))
#
# result = factorial(3)
# print(result)
#

n = int(input('n = '))

def factorial(n):
    f = 1
    for i in range(n):
        f *= (i+1)

    return print(f)

factorial(n)


