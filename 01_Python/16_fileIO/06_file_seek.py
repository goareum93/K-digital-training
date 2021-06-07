#파일 내에서 검색
# seek(offset, whence) 함수

# print('----파일 내에서 검색 seek()-------')
# f = open('test2.txt','r', encoding='utf-8')
# # f.seek(0,0)  # 시작위치는 0행, 0열
# # f.seek(1,0)  # 시작위치는 0행, 1열
# # f.seek(7,0)  # 시작위치는 1행 0열
# # f.seek(14,0)
# # f.seek(15,0)  # 오류발생 : UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb0 in position 0: invalid start byte
# # 한글 3바이트
# f.seek(17,0)
# lines = f.readlines()
# print(lines)
# f.close()

# 한글 utf-8 : 3바이트씩, utf-16: 2바이트씩
f = open('test2_utf16.txt','r', encoding='utf-16')  # utf-16으로 파일이 저장된 경우
f = open('test2.txt','r', encoding='utf-8')
# f.seek(0,0)  # 시작위치는 0행, 0열
# f.seek(1,0)  # 시작위치는 0행, 1열
# f.seek(7,0)  # 시작위치는 1행 0열
# f.seek(14,0)
# f.seek(15,0)  # 오류발생 : UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb0 in position 0: invalid start byte
f.seek(16,0)
lines = f.readlines()
print(lines)
f.close()