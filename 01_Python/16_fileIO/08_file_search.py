# read()함수 이용하여 원하는 내용이 파일에 있는지 검색

value = input("검색 값 입력 : ")
f = open("test2.txt","r",encoding="utf-8")
data = f.read()
if value in data:
    print('있음',value)
else:
    print("없음")
f.close()

