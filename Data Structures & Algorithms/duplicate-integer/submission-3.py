class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num1=set()
        for i in nums:
            if i not in num1:
                num1.add(i)
            else:
                return True
        return False