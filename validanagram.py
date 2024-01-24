class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))
        return s == t
    
    def isAnagramBetter(self, s: str, t: str) -> bool: #hash
        if len(s) != len(t):
            return False # just get it out of the way

        dict1, dict2 = {}, {}
        for i in range(len(s)):
            dict1[s[i]] = dict1.get(s[i],0) + 1
            dict2[t[i]] = dict2.get(t[i],0) + 1
        for i in dict1:
            if dict1[i] != dict2.get(i,0):
                return False
            
        return True
    
    #also a unicode/ascii solution I dont get
        
       
c = Solution()
print(c.isAnagram("nagaram", "anagram"))
print(c.isAnagramBetter("nagaram", "anagram"))