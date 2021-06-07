# 클래스메소드 (class mehod) : self 를 통하지 않고 바로 클래스가 메소드 호출
# @classmethod : 클래스메소드임을 표시
# 클래스 변수를 이용하는 메소드를 정의

class Person:
    count = 0  # 클래스변수

    def __init__(self, name):
        Person.count += 1
        self.name = name

    @classmethod
    def showCount(cls):
        print('%d명 태어났습니다' % cls.count)  # cls로 클래스 속성에 접근

    def greeting(self):
        print('%s가 인사해요' % self.name)

kim = Person('Kim')
Person.showCount()
Lee = Person('Lee')
Person.showCount()
kim.greeting()
Lee.greeting()




