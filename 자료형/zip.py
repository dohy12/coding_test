# 두 그룹의 데이터를 서로 엮어주는 파이썬의 내장 함수 zip()

# 기본 예시
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)


# 병렬 처리
for number, upper, lower in zip("12345","ABCDE","abcde"):
    print(number, upper, lower)


# unzip
tmp1 = (1,2,3)
tmp2 = ("A","B","C")
pairs = list(zip(tmp1,tmp2))
print(pairs)
numbers, letters = zip(*pairs)
print(numbers)
print(letters)


# dictionary 변환
keys = [1,2,3]
values = ["A","B","C"]
print(dict(zip(keys,values)))
print(dict(zip(["year","month","data"],[2001,1,31])))


# 주의 사항
numbers = ["1","2","3"]
letters = ["A"]
print(list(zip(numbers,letters)))