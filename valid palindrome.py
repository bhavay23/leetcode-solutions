class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        import re

        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        output = True
        s = s.lower()
        i = 0
        j = len(s) - 1
        print(i, j)
        while( j > i ):

            if( s[i] != s[j] ):
                output = False
                break
            i = i + 1
            j = j +-1
        
        return output