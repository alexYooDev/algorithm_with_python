import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

# 숫자를 입력받는다
n = int(input())

# 1~n의 수가 요소인 데크 선언
d = deque([i for i in range(1, n+1)])

# 데크의 크기가 1일 때까지 반복
while len(d) > 1:
  # 가장 첫번째 카드를 뺀다
  d.popleft()
  # 그 다음, 앞에 온 카드를 빼서 뒤로 옮긴다.
  d.append(d.popleft())

print(d[0])
