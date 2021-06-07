# continue문

x = 0
while x<10:
    x += 1
    if x % 2 !=0:   #짝수
        continue
    print(x)

#무한반복(loop) & break

while True:
    print("반복시작")
    answer = input("종료하려면 x입력 :")
    if answer=='x':
        break

print('반복 종료')