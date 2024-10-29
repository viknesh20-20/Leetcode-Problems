class Solution(object):
    def isAnagram(self, s, t):
        dict1 = {}
        dict2 = {}
        if len(s) == len(t):
            for i in range(len(s)):
                sc = s.count(s[i])
                tc = t.count(t[i])
                dict1[s[i]] = sc
                dict2[t[i]] = tc
            for j in dict1:
                if dict1[j] != dict2.get(j):
                    return False
            return True
                    
        else:
            return False
        print(dict1,dict2)
        
            