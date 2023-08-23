"""
You have a long flowerbed in which some of the plots are planted, and some are not.
 However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted in 
the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 
"""
def canPlaceFlowers(self, flowerbed, n):
        count = 0    #A counter to keep track newly plated flowers
        i = 0        #index for iterating through the flowerbed
        while i < len(flowerbed):      
            if flowerbed[i] == 0:     #Check if plot is empty
                if i == 0 or flowerbed[i - 1] == 0:  #Check first and previous plot is empty
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:#Check last plot or next plot empty
                        flowerbed[i] = 1   #plant flower in current plot
                        count += 1         #increment count to new flower
            i += 1                      
        return count >= n


