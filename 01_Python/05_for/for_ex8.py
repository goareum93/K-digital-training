# 다중 for (중첩)
'''
for i in range(3):
    for j in range(1, 5):
        print(j+i*4, end='\t')

    print()
'''
n=0
for i in range(3):
    for j in range(1, 5):
        n += 1
        print(n, end='\t')

    print()