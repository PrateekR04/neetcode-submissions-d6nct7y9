from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # stores indices
        res = []

        for i in range(len(nums)):
            # Remove indices out of window
            if q and q[0] < i - k + 1:
                q.popleft()

            # Maintain decreasing order
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # Start adding results after first window
            if i >= k - 1:
                res.append(nums[q[0]])

        return res