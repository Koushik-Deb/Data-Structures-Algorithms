import collections
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row,col = len(matrix),len(matrix[0])
        
        for r in range(row):
            for c in range(col-1):
                matrix[r][c+1]+=matrix[r][c]
        
        res = 0
        
        for i in range(col):
            for j in range(i,col):
                c = collections.defaultdict(int)
                cur,c[0] = 0,1
                
                for k in range(row):
                    cur+=matrix[k][j]-(matrix[k][i-1] if i>0 else 0)
                    res+=c[cur-target]
                    c[cur]+=1
        return res