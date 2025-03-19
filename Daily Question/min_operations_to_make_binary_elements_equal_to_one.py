class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        # function made to check if the current index value is 0 and flip it to a 1 accordingly
        def flip(nums, i):
            nums[i] = 0 if nums[i] else 1

        # result of opetaions required to make all elements = 1
        s = 0 

        # - 2 is to stop two elements before the end
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                # flips the first consectuive element
                flip(nums, i)
                # second element...
                flip(nums, i + 1)
                # third element...
                flip(nums, i + 2)
                s += 1
            # the program is checking if the last or 2nd to last elements are 0 
            # if they are we return -1 since we will never be able to fix them given 
            # the consecutive constraint
        if not nums[-1] or not nums[-2]:
            return -1
        
        return s



        
