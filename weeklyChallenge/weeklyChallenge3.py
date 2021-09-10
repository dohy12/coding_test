# https://programmers.co.kr/learn/courses/30/lessons/85002
# 프로그래머스 코팅테스트 연습 > 위클리 챌린지 > 3주차
# 두번만에 완료!

dir = [[1,0],[-1,0],[0,1],[0,-1]]

def rotate(shape):
    l = [[] for x in range(4)]
    # 0도
    l[0] = list(shape)

    # 90도 회전
    for p in shape:
        l[1].append((-p[1],p[0]))

    # 180도 회전
    for p in shape:
        l[2].append((-p[0],-p[1]))

    # 270도 회전
    for p in shape:
        l[3].append((p[1],-p[0]))
    
    return setOrigin(l)


def setOrigin(shapes):
    for s_idx,shape in enumerate(shapes):
        shape.sort(key=lambda x:(x[1],x[0]))
        origin = shape[0]

        for idx,p in enumerate(shape):
            shape[idx] = (p[0]-origin[0], p[1]-origin[1])
        shapes[s_idx] = tuple(shape)

    return set(shapes)


def getShape(pos,game_board,ch):
    global dir
    n = len(game_board)
    shape = []
    stack = [pos]
    while stack:        
        p_pos = stack.pop()
        shape.append((p_pos[0]-pos[0],p_pos[1]-pos[1]))
        game_board[p_pos[1]][p_pos[0]] = ch
        for d in dir:
            if (p_pos[0] + d[0])>=0 and (p_pos[0] + d[0])<n and (p_pos[1] + d[1])>=0 and (p_pos[1] + d[1])<n and game_board[p_pos[1]+ d[1]][p_pos[0]+ d[0]] == 1-ch:
                game_board[p_pos[1]+d[1]][p_pos[0]+d[0]] = ch
                stack.append( (p_pos[0]+d[0],p_pos[1]+d[1]) )   

    if ch == 1:
        shape.sort(key=lambda x:(x[1],x[0]))
    return tuple(shape)


def solution(game_board, table):
    empty_l = []
    shape_l = []
    shape_rotate = []
    for y,i in enumerate(game_board):
        for x,j in enumerate(i):
            if j==0:
                empty_l.append(getShape((x,y),game_board,1))

    for y,i in enumerate(table):
        for x,j in enumerate(i):
            if j==1:
                shape_l.append(getShape((x,y),table,0))

    for shape in shape_l:
        shape_rotate.append(rotate(shape))

    h = {}
    for e in empty_l:
        h[e] = h.get(e,0) + 1

    cnt = 0
    for shapes in shape_rotate:
        for s in shapes:
            if s in h and h[s]>0:
                h[s]-=1
                cnt += len(s)
                break

    return cnt


game_board  = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table       = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

print(solution(game_board, table))