from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # -----------------brute force-----------
        # result = 0
        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i,len(nums)):
        #         total+=nums[j]
        #         if total==k:
        #             result+=1
        # return result
        

        # -----------------optimized --------------
        # pref = defaultdict(int)
        # total,result = 0,0
    
        # for i in range(len(nums)):
        #     total+=nums[i]

        #     if total==k:
        #         result+=1

        #     if total-k in pref:
        #         result+=pref[total-k]
        #     pref[total]+=1
            
        # return result

        # --------------- code optimized--------------
        pref = defaultdict(int)
        total,result = 0,0
        
        pref[0]=1
        for i in range(len(nums)):
            total+=nums[i]
            result+=pref[total-k]
            pref[total]+=1
            
        return result