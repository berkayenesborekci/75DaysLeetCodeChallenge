class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        #first of all s[i] != s[i+1] so that happy string is like abc, ababc, bcabacb,ab,a,b,c,ac,bc ... but not like that aa, abb, abcc, bb, bcaabc ...
        #secondly n is lenght of the string and k is number of the string
        choices = ['a', 'b', 'c']
        result = []
        def backtrack(current_s):
            if len(current_s) == n:
                result.append(current_s)
                return
            
            for char in ['a', 'b', 'c']:
                if len(current_s) > 0 and current_s[-1] == char:
                    continue
                backtrack(current_s + char)
                if len(result) >= k:
                    return
        
        backtrack("")

        if len(result) >= k:
            return result[k-1]
        else:
            return ""
