# -*- coding: utf-8 -*-
"""1. Two Sum.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xvwdMiNsybFVt7xbxtYOuR5qodEo-0qh
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}  # Dictionary to store the value and its index

        for i in range(len(nums)):
            y = target - nums[i]
            if y in h:
                return [h[y], i]
            h[nums[i]] = i