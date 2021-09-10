# 제너레이터 예제
def number_generator():
    yield 0
    yield 1
    yield 2

for i in number_generator():
    print(i)

# __next__()
g = number_generator()
print(g.__next__())
print(g.__next__())
print(g.__next__())

g = number_generator()
a = next(g)
print(a)

b = next(g)
print(b)

c = next(g)
print(c)