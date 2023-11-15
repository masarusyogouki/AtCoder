N, Q = map(int, input().split())
S = input()

# 累積和を計算
cumulative_sum = [0]
for i in range(1, N):
    cumulative_sum.append(cumulative_sum[i-1] + int(S[i-1] == S[i]))

# 各質問に対する答えを計算
for _ in range(Q):
    l, r = map(int, input().split())
    result = cumulative_sum[r-1] - cumulative_sum[l-1]
    print(result)
