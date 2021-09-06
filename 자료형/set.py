# set은 집합을 의미한다
A = set([4,5,1])
B = set('abc')

A.add(3)
print(A)
print(B)

A = set('abbbc')
print(A)
# 중복을 

# set추가
A.update([5,6,7,8,9])
print(A)

set1 = set([1,2,3])
set2 = set([2,4,5,6])
set3 = set() # 공집합

# 교집합
print (set1 & set2) 
print (set1.intersection(set2))

# 합집합
print (set1 | set2)
print (set1.union(set2))

# set1과 set2의 차집합
print (set1 - set2)

# set1과 set2의 합집합에서 교집합을 뺀 차집합
print (set1 ^ set2)