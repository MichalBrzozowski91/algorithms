class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        while len(s) >= 2 and i < len(s):
            if i == 0 and (s[0] == ')' or s[0] == ']' or s[0] == '}'):
                return False
            false_condition = (s[i] == ')' and s[i-1] != '(') or (s[i] == ']' and s[i-1] != '[') or (s[i] == '}' and s[i-1] != '{')
            reduction_condition = (s[i] == ')' and s[i-1] == '(') or (s[i] == ']' and s[i-1] == '[') or (s[i] == '}' and s[i-1] == '{')
            if false_condition:
                return False
            elif reduction_condition:
                s = s[:i-1] + s[i+1:]
                i -= 1
            else:
                i += 1
        if len(s) > 0:
            return False
        else:
            return True
