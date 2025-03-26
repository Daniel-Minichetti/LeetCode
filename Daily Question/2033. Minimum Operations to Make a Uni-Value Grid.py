class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int: 
        
        # 1 the first step in this problem is we want to check for all remainders given that 
        # its important every single number has the exact same remainder to be possible 

        for row in grid: 
            for n in row: 
                if n % x != grid[0][0] % x: 
                    return -1 # remember we are returning an int 
        
        # 2 the next important step is to flatten and sort the grid into a digestable array
        # that can be used 

        nums = sorted([n for row in grid for n in row]) 

                     # for row in grid 
                        # this loop iterates over each row in the 2d grid
                        # ex: grid = [[1, 5], [3, 2]] 
                        # row is [1, 5] & [3 , 2] 

                     # for n in row: 
                        # for each row we are further iterating through every element n in said row
                        # ex: row = [1, 5], n takes values 1 and 5 
                        # ex: row = [3, 2]. n takes values 3 and 2

        # 3  
        # is the sum of all elements before the current element at index i
        prefix = 0 

        # the sum of all elements in the flattened array from earlier which = 20 in test case 1
        total = sum(nums) 

        # 
        res = float("inf") # since we are trying to minimize our result, set it to something big    temporrailty 

        for i in range(len(nums)):
            cost_left = nums[i] * i - prefix 
            # ex if nums = [2, 4, 6, 8] and i = 2 (nums[i] = 6)
            # elements before index 2 are [2, 4] with sum = 6
            # to raise both [2,4] to become [6, 6] total needed sum is 2 * 6 = 12 
            # actual sum is 6, thus cost_left will equal 12 - 6 = 6 

            cost_right = total - prefix - (nums[i] * (len(nums) - i))
            #             20   -   6    - (6 *          (4      -  2 = 2)) 
                            # cost_right = 20 - 6 - (6 * 2) = 2
                                # cost_right = 2
            # total - prefix is used to give you the rest of the array not used in the left side 
                # of the array so from that index to the end 

            # (nums[i] * len(nums)-i)) is the sum we will end up with if all elements from i to the end matched the target, subtracting is done to increment the right side 

            # ex: [2,4,6,8] and i = 2. 
                # elements from index 2 onward are [6, 8] which is a sum of 14 
                # cost_right = 14 - 

            operations = (cost_left + cost_right) // x 

            res = min(res, operations)
            prefix += nums[i]

        return res
        
