from collections import deque

N = int(input())
q=deque()

for i in range(1,N+1):
    q.append(i)

while N!=1:
    q.popleft()
    a=q.popleft()
    N-=1
    q.append(a)
print(q[0])