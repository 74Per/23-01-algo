import heapq
import sys

q = int(input())
a = []
for i in range(q):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(a, (abs(n), n))
    else:
        if a:
            i, num = heapq.heappop(a)
            print(num)
        else:
            print(0)