# https://programmers.co.kr/learn/courses/30/lessons/72410
# 프로그래머스 코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 신규 아이디 추천

def solution(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    l = [chr(x) for x in range(ord('a'), ord('z') + 1)] + [chr(x) for x in range(ord('0'), ord('9') + 1)] + ["-","_","."]
    tmp = [x for x in new_id]
    for ch in new_id:
        if ch not in l:
            tmp.remove(ch)
        
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    idx=0
    while True:
        if idx<(len(tmp)-1):
            if tmp[idx]=='.' and tmp[idx+1]==".":
                tmp.pop(idx)
            else:
                idx+=1
        else:
            break

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if len(tmp)>0 and tmp[0] == '.':
        tmp.pop(0)
    if len(tmp)>0 and tmp[-1]=='.':
        tmp.pop()

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(tmp)==0:
        tmp.append("a")
    
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(tmp)>=16:
        tmp = tmp[:15]
        if tmp[-1]=='.':
            tmp.pop()

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(tmp)<=2:
        tmp.append(tmp[-1])

    answer = ''.join(tmp)
    return answer

new_id = "abcdefghijklmn.p"
print(solution(new_id))