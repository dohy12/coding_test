def solution(n, arr1, arr2):
    l = []
    for a1,a2 in zip(arr1,arr2):
        st = bin(a1|a2)[2:]
        while len(st)<n:
            st = "0" + st
        st = st.replace("1","#")
        st = st.replace("0"," ")
        l.append(st)
    answer = l
    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))