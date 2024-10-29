class Solution(object):
    def isAnagram(self, s, t):
        dict1 = {}
        dict2 = {}
        if len(s) == len(t):
            for i in range(len(s)):
                dict1[s[i]] = s.count(s[i])
                dict2[t[i]] = t.count(t[i])
            for j in dict1:
                if dict1[j] != dict2.get(j):
                    return False
            return True
                    
        else:
            return False
        
            