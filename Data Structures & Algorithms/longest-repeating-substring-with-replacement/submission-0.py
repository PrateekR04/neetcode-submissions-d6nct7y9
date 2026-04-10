from collections import defaultdict 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxFrequency = 0
        longest = 0
        counter = defaultdict(int)

        for right in range(len(s)):

            counter[s[right]] += 1
            maxFrequency = max(maxFrequency, counter[s[right]])

            while (right - left + 1) - maxFrequency > k:
                counter[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)

        return longest

