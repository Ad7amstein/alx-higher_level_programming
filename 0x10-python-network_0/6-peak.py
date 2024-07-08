#!/usr/bin/python3
"""Find peak
"""


def find_peak(nums=None):
    """Finds a peak in a list of numbers
    """
    if not nums or len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    if len(nums) >= 2:
        if nums[0] >= nums[1]:
            return nums[0]
        if nums[len(nums) - 1] >= nums[len(nums) - 2]:
            return nums[len(nums) - 1]
    for i in range(1, len(nums)-1):
        if nums[i - 1] <= nums[i] >= nums[i + 1]:
            return nums[i]
    return None
