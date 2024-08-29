#함수

lst = [3,5,4,2,1]
lst.sort()
print(lst)
print(sorted(lst))#정렬된 별도의 리스트를 만들 뿐 우너본 리스트를 건드리지는 못한다는 특징이 있음
#결론 : 함수는 원본을 건들 수는 없음

my_dict = {1:100,2:50,3:20}
sorted_dict = sorted(my_dict.items(), key=lambda x: str(x))
#lambda 내장함수 x : x[1] = 정렬기준

print(sorted_dict)
#항상 앞에 있는 글자를 기준으로 정렬이 이루어진다
#sort 메소드 Key로 정렬의 기준을 알릴 수 있음 + 원본의 리스트를 바꾸는 것
#sorted은 원본은 그대로 두고 컨데이터 적용이 가능하다 + 정렬된 리스트를 따로 생성해서 반환하는 것이고, 다른 변수에 할당해서 사용해야한다
#공통점은 무엇인가 ? : reverse=True 역순