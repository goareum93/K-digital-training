# Dog class
# 김현재 작성
# class Dog:
#     def __init__(self, breed, size, age, color):
#         self.Breed = breed
#         self.Size = size
#         self.Age = age
#         self.Color = color
#
#     def Eat(self):
#         print('먹는다')
#
#     def Sleep(self):
#         print('먹는다')
#
#     def Eat2(self, a):
#         print('%d 만큼 먹는다', a)
#
#     def Sleep2(self, h):
#         print('%d 동안 잔다', h)
#
#     def Sit(self):
#         print('앉는다')
#
#     def Run(self):
#         print('달린다')
#
# dog1 = Dog('Neapolitan', 'Large', 5, 'Black')
# dog2 = Dog('Maltese', 'small', 2, 'white')
# dog3 = Dog('Chow', 'Medium', 3, 'Brown')

# 노명철 작성
# class Dog:
#     def __init__(self, breed, size, age, Color):
#         self.breed = breed
#         self.size = size
#         self.age = age
#         self.Color = Color
#
#     def eat(self):
#         print('%s가 먹는다.' % self.breed)
#
#     def sleep(self):
#         print('%s가 잠들었다.' % self.breed)
#
#     def run(self):
#         print('%s가 놀고있다.' % self.breed)
#
# dog1 = Dog('Neapolitan Mastiff', 'Large', '5 years','Black')
# dog2 = Dog('Maltese','Small','2 years','White')
# dog3 = Dog('Chow Chow','Medium','3years','Brown')

# 박경빈 작성
class Dog:
    def __init__(self, breed, size, age, color):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color

    def __str__(self):
        print(self.breed, self.size, self.age, self.color)

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

    def Eat(self):
        print("%s가 먹는다." % self.breed)

    def Sleep(self):
        print("%s가 잠들었다." % self.breed)

    def Sit(self):
        print("%s가 앉았다." % self.breed)

    def Run(self):
        print("%s가 뛴다." % self.breed)


if __name__ == "__main__":
    dog1 = Dog("Neapolitan Mastiff", "Lage", 5, "Black")
    dog2 = Dog("Maltese", "Small", 2, "White")
    dog3 = Dog("Chow Chow", "Midium", 3, "Brown")

    dog1.Eat()
    dog2.Sleep()
    dog3.Sit()
    dog3.Run()

    # Dog1.__lt__(Dog2)
    # Dog1.__str__()
    # Dog2.__eq__(Dog3)
    #
    
# 남혜미 작성
    if dog1 < dog2:
        print("%s 나이가 더 많습니다." % dog2.age)
    # else:
    #     print("%s 나이가 더 많습니다." % dog1.age)

    if dog2 == dog3:
        print("%s, %s 의 나이가 같습니다." %(dog2.breed, dog3.breed))
    else:
        print("%s, %s 의 나이가 다릅니다." % (dog2.breed, dog3.breed))