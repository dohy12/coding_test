clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

d ={}

for c in clothes:
    print(c[1])
    d[c[1]] = d.get(c[1],0) + 1
    print(d[c[1]])
    
rs = 1
for v in d.values():
    print(v)
    rs *= (v+1)  

answer = rs-1

print(answer)
