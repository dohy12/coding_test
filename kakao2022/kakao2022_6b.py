def solution(board, skill):
    y_n = len(board)
    x_n = len(board[0])

    h = {}
    for s in skill:
        p1 = (s[2],s[1])
        h[(p1)] = h.get(p1,[]).append(s)

    remain = 0 
    for y_idx in range(y_n):

        for x_idx in range(x_n):
            
            s = h.get(p1,[])



    answer = remain
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))