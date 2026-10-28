from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list) # creates a dictionary of empty list

        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)
        return list(groups.values())            

