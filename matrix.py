matrix = [[3,7,9],
          [4,2,6],
          [8,1,5]]

# #이차원 리스트 원소 접근/수정
# matrix[2][0] += 1
# print(matrix)

#이차원 리스트 순회
# 가로로 순회하는건 행을 고정시켜놓고 행을 순회하는건 -행 우선순회- 이중 for문 이용
#i를 고정시키고 c를 돌려야함
for i in range(3):
    for c in range(3):
        print(matrix[i][c])#어떤 2차원 리스트 379 426 순으로 순회

#열로 순회하는 방법
#c를 고정시키고 i를 돌려야함
for c in range(3):
    for i in range(3):
        print(matrix[i][c])
