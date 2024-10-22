class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ct=0
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                ct+=1
                if s[i-1] == " ":break
        return ct
                
        