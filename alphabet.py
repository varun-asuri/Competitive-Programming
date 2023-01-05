# “Author: Varun Asuri
# It is not ok to post my anonymized solution

# CREDIT TO GEEKSFORGEEKS FOR HELP (LONGEST INCREASING SUBSEQUENCE)

import sys # import sys to use for sys.maxsize

def recur(curr, prev, seq, dp): # recursive function to break down the problem 
    if (curr == len(seq)): return 0 # if i've reached the end of the sequence return 0 as i can't add more elements 
    if (dp[curr][prev + 1] != -1): return dp[curr][prev + 1] # if this locations calculation till the end has been done access it

    skip = recur(curr + 1, prev, seq, dp) # find the longest sequence if we skip this character
    add = -sys.maxsize -1 # initialize the sequence if we use this character at a horrible value to ensure it isnt picked in max
    if (prev == -1 or seq[curr] > seq[prev]): add = 1 + recur(curr + 1, curr, seq, dp) # if we can use this character get one plus the calculation from the next
    dp[curr][prev + 1] = max(add, skip) # find the longest sequence from this location based on adding or skipping the next character

    return dp[curr][prev + 1] # return longest sequence found till this point

seq = [ord(x) - 97 for x in list(input())] # list of all letters given connecting a to 0 and z to 25 etc with ascii to make compares easier
dp = [[-1 for i in range(len(seq) + 1)] for j in range(len(seq) + 1)] # matrix that stores longest list from a location given its previous initialized to -1
print(26 - recur(0, -1,  seq, dp)) # print 26 - longest sequence as that is the remaining needed to add