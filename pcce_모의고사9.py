# 소수란 약수가 1과 자기자신뿐인 수를 말합니다.
#
# 어떤 수 N이 소수인지 아닌지 판별하는 방법은 다음과 같습니다.
#
# 1 단계. i를 2부터 N-1까지 1씩 증가시키며 다음을 수행합니다.
#     1-a 단계. i가 N을 나누어 떨어뜨리면 반복을 종료합니다.
#     1-b 단계. i가 N을 나누어 떨어뜨리지 못하면 다음 반복을 진행합니다.
#
# 2 단계. 1 단계의 반복이 종료되면 다음 두 조건을 검사합니다.
#     2-a 단계. 1 단계의 반복이 1-a 단계에서 종료됐다면 N은 소수가 아닙니다.
#     2-b 단계. 1 단계의 반복이 모든 반복을 수행하고 종료됐다면 N은 소수입니다.
# 정수들이 담긴 리스트 num_list가 주어질 때, 리스트의 원소가 소수이면 True, 소수가 아니면 False를 차례로 담은 리스트를 return 하는 solution 함수를 완성해보세요.



def solution(num_list, is_decimal=None):
    answer = []

    for num in num_list:
        is_decimal == True
        for i in range(2, num):
            if num % i ==0:
                answer.append(False)
                is_decimal == False
                break
            if is_decimal == True:
                answer.append(True)
    # for num in num_list:
    #     pri = 1
    #     for i in range (2, num):
    #         if num%i == 0 :
    #             answer.append(False)
    #             pri = 0
    #             break
    #     if pri == 1 :
    #         answer.append(True)
    return answer
