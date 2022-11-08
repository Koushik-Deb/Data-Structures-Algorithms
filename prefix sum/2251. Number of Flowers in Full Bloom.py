# Another solution
# https://leetcode.com/problems/number-of-flowers-in-full-bloom/discuss/1977099/C%2B%2BPython-Binary-Search-and-Sweep-Line

from itertools import accumulate
from typing import List
from sortedContainers import SortedList, SortedSet, SortedDict
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        diff = SortedDict({0: 0})
        for i,j in flowers:
            diff[i] = diff.get(i, 0) + 1
            diff[j + 1] = diff.get(j + 1, 0) - 1
        
        print(diff)
        count = list(accumulate(diff.values()))
        print(count)
        return [count[diff.bisect(t) - 1] for t in persons]
#         start = sorted(flowers,key=lambda x:x[0])
#         end = sorted(flowers, key=lambda x:x[1])
        
#         result = []
        
#         for person in persons:
#             startIndex = bisect.bisect_right(start,person,key=lambda i: i[0])
#             endIndex = bisect.bisect_left(end,person,key=lambda i: i[1])
#             result.append(startIndex-endIndex)
#         return result
    
# https://leetcode.com/problems/number-of-flowers-in-full-bloom/discuss/1977099/C%2B%2BPython-Binary-Search-and-Sweep-Line