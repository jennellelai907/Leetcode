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

# Optimization:
# 使用字典來簡化羅馬數字的映射
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        
        for i in range(len(s)):
            # 如果當前數字小於下一個數字，則進行減法操作
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                result -= roman_values[s[i]]
            else:
                result += roman_values[s[i]]
        
        return result