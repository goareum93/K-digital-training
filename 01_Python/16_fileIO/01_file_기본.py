#파일 입출력
#파일 생성하기 (open())
#파일에 쓰기 (write())
#파일에서 읽기(read())
#파일에 추가하기 (append())
#파일 연결 종료 하기 (close())
# with 문과 함께 사용 : close() 단계를 자동 수행함.

#open() 함수
#형식
#파일객체 = open(파일명, 파일 열기모드)
#파일이 저장된 메모리 참조하는 객체로 생성
#open이후 작업에서는 파일객체.함수(파일객체.read())형식으로 사용

#파일 열기 모드
#r : 읽기, w : 쓰기, a : append(파일끝에 내용 추가)

#파일 사용 코드
#파일객체.close()함수- 파일 닫기
#파일 작업이 끝나면 close()함수로 열려있는 파일 객체를 닫는다.
#파일 닫지 않아도 에러는 나지 않고, 프로그램 종료시 전부 자동으로 닫힌다.
#쓰기모드로 연 파일을 닫지 않고 다시 작업하는 경우 에러가 발생
#close()로 닫는 것이 좋다.

#빈 파일 생성
#파일을 쓰기모드(w)로 연다.
#해당파일이 존재하지 않으면 새로 생성하고
#존재하면 덮어 씀(기존 내용은 없어짐)

#원래 있던 파일의 수정은 append 방식으로 열어야 함.

### 파일 입출력의 기본 형식은 txt 임.

#디렉터리 변경하지 않으면 현재 코딩중인 파일의 디렉터리에 생성됨 : 경로를 적어주지 않으면

#!!!!파일 입출력은 콘솔 실행 불가 : 실행메뉴를 이용해야 함.

#파일생성 : 파일명만 적기

# f = open("file1.txt",'w')
# f.close()
# 생성된 file1.txt 파일은 빈 파일

# 경로 수정 : 디렉토리가 존재하지 않는 경우
#
# f = open("c:/python/file1.txt",'w')
# f.close()
# FileNotFoundError: [Errno 2] No such file or directory: 'c:/python/file1.txt'

# 디렉토리 경로 설정 시  '\' 사용하면 오류 발생  => \\ 또는 /
# 파일의 절대경로
# f = open("c:\pythonStudy\file1.txt",'w')
# f = open("c:\\pythonStudy\\file2.txt",'w')
# f.close()
# OSError: [Errno 22] Invalid argument: 'c:\\pythonStudy\x0cile1.txt'

# 상대경로 표현
f = open("../file.txt",'w')
f.close()
# C:/pythonStudy/file.txt

