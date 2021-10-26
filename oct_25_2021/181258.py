import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

d = deque()

n = int(input())

for _ in range(n):

  # 명령어를 입력 (push, pop, top, empty, size)
  cmd = input().strip().split()

  # 'push'인 경우 -> 뒤의 숫자를 stack에 push 한다.
  if cmd[0] == 'push':
    d.append(int(cmd[1]))

  # 'pop' 인 경우 -> 스택의 맨 마지막 push된 요소를 빼내고 그 값을 출력
  if cmd[0] == 'pop':
    if not d:
      print(-1)
    else:
      print(d.popleft())

  #  'size' 인 경우 -> 스택의 길이를 출력
  if cmd[0] == 'size':
    print(len(d))

  # 'empty' 인 경우 -> 비어있는 여부를 출력
  if cmd[0] == 'empty':
    if not len(d):
      print(1)
    else:
      print(0)

  # 'front' 인 경우 -> 가장 큐 앞에 있는 값을 출력
  if cmd[0] == 'front':
    if not d:
      print(-1)
    print(d[0])
  
  #  'back' 인 경우 -> 가장 큐 뒤에 있는 값을 출력
  if cmd[0] == 'back':
    if not d:
      print(-1)
    print(d[-1])


