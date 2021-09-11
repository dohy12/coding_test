def solution(board, skill):

    for s in skill:
        p1 = (s[2],s[1])
        p2 = (s[4],s[3])

        print(p1,p2)
        for y in range(p1[1],p2[1]+1):
            for x in range(p1[0],p2[0]+1):
                board[y][x]+=s[5] * (-1 if s[0]==1 else 1)
        print(board)

    remain = 0 
    for y_l in board:
        for b in y_l:
            if b>0:
                remain+=1    

    answer = remain
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))