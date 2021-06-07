## readlines()를 이용하여 파일 읽기

# readline() : 1개의 행씩 읽어 오기, 행 끝에 '\n' 포함
# readlines() : 모든 행을 읽어 라인 단위별로 잘라서 리스트를 생성
#               ['...\n','...\n','...\n',...,'...\n']
# read() : 내용 전체를 한 문자열로 반환 ''' '''

# =============================================

# #----파일 전체 읽고 각 행을 리스트에 저장하기 ------
# # readlines() 결과와 동일
# print('----파일 전체 읽기------')
# f = open('test.txt','r', encoding='utf-8')
# myL = []
# while True:
#     line = f.readline()
#     if(line ==''):
#         break
#     myL.append(line)
# f.close()
# print(myL)

# 파일 전체 읽기
# f = open('test.txt', 'r', encoding='utf-8')
# lines = f.readlines()
# print(lines)
# f.close()

# readlines()로 읽은 내용을 한 줄씩 출력하기

f = open('test.txt', 'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close()
