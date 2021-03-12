# M이 10000 이하라면 전의 방법으로 해결가능하나 100억이상 커진다면 시간초과 남.
# 가장 큰 수와 두 번째로 큰 수가 더해질 때 일정하게 반복해서 더해지는 특징 있음.
# 수열의 길이는 K + 1. M을 K + 1로 나눈 몫이 수열의 반복되는 횟수.
# K를 곱해주면 가장ㄷ 큰 수가 등장하는 횟수.
# M이 K + 1로 나누어 떨어지지 않는 경우도 고려. 나눈 나머지만큼 가장 큰 수가 추가로 더해지면 됨.



# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)