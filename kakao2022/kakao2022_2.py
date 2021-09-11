import math
def solution(n, k):
    st = ''
    while n:
        st = str(n%k ) + st
        n = n//k

    st = "22"
    st = st.replace('0',' ')
    l = st.split()
    print(l)

    rs = 0
    for n in l:
        num = int(n)
        
        if num!=1:
            ch = 0
            for i in range(2,math.ceil(num/2)+1):
                print (i)
                if num%i == 0:
                    ch = 1

            if ch == 0:
                rs+=1
            
    return rs


n = 437674
k = 3

print(solution(n, k))