class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #byd python 里的set()能自动去重
        return len(set(nums)) != len(nums)
       