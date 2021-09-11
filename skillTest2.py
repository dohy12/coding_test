def solution(participant, completion):
    h = {}
    for p in participant:
        h[p] = h.get(p,0)+1
    for c in completion:
        h[c] -=1
    
    for k,v in zip(h.keys(),h.values()):
        if(v==1):
            return k

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant, completion))