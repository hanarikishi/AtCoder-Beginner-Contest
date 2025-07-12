# 問題 C – Cube and Sum:
#
# 3 つの整数 a, b, c（それぞれ ≤ 10^6）が与えられる。
# 以下の条件を満たすか判定せよ：
#   a^3 + b^3 + c^3 = 0
#
# ただし、a, b, c が負でもよい。
#
# 入力:
#   a b c
#     （例： 1 2 -3）
#
# 出力:
#   条件を満たすなら Yes、満たさなければ No を出力。
#
# 制約:
#   -10^6 ≤ a, b, c ≤ 10^6
#   計算量 O(1) で評価可能（3 乗と合計のみ）。

##################################################
# 自分の回答
##################################################
N, M = map(int, input().split())
counts =[0] * (N+2)
for _ in range(M):
    l,r = map(int, input().split())
    counts[l] += 1
    counts[r+1] -= 1
for i in range(1, N + 1):
    counts[i] += counts[i - 1] #累積和

# 最小の守られている数を出力
print(min(counts[1:N + 1]))

##################################################
# 解説
##################################################
N, M = map(int, input().split())
imos = [0] * (N + 1)
for _ in range(M):
    l,r = map(int, input().split())
    l -= 1 # r+=1ならN+2にする
    imos[l] += 1
    imos[r] -= 1
for i in range(1, N + 1):
    imos[i] += imos[i -1]
ans = 1e9
for i in range(N):
    ans = min(ans, imos[i])
print(ans)