import sys
from collections import deque

n=int(input())
q=deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "pop":
        if not q:
            print(-1)
            continue
        print(q.popleft())
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if not q:
            print(-1)
            continue
        print(q[0])
    elif cmd[0] == "back":
        if not q:
            print(-1)
            continue
        print(q[-1])