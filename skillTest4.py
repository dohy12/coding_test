def binaryChange(s):    
    len_s = len(s.replace("0",""))
    zero = len(s) - len_s
    return [bin(len_s)[2:],zero]

def solution(s):
    answer = [0, 0] #[0]:cnt [1]:zero
    while s!="1":
        tmp = binaryChange(s)
        s = tmp[0]
        answer[0] += 1
        answer[1] += tmp[1]

    return answer

s = "110010101001"
print(solution(s))