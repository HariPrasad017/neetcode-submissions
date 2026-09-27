class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        numset=set()
        for i in range(len(nums)):
            numset.add(nums[i])
        longestseq =1
        for num in numset:
            if num-1 in numset:
                continue
            else:
                currentnum = num
                currentseq = 1
                while currentnum+1 in numset:
                    currentnum +=1
                    currentseq +=1
                longestseq =max(longestseq,currentseq)
        return longestseq
        
