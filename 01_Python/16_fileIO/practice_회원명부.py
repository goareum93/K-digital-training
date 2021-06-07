# # 실습예제.
# # 조민호 작성
# def input_member(input_filename):
#     while True:
#         name = input('멤버를 입력하세요.(종료는 q) : ')
#         if name == 'q':
#             return
#         with open(input_filename, 'a', encoding='utf-8') as f:
#             f.write(name+'\n')
#
# def output_member(output_filename):
#     with open(output_filename, 'r', encoding='utf-8') as f:
#         data = f.read()
#     print(data)
#
# def main():
#     while True:
#         order = input('저장 1, 출력 2, 종료 q : ')
#         if order == '1':
#             input_filename = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
#             input_member(input_filename)
#         elif order == '2':
#             output_filename = input('멤버 명단이 저장된 파일명을 입력하세요. : ')
#             output_member(output_filename)
#         elif order == 'q':
#             break
#
# main()
#

# 장우창 작성
# 멤버 입력하는 함수
def input_member(inputfile):
    ifile = open(inputfile, 'w', encoding='utf8')
    while True :
        mem = input('멤버를 입력하세요. (종료는 q) : ')
        if mem == 'q' :
            break
        ifile.write(mem+'\n')
    ifile.close()
    print('저장되었습니다.')

# 멤버 출력하는 함수
def output_member(outputfile):
    ofile = open(outputfile, 'r', encoding='utf8')
    while True :
        line = ofile.readline()
        if line == '' :     # 마지막 줄이면 while문 끝내기
            break
        print(line, end='')
    ofile.close()

if __name__ == '__main__' :
    print('3번 문제. 회원 명단 입출력')
    while True :
        command = input('저장 1, 출력 2, 종료 q : ')
        if command == 'q' :
            break
        elif command == '1' :
            filename = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
            input_member(filename)
        elif command == '2' :
            filename = input('멤버 명단이 저장된 파일명을 입력하세요 : ')
            output_member(filename)

