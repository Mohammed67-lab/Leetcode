"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""
# Brute - Force Approach - Uses 0(n^)
def twoSum_bruteforce(nums, target):
    # Iterate over two loops and add numbers
    for index , first_number in enumerate(nums):
        for sindex, second_number in enumerate(nums):
            if index!=sindex:
                # If addition of 2 numbers gives target return indices of each number
                if first_number + second_number == target:
                    return[index,sindex]


# One Pass Approach - Uses 0(n) Complexity
def one_pass(nums, target):

    # Initialize an empty dictionary to store numbers encountered so far along with their indices
    required_number_dict = {}

    for index , number in enumerate(nums):
        value = target - nums[index]
        # If the complement value is not present in the 'required_number_dict' add it
        if value not in required_number_dict:
            required_number_dict[number] = index
            print (required_number_dict)
        else:
            # if complement value is present return indices
            print([nums.index(value), index])
            return [nums.index(value), index]
    

        


