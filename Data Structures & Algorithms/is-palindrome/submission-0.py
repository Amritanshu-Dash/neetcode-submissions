class Solution:

    def alphaBetsAndNums(self, currChar):

        ret =   ( ord('A') <= ord(currChar) <= ord('Z') or 
                ord('a') <= ord(currChar) <= ord('z') or
                ord('0') <= ord(currChar) <= ord('9') )
        
        return ret
 
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while(start < end):
            while (not self.alphaBetsAndNums(s[start])) and (start < end):
                start += 1
            while (not self.alphaBetsAndNums(s[end])) and (start < end):
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        
        return True


        

        