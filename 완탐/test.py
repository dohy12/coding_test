# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    student = [[] for x in range(3)]
    student_scores = [[x+1,0] for x in range(3)]
    
    student[0] = [1, 2, 3, 4, 5]
    student[1] = [2, 1, 2, 3, 2, 4, 2, 5]
    student[2] = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]   
    
    for i in range(3):
        tmp_l = (student[i] * (len(answers)//5+1))[:len(answers)]
        print(tmp_l)
        for j,k in zip(tmp_l,answers):
            if j ==k:
                student_scores[i][1]+=1       
    
    student_scores.sort(key=lambda x:(x[1],-x[0]), reverse=True)        
    
    answer = [student_scores[0][0]]
    tmp = student_scores[0][1]
    idx = 0
    while True:
        idx += 1
        if idx < len(student_scores) and tmp == student_scores[idx][1]:
            answer.append(student_scores[idx][0])
        else:
            break
    return answer


answers = [1,3,2,4,2,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(solution(answers))