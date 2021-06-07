# 허영대 작성
# with open('yesterday.txt', 'r', encoding='utf-8') as f:
#     textFile = f.readlines()
#     wordCounter = dict()  # 딕셔너리로 단어별 카운트 저장
#     for line in textFile:
#         if line.endswith("\n"):
#             line = line[:-1]
#         wordList = line.lower().split(' ')
#         for word in wordList:
#             if word in wordCounter:
#                 wordCounter[word] += 1
#             else:
#                 wordCounter[word] = 1
#
# print(wordCounter)

# 김정명
with open('yesterday.txt', 'r', encoding='utf-8') as f:
    # 딕셔너리로 저장해서 출력
    dic = dict()

    # 모든 파일을 불러와서 공백기준으로 쪼개기
    # lines에 있는 모든요소를 소문자
    lines = list(f.read().split())
    lines = list(map(lambda x: x.lower(), lines))

    # key값을 나타내기 위해 set으로 중복제거 후 리스트변환
    # 그 리스트를 오름차순 정렬
    temp_lines = list(set(lines))
    temp_lines.sort()

    # key값을 하나씩 불러와서 lines리스트 중 단어를 count한 값을 저장
    for line in temp_lines:
        dic[line] = lines.count(line)

# dic을 item으로 불러와 차례대로 출력
print("[출력결과 : 단어별 빈도]")
for k,v in dic.items():
    print(f"'{k}': {v}")
