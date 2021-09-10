# https://programmers.co.kr/learn/courses/30/lessons/43163
# 프로그래머스 코팅테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 단어 변환

def solution(begin, target, words):
    idx_target = -1
    for idx,w in enumerate(words):
        if(w==target):
            idx_target = idx

    if (idx_target) == -1:
        return 0
    else:
        word_len = len(begin)

        words_ch = []        
        for w in words:
            words_l = []
            for j in range(word_len):
                word = w[:j] + (w[j+1:] if (j+1)<word_len else '')
                words_l.append(word)
            words_ch.append(words_l)
        
        begin_l = [begin]
        used = [0 for x in words]
        
        for i in range(word_len+1):      
            b_tmp_l = []
            for b in begin_l:                
                for idx,w_l in enumerate(words_ch):
                    if used[idx]==0:
                        for j in range(word_len):         
                            b_ch = b[:j] + (b[j+1:] if (j+1)<word_len else '')
                            if b_ch == w_l[j]:
                                used[idx] = 1
                                b_tmp_l.append(words[idx])
                                if (idx==idx_target):
                                    return (i+1)
                                break
                
                begin_l = b_tmp_l

        return 0

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]	
print(solution(begin, target, words))