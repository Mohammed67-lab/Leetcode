# Brute - Force Approach - Uses 0(n^)
def twoSum_bruteforce(nums, target):
    # Iterate over two loops and add numbers
    for index , first_number in enumerate(nums):
        for sindex, second_number in enumerate(nums):
            if index!=sindex:
                # If addition of 2 numbers gives target return indices of each number
                if first_number + second_number == target:
                    return[index,sindex]
