"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating
order, starting with word1. If a string is longer than the other, append the additional letters onto
the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d



"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []        #Initialize an empty list to sotre the merged characters
        i, j = 0, 0        #Initialize 'i' & 'j' to keep track the position of 'word1' & 'word2'.

        while i < len(word1) or j < len(word2):   # The while loop continues as long as there are characters left in either 'word1' or 'word2'.
          if i < len(word1):                      # Check if there are characters left in 'word1'
            result.append(word1[i])               # Append the character at index 'i' in 'word1' to the 'result' list.                                                  
            i += 1                                # Increment the 'i' index to move to the next character in 'word1'
          if j < len(word2):                # Check if there are characters left in 'word2'
            result.append(word2[j])         # Append the character at index 'j' in 'word2' to the 'result' list
            j += 1                          # Increment the 'j' index to move to the next character in 'word2'

        return ''.join(result)
        # Convert the 'result' list to a string by joining its elements together and return the merged string.