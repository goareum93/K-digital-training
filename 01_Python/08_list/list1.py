# 리스트의 기본 개념

# intL = [1, 3, 2, 10]
# floatL = [1.5, 3.2, 5.4]
# nameL =['홍길동', '성춘향', '변학도', '방자']
# numL = [1, 3, 4, [1,2]]
# samL = [1,3,.5, '하하']
# print(intL)
# print(type(intL))
# print(numL)
# print(samL)
#
# for x in numL:
#     print(x)
#
# for i in range(len(numL)):
#     print(numL[i])
#
# a, b, c = floatL
# print(a)
# print(b)
# print(c)

# data = "{a1:30 } ,{a2: 50},{ a3 :20},{a4:70},{a5:40}"
# split_data = data.split(',')
# n = total =0
# for d in split_data:
#     id, score = d.split(':')    # d={a1:30}   => ['{a1' , '30}']
#     score = int(score.split('}')[0])  # '30}'  => ['30'] => 30
#     #score = int(item2[0])
#     # score = int(item[1].split('}')[0])
#     print(score)
#     total += score
#     n += 1
#
# print('총점 : %d, 평균 : %f' % (total, total/n))

intL = [1, 3, 2, 10]
floatL = [1.5, 3.2, 5.4]
nameL =['홍길동', '성춘향', '변학도', '방자']
numL = [1, 3, 4, [1,2]]
samL = [1,3,.5, '하하']

# 인덱싱(indexing) & 슬라이싱(slicing)
# print(nameL[-1])
# print(nameL[:])
# print(nameL[1:3])
# print(numL[-1][0])

# allL = []   # 빈 리스트 생성
# allL = list()
#
# allL = [intL, floatL, nameL, numL]
# print(allL)
# print(allL[-1][-1][0])
#
# print(nameL[:-1])
# print(nameL[-1:])
# print(nameL[-1])
# n = len(nameL)
# print(nameL[:n])
#
# # 리스트의  +, * 연산
# sumL = numL + samL
# print(sumL)
# print(numL*3)

# 리스트의 내용 변경
print(numL)
numL[3] = 10
print(numL)
numL[2:4] = []
print(numL)