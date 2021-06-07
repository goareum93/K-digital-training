#사용자로부터 회원 명단을 입력받아서 파일로 저장하는 함수 정의
#input_member(저장파일명)
#사용자로부터 명단 입력 받고 저장이 완료된 후
#저장되었습니다.를 출력
#명단 입력은 q키를 누를때까지 계속 작업 한다.

def input_member(input_file) :
    f = open(input_file,'w',encoding='utf-8')
    while True :
        mem = input("멤버를 입력하세요.(종료는 q) : ")
        if mem == 'q' :
            break
        else :
            f.write(mem + '\n')
    f.close()


#사용자가 입력한 파일을 열어서 출력해주는 함수 정의
#output_member(출력데이터파일명)
#전달된파일명을 이용해서 파일에 들어있는 데이터를 출력한다.
def output_member(output_file) :
    f=open(output_file,'r',encoding='utf-8')
    lines = f.readlines()
    for mem in lines :
        print(mem,end='')
    f.close()


#실행코드(main)
#q를 입력할때 까지 실행은 무한 반복
#사용자에게 저장 1, 출력 2, 종료 q
# input_file=input("멤버 명단을 저장할 파일명을 입력하세요. :")
# input_member(input_file)
# output_file = input("멤버 명단이 저장되어 있는 파일명을 입력하세요. : ")
# output_member(output_file)

#main
while True :
    sel = input("저장 1, 출력 2, 종료 q : ")
    if sel == '1' :
        input_file = input("멤버 명단을 저장할 파일명을 입력하세요. : ")
        input_member(input_file)
    elif sel == '2' :
        output_file = input("멤버 명단이 저장된 파일명을 입력하세요. : ")
        output_member(output_file)
    elif sel == 'q' :
        break
    else :
        print("잘못 입력 하셨습니다.")