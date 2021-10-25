import sys
from queue import Queue

def input():
  return sys.stdin.readline().rstrip()

# n명의 사람과 퇴출시킬 k번째를 입력한다.
n, k = map(int, input().split())

# 큐 자료구조를 사용 
q = Queue()

for i in range(1, n+1):
  q.put(i)

# 나간 순서대로 저장할 배열 :정답이 들어갈 배열
result = []

# 큐가 비어있을 때 까지 반복
while not q.empty():
        
        # (0 - k -1)
    for i in range(k):
            #pop과 같다
        num = q.get()
            
        if i == k-1:
            result.append(num)
        else:
            q.put(num)
    
print(result)