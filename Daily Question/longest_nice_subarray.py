# goal is to find the the length of the longest nice subarray in the given array
# will utilize sliding window technique


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0 

        # Each number has a certain set of bits set to 1
        current_window = 0 # bitmask tracking all bits set within the current subarray


        # left pointer indiciates left boundary of the window
        left_pointer = 0 
        # n will act as right boundary of the window
        for n in range(len(nums)):
            # move right as long as the new number nums[n] doesnt conflict with existing ones 
            # in the current window
            while current_window & nums[n]:
                # removes the leftmost number from the window to resolve conflicts (shrinking)
                current_window = current_window ^ nums[left_pointer]
                # increments left pointer until the conflict is resolved
                left_pointer += 1
            res = max(res, n - left_pointer + 1) # right minus left + 1
            current_window = current_window | nums[n]


        return res

# O(n) because each number is visited at most twice (once by left and once by right pointer)         
