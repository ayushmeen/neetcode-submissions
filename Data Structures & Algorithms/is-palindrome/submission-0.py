class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split())
        s=re.sub(r"[^a-zA-Z0-9\s]", "", s)
        mid,start,end=len(s)//2,0,len(s)-1
        while start<end:
            if s[start].lower() != s[end].lower():
                return False
            start+=1
            end-=1
        return True
        