from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        
        # Pure Brute force
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 if sum(nums[i:j+1])*(j-i+1)<k:
#                     result+=1
#         return result

        # Brute force with sum pre-calculated
#         for i in range(len(nums)-1):
#             nums[i+1]+=nums[i]
        
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 if (nums[j]-(nums[i-1] if i>0 else 0)) * (j-i+1)<k:
#                     result+=1
#                 else:
#                     break
#         return result

        # Optimized one
    
        cur = i = 0
        for j in range(len(nums)):
            cur+=nums[j]
            while (cur*(j-i+1)>=k):
                cur-=nums[i]
                i+=1
            result+= j-i+1
        return result