class GenresList:
    _list_cnt = 0
    _genresName = ""
    _list = []

    def __init__(self, genresName):
        self._genresName = genresName
        self._list = []

genres = ["classic", "pop", "classic", "classic", "pop", "pop"]
plays = [500, 600, 150, 800, 2500, 600]

d = {}

p_n = 0
for k in genres:
    d[k] = d.get(k, GenresList(k))
    d[k]._list_cnt += plays[p_n]
    d[k]._list.append((plays[p_n], p_n))
    
    if(len(d[k]._list)>1):
        d[k]._list.sort(reverse = True)
        #d[k]._list.sort(key=lambda x:x[0], reverse = True)    
        d[k]._list = d[k]._list[0:2]
    p_n += 1   

genlist = [v for k,v in d.items()]

genlist.sort(key=lambda object:object._list_cnt, reverse = True)

rs = []

for g in genlist:
    for i in g._list:
        rs.append(i[1])

print(rs)

