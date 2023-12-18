N, S, M, L = map(int,input().split())

# priceはでかければ何でもいい
price = 10**8
# rangeの中身は必ず整数にし(100 / 卵の個数(6, 8, 12))の答えの次の次の整数
for a in range(18):
    for b in range(13):
        for c in range(10):
            if a*6 + b*8 + c*12 >= N:
                # ansとa*S + b*M + c*Lの値段で小さいほうをpriceに格納
                price = min(price, a*S + b*M + c*L)

print(price)