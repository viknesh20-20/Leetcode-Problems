class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict1 ,dict2= {},{}
        for i in range(len(s)):
            dict1[s[i]] ,dict2[t[i]] = s.count(s[i]), t.count(t[i])
        for j in dict1:
            if dict1[j] != dict2.get(j):
                return False
        return True
                    
        
        
            