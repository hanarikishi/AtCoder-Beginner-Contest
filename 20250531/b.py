# 問題 B – Compression:
#
# 長さ N の整数列 A = [A1, A2, …, AN] が与えられる。
# その中に含まれる数について、重複を除いて小さい順に並べた
# 列 C = [C1, C2, …, CM] を作り、これを出力せよ。
#
# 具体的には:
#   - M は A に含まれる異なる値の個数
#   - C1 < C2 < … < CM
#   - 各 Ci は A に出現する
#
# 制約:
#   1 ≤ N ≤ 100
#   1 ≤ Ai ≤ 100
#   すべて整数
#
# 入力:
#   N
#   A1 A2 … AN
#
# 出力:
#   M
#   C1 C2 … CM

##################################################
# 自分の回答
##################################################
N = int(input())
A = list(map(int, input().split()))

lst = []

#set()を使うと重複が省かれる。
for a in A:
    if a not in lst:
        lst.append(a)

lst.sort()
print(len(lst))
print(*lst)

##################################################
# 解説
##################################################
N = int(input())
A = list(map(int, input().split()))

s = set(a) #重複が消える
ans = list(s)
ans.sort(s)
print(len(ans))
print(*ans)
