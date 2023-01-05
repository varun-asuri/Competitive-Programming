# “Author: Varun Asuri
# It is not ok to post my anonymized solution

# CREDIT TO GEEKSFORGEEKS FOR HELP (COIN CHANGE PROBLEM)

import sys # import sys for sys.maxsize

testcases = int(input()) # read in number of test cases
for run in range(testcases): # for each test case
    cost = int(input()) # read in the cost needed to pay

    bills = [] # list of all the bills that i have
    maxbill = 0 # highest denomination bill
    count = int(input()) # number of bills
    for i in range(count): # add to the list of bills with the count
        bill = int(input()) # read the user input in each line
        if bill > maxbill: maxbill = bill # if this bill is larger than the current maxbill make it the new maxbill
        bills.append(bill) # append the bill to my blll list

    required = [sys.maxsize] * (cost + maxbill) # list of how many bills needed to get every amount from 0 to the cost + maxbill (the highest potential value) initialized at maxsize to be really bad
    required[0] = 0 # 0 bills needed to get a value of 0

    for bill in bills: # for each bill
        curr = cost - 1 # in this forloop im adding to found combinations, any combination with a value of cost or higher doesnt need new bills in it
        while curr >= 0: # while the amount im adding to is a positive place in my required list
            if required[curr] == sys.maxsize: # if ive never reached this
                curr -= 1 # increment to the next
                continue # disregard the rest of this function
            if required[curr + bill] > required[curr] + 1: # if the amount i am creating with my current bill doesnt already have a combination with less bills
                required[curr + bill] = required[curr] + 1 # change the value for number of bills needed to reach it
            curr -= 1 # increment to the next
    
    while required[cost] == sys.maxsize: cost += 1 # starting from my target cost, go up until i reach a cost i attained 
    print(cost, required[cost]) # output it along with how many bills i used.