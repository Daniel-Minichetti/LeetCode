class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # developed a empty list called merged to store the merged characters from word 1 and 2
        merged = []

        # run a foor loop to iterate over corresponding characters of word1 and word 2
        for a, b in zip(word1, word2):
            # append concatenation to the merged list
            merged.append(a + b)

        # after loop, append remaining characters of word1 and word 2 that are not covered by the 
        # the loop. 
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])

        # use join() method with an empty string as the delimiter to concatenate all the characters 
        # in the merged list into a single string
        return "".join(merged)
        
