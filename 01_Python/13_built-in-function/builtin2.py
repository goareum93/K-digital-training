# 계산과 관련된 내장 함수

# abs() : 절대값 계산

print(abs(-10))
print(abs(100))

# min() : 최소값 계산

print(min(1,-10, 3))
print(min([-9, 10, -30, 3]))

# max() : 최대값 계산

print(max(1,-10, 3))
print(max([-9, 10, -30, 3]))


# pow(base, exp) : x^y

print(pow(2, 10))

# divmod(a, b) : 나머지와 몫 => 결과 (//, %)

print(divmod(9, 2))

# sum(iterable) : 합계
print(sum([1,-10, 3]))

# round(숫자, 소수자리) : 반올림

print(round(9.87))
print(round(9.87, 1))
print(round(-9.87, 1))
print(round(9.87433, 3))

# enumerate(iterable, start=0) : 열거형
# 시퀀스(리슽, 튜플, 문자열, range)를 인덱스값을 포함하느 enumerate 객체로 반환

enum = enumerate(['apple','banana','melon', 'strawberry', 'kiwi','watermelon'])
print(enum)

for i, item in enum:
    print(i, item)

# for item in enum:
#     print(item)

seasons = ['Spring', 'Summer', 'Fall', 'winter']
enumSeason = list(enumerate(seasons, start=1))
print(enumSeason)

# eval()

print(eval('3.1'))
print(eval('10+100'))

# filter(function, iterable) : 반복가능한 자료형 요소에 함수를 적용하여
# 반환값이 참(True)인 결과만 걸러내어 반환

def positive(x):
    return x > 0

print(positive(-9))

result = filter(positive, [-10, 0, 3, -8, 7])
print(type(result))
print(list(result))

# 실습문제 : 짝수인지를 판별하는 함수 even(x)를 정의하고,
# 이 함수를 filter를 이용하여 주어진 리스트의 짝수만 걸러내는 코드

def even(x) :
    return x % 2 == 0

result = filter(even,[1,2,3,4,5,6])
print(list(result))

print('-------------')

# enum = enumerate(['apple', 'banana', 'melon'])
# # enum = list(enum)
# # next()
# for e in enumerate(['apple', 'banana', 'melon']):
#     print(e)
#
# print(enum)
# print(list(enum))
#
# print('-------------')
#
# fruits = iter(['apple', 'banana', 'melon'])
# print(next(fruits))
# print(next(fruits))
# print(next(fruits))
# print(list(fruits))

# list()
list("Hi Hello ")

# sorted(iterable, key=None, reverse=False)
print(sorted([10, -4, 5]))
print(sorted([10, -4, 5], reverse=True))
print(sorted("flower"))
print(sorted("SunFlower", key=str.lower))

# range()

print(type(range(5)))
print(list(range(5)))
print(list(range(2, 10, 3)))
print(tuple(range(5)))

# zip(*iterable) : 각 iterable에서 동일한 인덱스 요소를 추출하여 묶어서 반환

print(zip([1,3,5], ['cat', 'dog', 'horse']))
print(list(zip([1,3,5], ['cat', 'dog', 'horse'])))
print(list(zip([1,3,5], ['cat', 'dog', 'horse','lion'])))
print(tuple(zip([1,3,5], ['cat', 'dog', 'horse'])))

keys = ['cat', 'dog', 'horse']
values = [1,3,5]
result = dict(zip(keys, values))
print(result)

# map()
result = list(map(str, range(10)))
print(result)
print(list(map(int, result)))