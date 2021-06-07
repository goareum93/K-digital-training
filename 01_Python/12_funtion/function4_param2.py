# 함수의 매개변수 형식
# 매개변수에 기본값 지정 : default argument

def showMessage(message='Hi!'):
    print(message)

def showMessage2(name, message='Hello!'):
    print(name, message)

# defualt argument는 맨 뒤에
# def showMessage2(message='Hello!', name):
#     print(name, message)

def showInfo(name, age=10, sex='F'):
    print(name, age, sex)


# showMessage('Hello')
# showMessage('Hi')
# showMessage('We are happy!')
# showMessage2('Kim', 'Hi')
# showMessage2('Kim')
# showMessage()

# showInfo('홍길동')
# showInfo('강감찬', 40)
# showInfo('변학도', 40, 'M')


# 함수의 실인수로 리스트가 전달
def showNames(names):
    for name in names:
        print(name, end=' ')

# names = ['Hong', 'Park', 'Chio','Lee']
# showNames(names)

# 함수의 실인수로 딕셔너리가 전달
def showInfoStd(student):
    print(student)
    print('이름 : ', student['name'])
    print('나이 : ', student['age'])
    print('연락처 : ', student.get('phone'))

# info_std = {'name':'Kim', 'age':19, 'phone':'010-1111-1023'}
# showInfoStd(info_std)

# 가변길이 매개변수
#  *args : arguments 1개이상 지정
#  **kwargs : keyword arguments key=value

def mySum(*args):
    total = 0
    for x in args:
        total += x
    return total

# print(mySum(1,3,5))
# print(mySum(3,4))
# print(mySum(1,2,4,5,6))
# print(mySum([1,2,4,5,6]))

def myShowInfo(**kwargs):
    for key in kwargs.keys():
        print(key, end=' ')
    print()
    for value in kwargs.values():
        print(value, end=' ')
    print()
    for item in kwargs.items():
        print(item)

# myShowInfo(id=123, name='Kim', add='Seoul')
# myShowInfo(id=333, name='Lee')
# myShowInfo(id=121, name='Hong', add='Daegu', phone='111-1111')

def calculator(operator, *args):
    pass

def studentInfo(name, age=4, sex='M'):
    student = {'name':name,
               'age':age,
               'sex':sex
               }
    return student

studentInfo('Lee', 30, 'F')   # 위치인수
print(studentInfo(name='Kim', age=30, sex='M'))  #키워드기반 인수
print(studentInfo(name='Kim', sex='M', age=15))

print(studentInfo('Kim', sex='M', age=15))
# print(studentInfo(name='hong', 15, 'F'))  # 오류
# 위치인수와 키워드인수를 혼용할때는 키워드인수는 위치인수 뒤쪽으로