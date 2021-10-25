import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

# 숫자를 입력받는다
n = int(input())

# 1~n의 수가 요소인 데크 선언
d = deque([i for i in range(1, n+1)])

while len(d) > 1:
  d.popleft()
  d.append(d.popleft())

print(d[0])
