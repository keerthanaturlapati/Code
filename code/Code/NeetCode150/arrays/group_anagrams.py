# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_anag=defaultdict(list)
        
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            dict_anag[tuple(count)].append(i)
        return list(dict_anag.values())