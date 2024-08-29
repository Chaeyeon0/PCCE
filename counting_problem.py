# 1. 아래 리스트 집계하기
grades = [1, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 2]
#인덱스 번호에 등급이라는 의미를 부여해주기

#1.1 리스트로 집계하기
#로직 설계 : 집계할 리스트 / 딕셔너리를 생성해야함 반복문을 통한 순회 / 생성해 놓은 리스트나 딕셔너리 데이터 집계
grade_count = [0,0,0,0]
for grade in grades:
    grade_count[grade] += 1
print(grade_count)

#1.2 딕셔너리로 집계하기
grade_dict = {1:0,2:0,3:0}
for grade in grades:
    grade_dict[grade] += 1
print(grade_dict)

# 2. 아래 리스트 집계하기
votes = ['a', 'b', 'a', 'c', 'a', 'c', 'b', 'b', 'b', 'a']

#2.1 딕셔너리로 집계하기
vote_dict = {'a':0,'b':0,'c':0}
for vote in votes:
    vote_dict[vote] += 1
print(vote_dict)

#2.2 리스트로 집계하기
# 빈 리스트 / 반복문 / 구조화 : 인덱스 번호랑 연결 / 집계
vote_idx = {'a':0,'b':1,'c':2}
vote_count = [0,0,0]
for vote in votes:
    vote_count[vote_idx[vote]] +=1
    #인덱스 딕셔너리를 통해서 0으로 치환이 되면 카운팅 리스트에 0번 리스트에 자동으로 집계가 되는 로직
    #문자열을 숫자로 바꿀 수 있는 방법
print(vote_count)

