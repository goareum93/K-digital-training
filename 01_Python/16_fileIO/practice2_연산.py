# 채길호
# def sum(input,result):
#     with open(result,'w',encoding='utf-8') as result:
#         with open(input,'r',encoding='utf-8') as f:
#             data = f.read().split().copy()
#             print(data)
#             for i in range(len(data)):
#                 if i%2==0:
#                     if int(data[i+1])<0:
#                         sic = data[i] + data[i+1]
#                         sum_result = str(int(data[i])+int(data[i+1]))
#                         result.write(sic)
#                         result.write('=')
#                         result.write(sum_result+'\n')
#                     else:
#                         sic = data[i] + '+' + data[i + 1]
#                         sum_result = str(int(data[i]) + int(data[i + 1]))
#                         result.write(sic)
#                         result.write('=')
#                         result.write(sum_result + '\n')
#
# if __name__ == '__main__':
#     sum('list_num.txt','sum_result.txt')

# 강아름
def sum(inputfile, outputfile):
    temp = []

    g = open(inputfile, 'r')
    r = open(outputfile, 'w')

    for i in g.readlines():
        temp = i.split()
        r.write('%s + %s = %.1f\n' % (temp[0], temp[1], float(temp[0]) + float(temp[1])))

    g.close()
    r.close()

sum('list_num.txt', 'two_numbers_result.txt')
