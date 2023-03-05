import random
c_answer = ""
p_answer = ""
def solution(_str):
    global c_answer
    global p_answer
    orizin_dict = {'a':'a','b':'b','c':'c','d':'d','e':'e','f':'f','g':'g','h':'h','i':'i','j':'j','k':'k', 'l':'l', 'm':'m', 'n':'n',
                   'o':'o','p':'p','q':'q','r':'r','s':'s','t':'t','u':'u','v':'v','w':'w','x':'x','y':'y','z':'z'}
    temp = list(orizin_dict.values())
    random.shuffle(temp)
    rand_dict = (zip(orizin_dict,temp))
    Mapped_Dict = dict(rand_dict)
    for i in range(0, len(_str)) :
        if not _str[i].isalpha():
            c_answer = c_answer + ' '
        for j in Mapped_Dict.keys() :
            if _str[i] == j:
                c_answer = c_answer + Mapped_Dict[j]

    print("암호문 : " + c_answer)

    for i in range(0,len(c_answer)) :
        if not c_answer[i].isalpha() :
            p_answer = p_answer + ' '
        for j in Mapped_Dict.keys():
            if Mapped_Dict[j] == c_answer[i] :
                p_answer = p_answer + j
    return p_answer


Str = input('평문 입력 : ')
print("복호문 : " + solution(Str))


