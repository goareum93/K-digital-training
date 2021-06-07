# 함수의 반환값(return)

# def sum() :
#     a = int(input('숫자1 입력 :'))
#     b = int(input('숫자2 입력 :'))
#     # print(a+b)
#     return a+b
#
# # res = sum()
# # print('합은 %d' % res)
# print('합은 %d' % sum())

# 삼각형의 넓이 계산 함수 get_triangle_area()
# 높이와 밑변을 키보드로 입력
# 결과값을 반환
# 높이 :
# 밑변 :
# 삼각형의 면적 :

# def get_triangle_area():
#     h = int(input('높이 : '))
#     w = int(input('밑변 : '))
#     area = h * w / 2
#     return area
#
# area = get_triangle_area()
# print('삼각형의 면적 : %.2f' % area)

# 반환값이 여러 개인 경우
# 반환값의 형식은 튜플

# def get_triangle_area():
#     h = int(input('높이 : '))
#     w = int(input('밑변 : '))
#     area = h * w / 2
#     return h, w, area
#
# area = get_triangle_area()
# print('높이 %d, 밑변 %d, 삼각형의 넓이 %.2f' % (area[0], area[1], area[2]))

# def multiReturn() :
#     return 1
#     return 2
#     return 3
#
# print(multiReturn())

#
# def order() :
#     a=int(input('상품가격 입력 : '))
#     b=int(input('주문수량 입력 : '))
#     price=a*b
#     return a,b,price
#
# price=order()
# print('-'*30)
# print('상품가격 : {0}원\n주문수량 : {1}개\n주문액 : {2}원'.format(price[0],price[1],price[2]))


# 리스트 반환값

# def getNames():
#     names = []
#     for i in range(3):
#         name = input('이름 입력 : ')
#         names.append(name)
#
#     return names
#
# nameL = getNames()
# print(type(nameL))
# print(nameL)

# 이름과 나이를 입력받아서 딕셔너리 형식으로 반환
# {'name':'홍길동', 'age':20 }

# def getInfo():
#     info = dict()
#     name = input('이름 입력 : ')
#     age = input('나이 입력 : ')
#     # info['name'] = name
#     # info['age'] = age
#     info = {'name': name , 'age': age}
#     return info
#
# info = getInfo()
# print(info)
# print(type(info))
#
# for key, value in info.items():
#     print(key,':',value)
#
# for key in info.keys():
#     print(key,':',info[key])


# 반환값이 없는 경우 None 출력

def showHello():
    print('Hello')

result = showHello()
print(result)