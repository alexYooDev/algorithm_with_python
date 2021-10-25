'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

class Stack:
  
  def __init__(self):
      self.thisStack = []

  def push(self, x):
    self.thisStack.append(x)
  
  def pop(self):
    if self.empty() == 1:
      return -1
    return self.thisStack.pop()

  def size(self):
    return len(self.thisStack)
  
  def empty(self):
    if self.size() == 0:
      return 1
    else:
      return 0

  def top(self):
    if not self.thisStack:
      return -1
    else:
      return self.thisStack[-1]

n = int(input())

s = Stack()

for _ in range(n):

  # 명령어를 입력 (push, pop, top, empty, size)
  cmd = input().strip().split()

  # 'push'인 경우 -> 뒤의 숫자를 stack에 push 한다.
  if cmd[0] == 'push':
    s.push(int(cmd[1]))

  # 'pop' 인 경우 -> 스택의 맨 마지막 push된 요소를 빼내고 그 값을 출력
  if cmd[0] == 'pop':
    print(s.pop())

  #  'size' 인 경우 -> 스택의 길이를 출력
  if cmd[0] == 'size':
    print(s.size())

  # 'empty' 인 경우 -> 비어있는 여부를 출력
  if cmd[0] == 'empty':
    print(s.empty())

  # 'top' 인 경우 -> 가장 스택 위에 있는 값을 출력
  if cmd[0] == 'top':
    print(s.top())






