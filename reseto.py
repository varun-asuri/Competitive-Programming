n, k = input().split()                  #read in n and k as given
n, k = int(n), int(k)                   #convert to integers
bool_arr = [True] * (n+1)               #initialize a boolean array for all numbers 0 through n
for i in range(2, n+1):                 #skip 0 and 1 then loop through the numbers 2 through n
    if k == 0:                          #if k is zero from finding the number we can break
        break
    if bool_arr[i]:                     #if we havent already checked this number
        for j in range(i, n+1, i):      #go through its multiples
            if bool_arr[j]:             #make sure the multiple is unchecked as well
                bool_arr[j] = False     #cross it out
                k -= 1                  #decrement k after we cross
                if k == 0:              #if k has reached zero
                    print(j)            #that means we have found out solution so we can print, break, and the other break will exit the outer loop
                    break