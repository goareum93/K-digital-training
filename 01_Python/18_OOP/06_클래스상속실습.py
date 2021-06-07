# 클래스 상속 실습
# 슈퍼클래스 : 사람 클래스 Person <- 서브클래스 : 학생클래스 Student

class Person:
    def __init__(self, age, sex, name):
        self.age = age
        self.name = name
        self.sex = sex

    def greeting(self):
        print('안녕하세요')


class Student(Person):
    # 학교, 학과, 학번, 공부하다(), 시험보다()
    def __init__(self, age, sex, name, school, major, number):
        super().__init__(age, sex, name)
        self.school = school
        self.major = major
        self.number = number

    def study(self):
        print("%s가 %s를 공부하고 있습니다." %(self.name, self.major))

    def test(self):
        print("%s가 %s 과목을 시험치고 있습니다." %(self.name, self.major))

person1 = Person(1, 'F', '이기쁨')
student1 = Student(20, 'M', '이기리', 'S', 'DS', '123')
person1.greeting()
student1.greeting()
student1.study()




