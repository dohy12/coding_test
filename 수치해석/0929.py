import sys

a_var = sys.maxsize
b_var = 1
c_var = float('inf')
d_var = float(10)

print(a_var)
print(sys.getsizeof(a_var))
print(type(a_var))

print(sys.getsizeof(b_var))
print(type(b_var))

print(sys.getsizeof(c_var))
print(type(c_var))

print(sys.getsizeof(d_var))
print(type(d_var))
