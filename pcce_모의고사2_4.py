# 양의 정수 n이 주어졌을 때, n팩토리얼(n!)은 1부터 n까지 모든 수를 곱한 값을 의미합니다.
# 팩토리얼 값을 구하는 코드를 완성해주세요.
#
# 1 ≤ n ≤ 10

n = int(input())

factorial = 1
for i in range(n):
    factorial *= i+1
print(factorial)