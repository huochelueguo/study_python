def longest(list):
    n = len(list)
    dp = [1] * n
    for i in range(1, n):
        for j in range(1, i+1):
            if list[i] > list[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return dp

l = [6,7,0,1,9,3,5,8,4]
print(longest(l))