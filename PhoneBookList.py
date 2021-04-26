def solution(phone_book):
    answer = True
    dic = {}

    for Pnum in phone_book:  # key 폰번호, value 1
        dic[Pnum] = 1

    for Pnum in phone_book:
        temp = ""
        for num in Pnum:  # 번호 한 글자씩 쪼개
            temp += num  # 한개씩 붙이기
            if temp in dic and temp != Pnum:  # dic key로 존재하는지
                answer = False
    return answer