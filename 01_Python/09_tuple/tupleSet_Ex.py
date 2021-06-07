# 1.

# 2.

# 3. num = (1,)
num = 1,

# hi=tuple()
# hi=(1,)
# print(type(hi))
# print(*hi)

# num = tuple()
# num = list()
# num.append(1)
# num = tuple(num)
# print(type(num))
# print(num)

# 5.
t = ('a', 'b', 'c')
listt=list(t)
print(listt)
listt[0]='A'
t=tuple(listt)
print(t)

# 6. 다음 튜플을 리스트로 변환하라.
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print('#6', end=' ') ; print(interest)

print('\n=======================\n')

# 7. 다음 리스트를 튜플로 변경하라.
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print('#7', end=' ') ; print(interest)

#8.
partyA = {"Park", "Kim", "Lee"}
partyB = {"Park", "길동", "몽룡"}

# 1) 파티에 참석한 모든 사람은?
print(partyB | partyA)
# 2) 2개의 파티에 모두 참석한 사람은?
print(partyB & partyA)
# 3) 파티 A에만 참석한 사람
print(partyA - partyB)
# 4) 파티 B에만 참석한 사람
print(partyB - partyA)

print(partyA&partyB^partyA)

partyA = partyB = set()
partyA = {"Park","Kim","Lee"}
partyB = {"Park","길동","몽룡"}

print(partyA.union(partyB))
print(partyA.intersection(partyB))
print(partyA.difference(partyB))
print(partyB.difference(partyA))

