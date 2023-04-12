#Problem Statement
# https://www.codingninjas.com/codestudio/problems/rod-cutting-problem_800284?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0


from sys import stdin
import sys

def recursiveApproach(price, n, size):
    if size<=0 or n<=0:
        return 0
    take,notTake = 0,0
    if n<=size:
        take = price[n-1]+recursiveApproach(price,n,size-n)
    notTake = recursiveApproach(price,n-1,size)
    return max(take,notTake)

def memoizationApproach(price, n, size,dp):
    if size<=0 or n<=0:
        return 0
    if dp[n][size]!=-1:
        return dp[n][size]
    take,notTake = 0,0
    if n<=size:
        take = price[n-1]+memoizationApproach(price,n,size-n,dp)
    notTake = memoizationApproach(price,n-1,size,dp)
    dp[n][size] = max(take,notTake)
    return dp[n][size]

def tabulationApproach(price, n, size, dp):
    for i in range(n+1):
        dp[i][0]=0
        dp[0][i]=0
    
    for i in range(1,n+1):
        for j in range(1,size+1):
            take,notTake = 0,0
            if i<=j:
                take = price[i-1]+dp[i][j-i]
            notTake = dp[i-1][j]
            dp[i][j] = max(take,notTake)
        print(dp[i])
    return dp[n][size]

def spaceOptimized(price, n, size, dp):
    toggleIndex = 1
    for i in range(1,n+1):
        for j in range(1,size+1):
            take, notTake = 0,0
            if i<=j:
                take = price[i-1] + dp[toggleIndex][j-i]
            notTake = dp[toggleIndex^1][j]
            dp[toggleIndex][j] = max(take,notTake)
        toggleIndex^=1
    return dp[toggleIndex^1][size]

def superSpaceOptimized(price, n, size, dp):
    for i in range(1,n+1):
        for j in range(1, size+1):
            take, notTake = 0,0
            if i<=j:
                take = price[i-1]+dp[j-i]
            notTake = dp[j]
            dp[j] = max(take,notTake)
    return dp[size]

def cutRod(price, n):
#     return recursiveApproach(price,n,n)

#     dp = [[-1]*(n+1) for _ in range(n+1)]
#     return memoizationApproach(price, n, n, dp)

   dp = [[-1]*(n+1) for _ in range(n+1)]
   return tabulationApproach(price,n,n,dp)
    
#    dp = [[0]*(n+1) for _ in range(2)]
#    return spaceOptimized(price, n, n, dp)

    # dp = [0]*(n+1)
    # return superSpaceOptimized(price, n, n, dp)

def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
