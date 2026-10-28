class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        # countS = {}
        # countT = {}

        # for c in s:
        #     countS[c] = countS.get(c, 0) + 1
        
        # for c in t:
        #     countT[c] = countT.get(c, 0) + 1

        # if countS == countT:
        #     return True
        # return False
        
        
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # print(sorted_s, sorted_t)

        # for i in range(0, len(s)):
        #     if sorted_s[i] != sorted_t[i]:
        #         return False
        # return True
