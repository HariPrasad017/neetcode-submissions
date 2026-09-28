class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)== 0:
            return []
        ansmap={}
        count = [0]*26
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            key =""
            for i in range(26):
                key +="#"
                key += str(count[i])
            if key not in ansmap:
                ansmap[key]=[]
            ansmap[key].append(s)
        return list(ansmap.values())
