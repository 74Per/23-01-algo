import sys
#impoty math
n=int(input())
stack=[]
total=0

for _ in range(n):
    cmd = int(sys.stdin.readline())
    if cmd == 0:
        stack.pop()
        continue
    stack.append(cmd)
print(sum(stack))