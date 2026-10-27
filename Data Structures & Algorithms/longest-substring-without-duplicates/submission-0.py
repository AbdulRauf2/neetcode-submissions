class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        last_seen = {}
        start = 0 
        best = 0

        for index, ch in enumerate(s):
            if ch in last_seen and start <= last_seen[ch]:
                start = last_seen[ch] + 1
            last_seen[ch] = index
            best = max(best, index - start + 1)
        return best