class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        zippedList = zip(growTime,plantTime)
        sortedList = sorted(zippedList,key=lambda x:-x[0])
        tuples = zip(*sortedList)
        
        grow,plant = [list(tup) for tup in tuples]
        
        track = []
        i,time = 0,0
        
        while(i<len(plant)):
            time += plant[i]
            track.append(time+grow[i])
            i+=1
        track.sort()
        return time if time>=track[-1] else track[-1]
# class Solution:
#     def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
#         zippedList = zip(growTime,plantTime)
#         sortedList = sorted(zippedList,key=lambda x:-x[0])
#         tuples = zip(*sortedList)
        
#         grow,plant = [list(tup) for tup in tuples]
        
#         result = 0
#         i,time = 0,0
        
#         # print(plant,grow)
#         while(i<len(plant)):
#             time += plant[i]
#             result = max(result,time+grow[i])
#             i+=1
        
#         return result