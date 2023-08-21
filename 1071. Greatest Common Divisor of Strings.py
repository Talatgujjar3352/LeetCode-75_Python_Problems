"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

"""

def gcdStrings(self, str1, str2):
    def gcd(a,b):
        while b:
            a, b = b, a % b  # Update a and b using the Euclidean algorithm (Checkout Euclidean algorithm articles )
        return a             

    if str1 + str2 != str2 + str1:   # Check if concatenating str1 and str2 is not equal to concatenating str2 and str1
        return " "                   

    common_length = gcd(len(str1), len(str2))  # Calculate the common length of a possible common divisor
    return str1[:common_length]                # Return the substring of str1 that represents the common divisor


