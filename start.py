import collections
import copy
import math
import sys



def make_table(p):
    length = len(p)
    table = [0] * len(p)
    j = 0
    for i in range(1, length):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table


def kmp(p, s):
    table = make_table(p)
    j = 0
    answers = []
    answer = 0
    aaa = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                answers.append(i - j + 1)
                answer += 1
                j = table[j]
            else:
                j += 1
    return answer, answers


"""
bin(42) 
int('0b111100', 2) 
oct(42) 
hex(42) 
ord() 
chr()
arr.reverse() # 배열 거꾸로
list.count(찾는 값) # 값이 배열에 몇 개가 있는지( 문자열도 가능)
arr.sort(key=lambda x:(x[0], x[1]))
res = a if a > b else b
"""
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

def print(a):
    sys.stdout.write(str(a))


def log2(i):
    return math.log(i, 2)

def iinput(): return int(input())


def lisinput(): return list(map(int, input().split()))


def minput(): return map(int, input().split())


def liinput(): return list(map(int, list(input())))


def dq(): return collections.deque([])


def popl(a): return a.popleft()


def appendl(a, b):
    a.appendleft(b)
    return a


move = [
    [-1, 0],  # 왼
    [0, -1],  # 아래
    [1, 0],  # 오른쪽
    [0, 1],  # 위
]


def in_r(x, N):
    return (0 <= x[0] and x[0] < N and 0 <= x[1] and x[1] < N)


def in_rc(x, r, c):
    return (0 <= x[0] and x[0] < r and 0 <= x[1] and x[1] < c)


def addNode(a, b):
    return [a[0] + b[0], a[1] + b[1]]


def returnValue(graph, node):
    return graph[node[0]][node[1]]

def add(A, value, maps):
    maps[A[0]][A[1]] += value
    return maps
def transpose(graph):
    return list(map(list, zip(*graph)))



def dpcopy(m):
    return copy.deepcopy(m)

def sec_to_time(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    ans = []
    if h < 10:
        ans.append(0)
    ans.append(h)
    ans.append(':')
    if m < 10:
        ans.append(0)
    ans.append(m)
    ans.append(':')
    if s < 10:
        ans.append(0)
    ans.append(s)
    string = ''.join(list(map(str, ans)))
    return string


def time_to_sec(play_time):
    h, m, s = map(int, play_time.split(":"))
    sec = 3600 * h + 60 * m + s
    return sec


def split2times(log):
    s, e = log.split("-")
    return (time_to_sec(s), time_to_sec(e))
# 항상 시간은   min(끝난 시간들) - max(시작 시간들 )

if __name__ == '__main__':
    pass