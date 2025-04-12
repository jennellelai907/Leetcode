class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        min_length = len(min(strs, key=len))

        if min_length == 0:
            return ""

        longest_prefix = ""

        for i in range(min_length):
                
                prefix_count = defaultdict(int)
                
                for word in strs:
                    prefix = word[:i+1]
                    prefix_count[prefix] += 1
                
                if len(prefix_count) > 1:
                    break
                else:
                    longest_prefix = list(prefix_count.keys())[0]


        return longest_prefix