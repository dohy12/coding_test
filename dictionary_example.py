
# def solution(participant, completion):
#     d = {}

#     for x in participant:
#         d[x] = d.get(x, 0) + 1

#     for x in completion:
#         d[x] -= 1

#     dnf = [k for k, v in d.items() if v > 0]

#     answer = dnf[0]
#     return answer

aa = {'0':'AA',
      '1': 'BB',
      '2': 'CC' }

print(aa)

# value를 이용 하여 key를 찾는다.
bb = [k for k, v in aa.items() if v == 'CC']
print(bb[0])

tt = [v for k, v in aa.items() if v == 'CC']
print(tt)

# key와 value를 뒤집는다.
cc = {v:k for k,v in aa.items()}
print(cc)



