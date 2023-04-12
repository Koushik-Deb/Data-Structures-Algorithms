#Problem Statement
# https://leetcode.com/problems/coin-change-ii/
#https://www.codingninjas.com/codestudio/problems/ways-to-make-coin-change_630471?leftPanelTab=1
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def recursion(n,total,coins):
    if n<=0 or total<0:
        return 0
    if total==0:
        return 1

    take = recursion(n,total-coins[n-1],coins)
    notTake = recursion(n-1,total,coins)

    return take+notTake

def memoization(n,total,coins,dp):
    if n<=0 or total<0:
        return 0
    if total==0:
        return 1
    if dp[n][total]!=-1:
        return dp[n][total]

    take = memoization(n,total-coins[n-1],coins,dp)
    notTake = memoization(n-1,total,coins,dp)

    dp[n][total] = take+notTake
    return dp[n][total]

def tabulation(size,amount,coins,dp):
    for i in range(amount+1):
        dp[0][i] = 0

    for i in range(size+1):
        dp[i][0] = 1
            
    for n in range(1,size+1):
        for total in range(1,amount+1):
            take,notTake = 0,0
            if total>=coins[n-1]:
                take = dp[n][total-coins[n-1]]
            notTake = dp[n-1][total]
            dp[n][total] = take+notTake
                
    return dp[size][amount]

def spaceOptmization(size,amount,coins, dp):
    for i in range(2):
        dp[i][0] = 1

    toggleIndex = 1
    for n in range(1,size+1):
        for total in range(1,amount+1):
            take, notTake = 0,0
            if total>=coins[n-1]:
                take = dp[toggleIndex][total-coins[n-1]]
            notTake = dp[toggleIndex^1][total]
            dp[toggleIndex][total] = take+notTake
        toggleIndex^=1

    return dp[toggleIndex^1][amount]

def superSpaceOptmization(size,amount,coins,dp):
    dp[0] = 1
    for n in range(1,size+1):
        for total in range(1,amount+1):
            take,notTake = 0,0
            if total>=coins[n-1]:
                take = dp[total-coins[n-1]]
            notTake = dp[total]
            dp[total] = take+notTake
    return dp[amount]

def countWaysToMakeChange(denominations, value) :
    
#     return recursion(len(denominations),value,denominations)

#     dp = [[-1]*(value+1) for i in range(len(denominations)+1)]
#     return memoization(len(denominations),value,denominations,dp)
    
#    dp = [[0]*(value+1) for i in range(len(denominations)+1)]
#    return tabulation(len(denominations),value,denominations,dp)

#    dp = [[0]*(value+1) for i in range(2)]
#    return spaceOptmization(len(denominations),value, denominations,dp)

    dp = [0]*(value+1)
    return superSpaceOptmization(len(denominations),value,denominations,dp)




























#taking inpit using fast I/O
def takeInput() :
    numDenominations = int(input())

    denominations = list(map(int, stdin.readline().strip().split(" ")))

    value = int(input())
    return denominations, numDenominations, value


#main
denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))