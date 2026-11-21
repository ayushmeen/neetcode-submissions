class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        item=[]
        result=[]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        
        for key, value in freq.items():
            item.append([key, value])
        
        item.sort(key=lambda x:x[1], reverse=True)

        for i in range(k):
            result.append(item[i][0])
        return result