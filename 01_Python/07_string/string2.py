# string 관련 함수들

# len() : 문자열의 length
string = 'Python Programming'
n = len(string)
print(n)

# count() : 문자열에서 찾고자하는 문자(열)의 갯수
print(string.count('ing'))

# find() : 특정문자열이 존재여부에 따라 위치인덱스나 -1 반환
print(string.find('ing'))
print(string.find('ong'))

# index() :
print(string.index('ing'))
print(string.index('ong'))



