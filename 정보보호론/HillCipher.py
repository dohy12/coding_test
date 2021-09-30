import numpy as np
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

def getModularInv(key):
    a,b,c,d = key[0][0], key[0][1], key[1][0], key[1][1]
    determinant = a*d - b*c

    inv = 0
    for inv in range(1,26):
        if (determinant*inv)%26 == 1:
            break   
    
    key = np.array([[d,-b],[-c,a]])

    return (key*inv) % 26

def hillChipher(key, text, isEncrypt):
    text = text.upper()

    alphabet_list = deque([])
    noneAlphabet_list = [] #(loc, chr)

    # 알파벳만 추출
    for idx,ch in enumerate(text):
        if ord(ch)>=ord('A') and ord(ch)<=ord('Z'):
            alphabet_list.append(ord(ch)-ord('A'))
        else:
            noneAlphabet_list.append((idx,ch))    
    
    # 알파벳 두개씩 묶기
    alphabet_zip_list = [] #(ch1, ch2)
    while alphabet_list:
        ch1 = alphabet_list.popleft()

        if len(alphabet_list)>0:
            ch2 = alphabet_list.popleft()
        else:
            ch2 = ord('X')-ord('A')
            pos = len(alphabet_zip_list)*2
            for idx in range(len(noneAlphabet_list)):
                if noneAlphabet_list[idx][0] > pos:
                    noneAlphabet_list[idx] = (noneAlphabet_list[idx][0]+1, noneAlphabet_list[idx][1])

        alphabet_zip_list.append((ch1,ch2))

    # key 처리
    if isEncrypt:
        key_matrix = np.array(key)
    else: # 복호화 -> 모듈러26 역행렬
        key_matrix = getModularInv(np.array(key))

    # 암호화
    rs_list = []

    for alphabet_zip in alphabet_zip_list:
        txt_matrix = np.array([[alphabet_zip[0]],[alphabet_zip[1]]])

        tmp_matrix = (key_matrix @ txt_matrix) % 26
        chr1 = chr(tmp_matrix[0][0] + ord('A'))
        chr2 = chr(tmp_matrix[1][0] + ord('A'))

        rs_list += [chr1, chr2]

    # 제외했던 문자열 다시 추가
    for tmp in noneAlphabet_list:
        rs_list.insert(tmp[0],tmp[1])

    encrypted_text = "".join(rs_list)

    return  encrypted_text


text = getText(input("text 파일 입력(파일dir) : "))
key = getJsonKey(input("key 파일 입력(파일dir) : "))
isEncrypt = getEncrypt(input("[0]암호화, [1]복호화, [etc]종료"))
rs_file_name = input("출력 파일 이름 입력 : ")

rs_text = hillChipher(key["KEY"], text, isEncrypt)

print("텍스트 : ", text)
print("키 : ", key["KEY"])
if isEncrypt:
    print("암호화된텍스트 : ", rs_text)
else:
    print("복호화된텍스트 : ", rs_text)
saveText(rs_file_name, rs_text)
print("["+rs_file_name + "]에 텍스트가 저장되었습니다.")