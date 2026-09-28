class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k>=len(nums):
            return nums
        count = {}
        for num in nums:
            count[num] =count.get(num,0) +1
        import heapq
        heap=[]
        for i in count.keys():
            heapq.heappush(heap,[count[i],i])
            if len(heap) > k:
              heapq.heappop(heap)
        ans =[0]*k
        for i in range(k):
            ans[i]=heapq.heappop(heap)[1]
        return ans

        
