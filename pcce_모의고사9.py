def solution(num_list):
    answer = []
    for num in num_list:
        pri = 1
        for i in range (2, num):
            if num%i == 0 :
                answer.append(False)
                pri = 0
                break
        if pri == 1 :
            answer.append(True)
    return answer
