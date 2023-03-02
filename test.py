import random


answer = ""

def solution(_str):
    global answer
    orizin_dict = {'a':'a','b':'b','c':'c','d':'d','e':'e','f':'f','g':'g','h':'h','i':'i','j':'j','k':'k', 'l':'l', 'm':'m', 'n':'n',
        'o':'o','p':'p','q':'q','r':'r','s':'s','t':'t','u':'u','v':'v','w':'w','x':'x','y':'y','z':'z'}

    #print(orizin_dict.items())
    temp = list(orizin_dict.values())
    random.shuffle(temp)
    rand_dict = (zip(orizin_dict,temp))
    Mapped_Dict = dict(rand_dict)
    #print(Mapped_Dict.items())

    for i in range(0, len(_str)) :
        for j in Mapped_Dict.keys() :
            if _str[i] == j:
                answer = answer + Mapped_Dict[j]
            elif _str[i] == ' ':
                answer = answer + ' '
    return answer


Str = input('입력 하시오 : ')

print(solution(Str))


