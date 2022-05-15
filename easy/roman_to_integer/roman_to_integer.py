"""
https://leetcode.com/problems/roman-to-integer/
"""

import pytest


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_digits = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman_digits[s[i]] < roman_digits[s[i+1]]:
                result -= roman_digits[s[i]]
            else:
                result += roman_digits[s[i]]
        return result






@pytest.mark.parametrize("input_data, expected", [
    ('III', 3),
    ('LVIII', 58),
    ('MCMXCIV', 1994)
])
def test_solution(input_data, expected):
    sol = Solution()
    assert sol.romanToInt(input_data) == expected