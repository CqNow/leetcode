"""
https://leetcode.com/problems/palindrome-number/
"""

import pytest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False





@pytest.mark.parametrize("input_data, expected", [
    (121, True),
    (-121, False),
    (10, False)
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.isPalindrome(input_data) == expected