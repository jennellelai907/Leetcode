class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = []

        for i in range(len(digits)):
            if digits[-i-1] + carry == 10:
                carry = 1
                result.append(0)
            else:
                result.append(digits[-i-1] + carry)
                carry = 0

        if carry == 1:
            result.append(1)

        result.reverse()
        return result
