import numpy as np

message = "sshzssfrawlvtevhamjfx"

for c in message:
    if c!=" ":
        print(c+" : ", ord(c)-ord("a"))


n1, n2 = 9,5

key = np.array([[19,25],[8,11]])

value = np.array([[n1],[n2]])


rs = key@value%26

print(rs)
print(rs[0][0],chr(rs[0][0]+ord('a')))
print(rs[1][0],chr(rs[1][0]+ord('a')))

inv = np.linalg.inv(key)
print(inv*29%26)