class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if len(s) => 1 and len(t) <= 5* 10**4:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
