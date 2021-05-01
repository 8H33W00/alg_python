def solution(clothes):
    answer = 1
    Ckind = dict()

    for cloth in clothes:
        if(cloth[1] not in Ckind.keys()):
            Ckind[cloth[1]] = 1
        else:
            Ckind[cloth[1]] += 1

    kind_cnt = list(Ckind.values())

    for kc in kind_cnt:
        answer *= (kc + 1)

    return answer - 1