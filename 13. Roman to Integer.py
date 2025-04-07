class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            if s[i] == 'M':
                result += 1000
            if s[i] == 'D':
                result += 500
            if s[i] == 'C' and i < len(s) - 1:
                if s[i+1] in ['M', 'D']:
                    result -= 100
                else:
                    result += 100
            elif s[i] == 'C':
                result += 100

            if s[i] == 'L':
                result += 50
            if s[i] == 'X' and i < len(s) - 1:
                if s[i+1] in ['C', 'L']:
                    result -= 10
                else:
                    result += 10
            elif s[i] == 'X':
                result += 10

            if s[i] == 'V':
                result += 5
            if s[i] == 'I' and i < len(s) - 1:
                if s[i+1] in ['X', 'V']:
                    result -= 1
                else:
                    result += 1
            elif s[i] == 'I':
                result += 1

        return result


        