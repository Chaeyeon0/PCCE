def solution(storage, num):
    clean_storage = []
    clean_num = []  # 리스트 인덱스에 중점을 두어야함
    #클린 되기 전 그냥 num은 [2,4,3,1]
    #리스트로 구조화 된 내용 -> 딕셔너리로 구조화?
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(num[i])
            clean_num.append(num[i])

    # 아래 코드에는 틀린 부분이 없습니다.

    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer