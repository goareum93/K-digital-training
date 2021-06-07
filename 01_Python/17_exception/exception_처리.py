# 예외 발생 상황 처리

# ZeroDivisionError: division by zero
# print(10/0)
# try:
#     print(10/0)
#     #print(10/2)
# except :
#     print('오류가 발생')
# finally:
#     print('나누기')

# 예외처리 클래스 지정
# try:
#     print(10/0)
#     #print(10/2)
# except Exception:
#     print('오류가 발생')
# finally:
#     print('나누기')

# try:
#     print(10/0)
#     #print(10/2)
# except ZeroDivisionError:
#     print('0으로 나누었네요')
# finally:
#     print('나누기')

# try:
#     print(10/0)
#     #print(10/2)
# except ZeroDivisionError as e:
#     print('0으로 나누었네요 : ', e)
# finally:
#     print('나누기')


# TypeError: can only concatenate str (not "int") to str
# print('age=' + 23)

# try:
#     print('age=' + 23)
# except Exception as e:
#     print(e)
#
# try:
#     print('age=' + 23)
# except TypeError as e:
#     print(e)

# 예외처리를 여러 개 지정하더라도 가장 먼저 나온 에러만 처리
# try:
#     print('age=' + 23)
#     print(10 / 0)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)

# 여러 개의 예외 처리 : 함께 처리 가능
# try:
#     print('age=' + 23)
#     print(10 / 0)
# except (ZeroDivisionError, TypeError) as e:
#     print(e)

#
# try:
#     num = int(input('input number :'))
# except ValueError:
#     print('정수가 아닙니다')
# else:
#     print(num)
# finally:
#     print('종료')
#
try:
    f = open('testex.txt','r')
except FileNotFoundError:
    pass
else:
    data = f.read()
    print(data)
    f.close()
finally:
    print('종료')

