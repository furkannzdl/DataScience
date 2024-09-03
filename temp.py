class Solution:
    def maxArea(self, height: list[int]) -> int:
        m = 1
        for i in range(len(height)):
            for j in range(len(height)):
                m = max(min(height[i],height[j]) * abs(j-i),m)
        return m
    

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))