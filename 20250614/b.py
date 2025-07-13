n,q=map(int, input().split())
x=list(map(int, input().split()))
box = [0]*(n+1)
res = []
for i in range(q):
    if x[i] >= 1:
        box[x[i]] += 1
        res.append(x[i])
    else:
        m = 1e9
        idx=-999
        for j in range(1, n+1):
            if m > box[j]:
                m = box[j]
                idx = j
        box[idx] += 1
        res.append(idx)
print(*res)
