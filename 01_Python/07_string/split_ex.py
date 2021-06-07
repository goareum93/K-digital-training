# split() 연습문제
# 1.
# birthday = input('생일 입력(연/월/일) : ')
# birth_split =birthday.split('/')
# print('당신은 %s년에 태어나셨군요' % birth_split[0])
# print('생일은 %s월 %s일 이네요' % (birth_split[1], birth_split[2]))

# 2.주어진 데이터에서 점수만 추출하여 숫자화하고 총점과 평균을 구하시오.
# split을 이용하여 분리
# 문자열.split(':')
# 첫번째 분리된 결과는 리스트 형태로 주어지므로 반복문for를 사용하여 다음 분리때 활용
# 리스트의 요소를 가지고 오려면 [ ] 사용

data = "{a1:30 } ,{a2: 50},{ a3 :20},{a4:70},{a5:40}"
split_data = data.split(',')
score = n = total =0
for d in split_data:
    item = d.split(':')    # d={a1:30}   => ['{a1' , '30}']
    item2 = item[1].split('}')  # '30}'  => ['30']
    score = int(item2[0])
    # score = int(item[1].split('}')[0])
    print(score)
    total += score
    n += 1

print('총점 : %d, 평균 : %f' % (total, total/n))



