class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)== 0:
            return chr(258)
        seperator = chr(257)
        result=""
        for s in strs:
            result += s
            result += seperator
        result =result[:-1]
        return result


    def decode(self, result: str) -> List[str]:
        if result == chr(258):
            return []
        seperator = chr(257)
        return result.split(seperator)
