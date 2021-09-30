from collections import deque
import json

def getText(file_dir):
    f = open(file_dir, 'r')
    tmp_str = f.readline()
    f.close()
    return tmp_str

def getJsonKey(file_dir):
    f = open(file_dir,"r")
    json_data = json.load(f)
    f.close()
    return json_data

def getEncrypt(tmp):
    if int(tmp) == 0: # 암호화
        return True
    elif int(tmp) == 1: # 복호화
        return False
    else:
        exit(0)

def saveText(file_dir, text):
    f = open(file_dir,"w")
    f.write(text)
    f.close()
    return

def playfair(matrix, text, isEncrypt):
    text = text.upper()

    alphabet_list = deque([])
    noneAlphabet_list = [] #(loc, chr)

    # 알파벳만 추출
    for idx,ch in enumerate(text):
        if ord(ch)>=ord('A') and ord(ch)<=ord('Z'):
            alphabet_list.append(ch)
        else:
            noneAlphabet_list.append((idx,ch))    
    
    # 알파벳 두개씩 묶기
    alphabet_zip_list = [] #(ch1, ch2)
    while alphabet_list:
        ch1 = alphabet_list.popleft()

        if len(alphabet_list)>0 and ch1 != alphabet_list[0]:
            ch2 = alphabet_list.popleft()
        else:
            ch2 = 'X'
            pos = (len(alphabet_zip_list))*2
            for idx in range(len(noneAlphabet_list)):
                if noneAlphabet_list[idx][0] > pos:
                    noneAlphabet_list[idx] = (noneAlphabet_list[idx][0]+1, noneAlphabet_list[idx][1])
                else:
                    pos+=1                   

        alphabet_zip_list.append((ch1,ch2))

    # 알파벳 위치 hash table에 넣기
    alphabet_pos_hash = {}
    
    for y in range(5):
        for x in range(5):
            ch = matrix[y][x]
            if len(ch) == 1:
                alphabet_pos_hash[ch] = (y,x)
            else:
                alphabet_pos_hash[ch[0]] = (y,x)
                alphabet_pos_hash[ch[1]] = (y,x)

    # 암호화, 복호화
    encrypted_zip_list = []

    for alphabet_zip in alphabet_zip_list:
        pos1 = alphabet_pos_hash[alphabet_zip[0]]
        pos2 = alphabet_pos_hash[alphabet_zip[1]]

        tmp1, tmp2 = "",""

        if pos1[0] == pos2[0]:   # y 일치
            if isEncrypt:
                tmp1 = matrix[pos1[0]][(pos1[1]+1) if (pos1[1]+1) <5 else 0][0]
                tmp2 = matrix[pos2[0]][(pos2[1]+1) if (pos2[1]+1) <5 else 0][0]
            else:
                tmp1 = matrix[pos1[0]][(pos1[1]-1) if (pos1[1]-1) >=0 else 4][0]
                tmp2 = matrix[pos2[0]][(pos2[1]-1) if (pos2[1]-1) >=0 else 4][0]
        elif pos1[1] == pos2[1]: # x 일치
            if isEncrypt:
                tmp1 = matrix[(pos1[0]+1) if (pos1[0]+1) <5 else 0][pos1[1]][0]
                tmp2 = matrix[(pos2[0]+1) if (pos2[0]+1) <5 else 0][pos2[1]][0]
            else:
                tmp1 = matrix[(pos1[0]-1) if (pos1[0]-1) >=0 else 4][pos1[1]][0]
                tmp2 = matrix[(pos2[0]-1) if (pos2[0]-1) >=0 else 4][pos2[1]][0]
        else:
            tmp1 = matrix[pos1[0]][pos2[1]][0]
            tmp2 = matrix[pos2[0]][pos1[1]][0]

        encrypted_zip_list += [tmp1,tmp2]

    encrypted_text = "".join(encrypted_zip_list)

    # 제외했던 문자열 다시 추가
    for tmp in noneAlphabet_list:
        encrypted_zip_list.insert(tmp[0],tmp[1])

    encrypted_text = "".join(encrypted_zip_list)

    return encrypted_text

text = getText(input("text 파일 입력(파일dir) : "))
key = getJsonKey(input("key 파일 입력(파일dir) : "))
isEncrypt = getEncrypt(input("[0]암호화, [1]복호화, [etc]종료"))
rs_file_name = input("출력 파일 이름 입력 : ")

rs_text = playfair(key["KEY"], text, isEncrypt) # playerfair 암호화 알고리즘 실행

print("텍스트 : ", text)
print("키 : ", key["KEY"])
if isEncrypt:
    print("암호화된텍스트 : ", rs_text)
else:
    print("복호화된텍스트 : ", rs_text)
    
saveText(rs_file_name, rs_text)
print("["+rs_file_name + "]에 텍스트가 저장되었습니다.")