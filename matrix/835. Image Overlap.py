from collections import defaultdict
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        
        dimension = len(img1)
        
        def non_zero_cells(mat):
            ret = []
            for i in range(dimension):
                for j in range(dimension):
                    if mat[i][j]==1:
                        ret.append((i,j))
            return ret
        
    
        transformation_count = defaultdict(int)
        max_overlap = 0
        
        first_ones = non_zero_cells(img1)
        second_ones = non_zero_cells(img2)
        
        for (x_a,y_a) in first_ones:
            for (x_b,y_b) in second_ones:
                tup = (x_b-x_a,y_b-y_a)
                transformation_count[tup]+=1
                max_overlap = max(max_overlap, transformation_count[tup])
                
        return max_overlap

img1 = [[1,1,0],[0,1,0],[0,1,0]]
img2 = [[0,0,0],[0,1,1],[0,0,1]]
solution = Solution()
val = solution.largestOverlap(img1,img2)
print(val)