# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        list_pal=[]
        for i in s:
            if(i.isalnum()):
                list_pal.append(i)
        
        print(list_pal)
        n=len(list_pal)
        print(n)


        i=0
        j=n-1
        while((i!=j) and (i<j)):
            print(list_pal[i],list_pal[j])
            if(list_pal[i].casefold()==list_pal[j].casefold()):
                i=i+1
                j=j-1
            else:
                return False
        return True
                
