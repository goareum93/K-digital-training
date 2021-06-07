# 함수의 매개변수(parameter)
# 함수에 전달(입력)되는 값 (함수 정의할 때)

# 인수(argument) : 함수에 실제로 전달되는 값

# def showInfo(name, age):
#     print('이름은 %s이고 나이는 %d에요' %(name, age))
#
# showInfo('홍길동', 18)
#
#
# def getArea(width, height):
#     return width*height*0.5
#
# w = int(input('밑변:'))
# h = int(input('높이: '))
# print(getArea(w, h))

# 사칙연산을 수행하는 함수들을 정의하여 호출
# add(x, y)
# sub(x, y)
# mul(x, y)
# div(x, y)

# 2개의 숫자를 키보드로 입력받고, 각 함수에 전달하여
# 계산 결과를 아래와 같이 출력하는 코드 완성

# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2.0


# def add(x,y):
#     return x + y
# def sub(x,y):
#     return x - y
# def mul(x,y):
#     return x * y
# def div(x,y):
#     return x / y
#
# x = int(input('숫자1 입력 : '))
# y = int(input('숫자2 입력 : '))
#
# print('%d + %d = %d' %(x, y, add(x,y)))
# print('%d - %d = %d' %(x, y, sub(x,y)))
# print('%d * %d = %d' %(x, y, mul(x,y)))
# print('%d / %d = %.1f' %(x, y, div(x,y)))


# def order():
#     price = int(input('상품가격 : '))
#     qty = int(input('주문수량 : '))
#     amount = int(price * qty)
#     if amount >= 100000:
#         discount = amount*0.1
#     elif amount >= 50000:
#         discount = amount*0.05
#     else:
#         discount = amount
#     total = int(amount-discount)
#
#
#
#     print('상품가격 : ',price,'원')
#     print('주문수량 : ',qty,'개')
#     print('='*20)
#     print('주문액 : ',amount,'원')
#     print('할인액 : ',discount,'원')
#     print('지불액 : ',total,'원')
#
#     return price,qty,amount,discount,total
#
# order()

# def order():
#     price = int(input('상품가격 : '))
#     qty = int(input('주문수량 : '))
#     amount = int(price * qty)
#     if amount >= 100000:
#         discount = amount*0.1
#     elif amount >= 50000:
#         discount = amount*0.05
#     else:
#         discount = amount
#     total = int(amount-discount)
#
#     return price,qty,amount,discount,total

# def order(price, qty):
#     amount = price * qty
#     if amount >= 100000:
#         discount = amount*0.1
#     elif amount >= 50000:
#         discount = amount*0.05
#     else:
#         discount = amount
#     total = int(amount-discount)
#
#     return price,qty,amount,discount,total

#딕셔너리 값으로 반환
def order(price, qty):
    amount = price * qty
    if amount >= 100000:
        discount = amount*0.1
    elif amount >= 50000:
        discount = amount*0.05
    else:
        discount = amount
    total = int(amount-discount)
    info = {'price':price,
            'qty':qty,
            'amount': amount,
            'discount': discount,
            'total': total}
    return info

price = int(input('상품가격 : '))
qty = int(input('주문수량 : '))
order = order(price, qty)
#print('상품가격 : %s',order[0],'원')
#print('주문수량 : ',order[1],'개')
print('='*20)
print(order)
for key in order.keys():
    print(key, ':', order[key])

