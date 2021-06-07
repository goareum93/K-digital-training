# 파일의 단어수 카운트

f = open('yesterday.txt', 'r')
yesterday = f.readlines()
f.close()

contents = ''
words = []
for line in yesterday:
    line = line.split()
    for w in line:
        words.append(w.lower())

# 사용된 단어들만 추출하기 위해 세트로 변경
wordList = set(words)
wordList = list(wordList)
wordList.sort()

# 단어별 빈도 계산을 위한 딕셔너리 생성 및 이용
wordDict = dict()

for w in wordList:
    wordDict[w] = words.count(w)
