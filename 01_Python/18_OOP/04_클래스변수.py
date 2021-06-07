# 인스턴스 변수와 클래스 변수

class Car:
    number = 0
    def __init__(self, speed=0, color='white'):
        self.speed = speed
        self.color = color
        Car.number += 1

    def __str__(self):
        return '이 자동차의 색상은 %s이고,\n속도는 %d입니다.' % (self.color, self.speed)

    # color 필드 값을 반환메소드
    def getColor(self):
        return self.color

    # color 필드값을 변경메소드
    def setColor(self, color):
        self.color = color

    def showInfo(self):
        print('속도는 %d입니다.' % self.speed)

    def drive(self):
        if self.speed != 0:
            print('%d 로 주행중입니다' % self.speed)
        else:
            print('정차중입니다')

    def upSpeed(self, up):
        self.speed += up

    def downSpeed(self, down):
        self.speed -= down
        if self.speed < 0 :
            self.speed = 0

# car1 = Car()
# print(car1.getColor())
# car1.setColor('Red')
# print(car1.getColor())
# # car1.color = 'blue'   # 필드를 외부에 직접 접근
# # car1.__showColor()
# car1.showInfo()
# car1.upSpeed(20)
# car1.drive()
# car1.upSpeed(20)
# car1.drive()
# car1.downSpeed(10)
# car1.drive()
# print(car1)

car1 = Car()
# 인스턴스 변수(필드)
print(car1.speed)
print(car1.color)

# 클래스 변수
print(Car.number)

car2 = Car(10, 'Blue')
print(Car.number)



