import sys
input = sys.stdin.readline

n, q = map(int, input().split())
A = list(range(1, n + 1))
turn = 0
res = []

for _ in range(q):
    tmp = input().strip().split()
    if not tmp:
        continue
    t = int(tmp[0])
    
    if t == 1:
        p, x = int(tmp[1]), int(tmp[2])
        A[(p - 1 - turn + n) % n] = x
    elif t == 2:
        p = int(tmp[1])
        res.append(str(A[(p - 1 - turn + n) % n]))
    else:
        k = int(tmp[1])
        turn = (turn + k) % n

print('\n'.join(res))
