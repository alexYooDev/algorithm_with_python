import sys

def input():
  return sys.stdin.readline().rstrip()

class Queue:
  
  def __init__(self):
    self.thisQueue = []

  def push(self, n):
    self.thisQueue.append(n)

  def pop(self):
    if self.empty() == 1:
      return -1
    return self.thisQueue.pop(0)

  def size(self):
    return len(self.thisQueue)
  
  def empty(self):
    if len(self.thisQueue) == 0:
      return 1
    else:
      return 0

  def front(self):
    if len(self.thisQueue) == 0:
      return -1
    return self.thisQueue[0]

  def back(self):
    if len(self.thisQueue) == 0:
      return -1
    return self.thisQueue[-1]
    
n = int(input())

q = Queue()

for _ in range(n):

  # 명령어를 입력 (push, pop, top, empty, size)
  cmd = input().strip().split()

  # 'push'인 경우 -> 뒤의 숫자를 stack에 push 한다.
  if cmd[0] == 'push':
    q.push(int(cmd[1]))

  # 'pop' 인 경우 -> 스택의 맨 마지막 push된 요소를 빼내고 그 값을 출력
  if cmd[0] == 'pop':
    print(q.pop())

  #  'size' 인 경우 -> 스택의 길이를 출력
  if cmd[0] == 'size':
    print(q.size())

  # 'empty' 인 경우 -> 비어있는 여부를 출력
  if cmd[0] == 'empty':
    print(q.empty())

  # 'front' 인 경우 -> 가장 큐 앞에 있는 값을 출력
  if cmd[0] == 'front':
    print(q.front())
  
  #  'back' 인 경우 -> 가장 큐 뒤에 있는 값을 출력
  if cmd[0] == 'back':
    print(q.back())


