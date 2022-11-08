# Problem Statement
# https://www.codingninjas.com/codestudio/problems/0-1-knapsack_920542

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
def recursion(index, weight):
    if index<=0 or weight<=0: return 0
    take, notTake = 0,0
    if wt[index-1]<=weight:
        take = val[index-1]+recursion(index-1,weight-wt[index-1])
    notTake = recursion(index-1,weight)
    
    return max(take, notTake)

def memoization(index, weight):
    if index<=0 or weight<=0: return 0
    if memo[index][weight]!=-1: return memo[index][weight]
    
    take, notTake = 0,0
    if wt[index-1]<=weight:
        take = val[index-1]+memoization(index-1, weight-wt[index-1])
    notTake = memoization(index-1, weight)
    
    memo[index][weight] = max(take, notTake)
    return memo[index][weight]

def tabulation(N, W):
    for index in range(N+1): tab[index][0] = 0
    for weight in range(W+1): tab[0][weight] = 0
    
    for index in range(1, N+1):
        for weight in range(1, W+1):
            take, notTake = 0,0
            if wt[index-1]<=weight:
                take = val[index-1]+tab[index-1][weight-wt[index-1]]
            notTake = tab[index-1][weight]
            tab[index][weight] = max(take, notTake)
    return tab[N][W]
                
def spaceOptimization(N, W):
    for index in range(2): twoRows[index][0] = 0
    for weight in range(W+1): twoRows[0][weight] = 0
    
    toggleIndex = 1
    
    for index in range(1, N+1):
        for weight in range(1, W+1):
            take, notTake = 0,0
            if wt[index-1]<=weight:
                take = val[index-1]+twoRows[toggleIndex^1][weight-wt[index-1]]
            notTake = twoRows[toggleIndex^1][weight]
            twoRows[toggleIndex][weight] = max(take, notTake)
        toggleIndex ^= 1
    return twoRows[toggleIndex^1][W]
                
def superSpaceOptimization(N,W):
    for index in range(1, N+1):
        for weight in range(W,-1,-1):
            take,notTake = 0,0
            if wt[index-1]<=weight:
                take = val[index-1]+oneRow[weight-wt[index-1]]
            notTake = oneRow[weight]
            oneRow[weight] = max(take, notTake)
    return oneRow[W]

T = int(input())
for i in range(T):
    N = int(input())
    wt = [int(i) for i in input().split()]
    val = [int(i) for i in input().split()]
    W = int(input())

###### recursion 
    print(recursion(N,W))

###### memoization 
    memo = [[-1]*(W+1) for i in range(N+1)]
    print(memoization(N,W))
    
###### tabulation 
    tab = [[-1]*(W+1) for i in range(N+1)]
    print(tabulation(N,W))


###### space optimization (2 rows optimization)
    twoRows = [[-1]*(W+1) for i in range(2)]
    print(spaceOptimization(N,W))


###### SUPER SPACE OPTIMIZATION (1 Row Only)
    oneRow = [0]*(W+1)
    print(superSpaceOptimization(N,W))