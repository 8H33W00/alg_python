def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("원소 개수만큼 문자역을 입력. 구분은 띄어쓰기")
array = input().split()

print(sequential_search(n, target, array))