class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring_length = 0
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
                if len(d) > max_substring_length:
                    max_substring_length = len(d)
            else:
                # We delete from the dictionary all letters which appeared before the duplicate:
                d={item:value for (item,value) in d.items() if value > d[s[i]]}
                d[s[i]] = i
                # We add d[s[i]] to all values in our dictionary
                #first_index += d[s[i]]
                #d={item:value - first_index for (item,value) in d.items()}
        return max_substring_length
