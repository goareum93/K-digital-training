#list_num.txt 파일을 읽어들이는 코드 작성

# input_file = open("list_num.txt","r")
# list_file=input_file.readlines()
# print(list_file)

#한줄에 두개의 숫자가 저장되어 있는 파일을 읽어와서
#한줄의 두 숫자를 더한 연산을 한 후 연산결과를 파일로 내보내는 프로그램

#파일을 읽어오고 파일에 쓰고, 숫자에 대해 연산하는 기능은 함수로 정의해서 사용
#sum(inputfile 객체,저장파일명)

#메인에서는 해당 함수를 호출해서 결과를 출력한다.
#함수 정의 부분
def sum(input_file,ouput_filename) :
    #함수 기능 구현
    list_file = input_file.readlines() #전달된 파일객체에서 데이터 읽어오기
    output_file = open(ouput_filename,"w")
    # print(list_file)

    #리스트 각 요소에 대하여 필요없는 문자 제거 작업
    for i in range(0,len(list_file)) :
        list_file[i]=list_file[i].replace("\n","")
    # print(list_file)
        if list_file[i] !='' :
            value1,value2 = list_file[i].split()
            sum = float(value1) + float(value2)
            # print(value1,"+",value2,"=",sum)
            new_line = value1+'+'+value2+'='+str(sum) +'\n'
            output_file.write(new_line)
        else :
            continue
    output_file.close() #파일 닫기

#main : 프로그램 실행코드
#숫자가 저장되어 있는 파일 열기
input_file = open("list_num.txt","r")
sum(input_file, "list_calc.txt")
input_file.close()