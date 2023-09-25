'''Write a program that finds the sum of all elements in an integer array. Use recursion.
Example:
    input: 1 2 3 4 --> output: 10
    input: -1 0 1 --> output: 0
'''


def array_sum(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + array_sum(nums, idx + 1)


nums = [int(x) for x in input().split()]

print(array_sum(nums, 0))
