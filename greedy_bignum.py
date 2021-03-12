# 문제를 해결하려면 입력값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 됨.
# 연속으로 더할 수 있는 횟수는 최대 k번.
# 가장 큰 수를 k번 더하고 두복 번째로 큰 수를 한번 더하는 연산 반복.



# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k번 더하기
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)