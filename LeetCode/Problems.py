#14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for string in zip(*strs):
            if len(set(string)) == 1:
                prefix += string[0]
            else:
                return prefix
        return prefix

#Notes
# zip(*strs) - returns tuples from the object