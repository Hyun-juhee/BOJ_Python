# 5분
n = int(input())
arr = list(map(int, input().split()))
dp = [0]*n
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = arr[i]
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])
print(max(dp))