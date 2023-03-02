Autokey_Answer = ""
P_Autokey_Answer = ""
_Vigenere = ""
P_Vigenere = ""
def Vigenere_sol(_str , Vigenere):
    global _Vigenere
    global P_Vigenere
    arr=[0]*len(_str)
    re_arr=[0]*len(_str)
    Key_Stream = [0]*len(_str)
    P_Stream = [0]*len(_str)
    orizin_dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10, 'L':11, 'M':12, 'N':13,
                   'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    for i in range(0 ,len(_str)):
        Key_Stream[i] = orizin_dict[Vigenere[i%len(Vigenere)]]

    for i in range(0,len(_str)):
        P_Stream[i] = orizin_dict[_str[i]]

    for i in range(0 ,len(_str)):
        arr[i] = (P_Stream[i] + Key_Stream[i])%26


    for i in range(0,len(arr)):
        for j in orizin_dict.keys():
            if arr[i] == orizin_dict[j]:
                _Vigenere = _Vigenere + j

    print("암호문 : " + _Vigenere)

    for i in range(0,len(_Vigenere)):
        re_arr[i] = (orizin_dict[_Vigenere[i]] - Key_Stream[i]) % 26
    for i in range(0,len(re_arr)):
        for j in orizin_dict.keys():
            if re_arr[i] == orizin_dict[j]:
                P_Vigenere = P_Vigenere + j
    return P_Vigenere

def Autokey_Cipher_Sol(_str , key):
    global Autokey_Answer
    global P_Autokey_Answer
    Key_Stream = [0]*len(_str)
    P_Stream = [0]*len(_str)
    arr=[0]*len(_str)
    re_arr=[0]*len(_str)
    orizin_dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10, 'L':11, 'M':12, 'N':13,
                   'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

    for i in range(0,len(_str)):
        P_Stream[i] = orizin_dict[_str[i]]

    Key_Stream[0] = key

    for i in range(1,len(_str)):
        Key_Stream[i] = P_Stream[i-1]

    for i in range(0,len(_str)):
        arr[i] = (Key_Stream[i] + P_Stream[i])%26
    for i in range(0,len(arr)):
        for j in orizin_dict.keys():
            if arr[i] == orizin_dict[j]:
                Autokey_Answer = Autokey_Answer + j

    print("암호문 : " + Autokey_Answer)

    for i in range(0,len(re_arr)):
        re_arr[i] = (arr[i]-Key_Stream[i])%26
    for i in range(0,len(re_arr)):
        for j in orizin_dict.keys():
            if re_arr[i] == orizin_dict[j]:
                P_Autokey_Answer = P_Autokey_Answer + j
    return P_Autokey_Answer



Str = input("평문 입력 : ")
Vigenere = input("Vigenere 암호? ")
print("평문 : " + Vigenere_sol(Str.replace(" ","").upper(),Vigenere.upper()))
key_int = int(input("자동 키 암호? : "))
print("평문 : " + Autokey_Cipher_Sol(Str.replace(" ","").upper(),key_int))

