#  Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        dict_t={}
        for i in s:
            if i in dict_s.keys():
                dict_s.update({i:dict_s[i]+1})
            else:
                 dict_s.update({i:1})
        for j in t:
            if j in dict_t.keys():
                dict_t.update({j:dict_t[j]+1})
            else:
                 dict_t.update({j:1})
        
        print(dict_s)
        print(dict_t)

        if(dict_s==dict_t):
            return True
        else:
            return False 