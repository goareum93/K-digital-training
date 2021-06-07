# 문자열의 구성요소 판단
# isalpha() : 문자여부 True False

# text = '123457num'
# print(text.isdigit())
# print(text.isalpha())
# print('    '.isspace())
# print(text.isalnum())
# print('Abc'.islower())
# print('AAA'.isupper())
#
# print('a'.isdigit())
# print('1'.isalpha())
# print('A'.islower())
# print('A'.isupper())

# 연습문제. 문장을 입력하여 문자, 숫자, 스페이스, 그외문자의 개수를 계산 출력
'나의 email 주소는 imlkm70@daum.net 입니다'

alphas = digits = space = others = 0
string = input('문장을 입력하세요 : ')
for c in string:
    if c.isalpha():
        alphas += 1
    elif c.isdigit():
        digits += 1
    elif c.isspace():
        space += 1
    else:
        others += 1

print('문자 : %d개' % alphas)
print('숫자 : %d개' % digits)
print('공백 : %d개' % space)
print('그외 : %d개' % others)

