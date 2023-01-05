letters = {'p', 'q', 'r', 's', 't'} # store all letters in set for checking
operations = {'K', 'A', 'C', 'E'} # store all operands in set for checking
formula = list(input().strip()) # get first formula in parsedlist form
while formula[0] != '0': # until i reach the last line
    fail = False # initialize a fail check
    length = len(formula) # calculate length
    if(length == 1): # if the length is one
        print('not') # print not and go to next
    else:
        for p in range(2):
            for q in range(2):
                for r in range(2):
                    for s in range(2):
                        for t in range(2): # for every 32 combinations of the 5 variables
                            indx = 1 # start at the second letter
                            stack = [formula[0]] # add the first operand in to the stack
                            while(indx < length):
                                if formula[indx] == 'p': # if its a p add ps value
                                    stack.append(bool(p))
                                elif formula[indx] == 'q': # if its a q add qs value
                                    stack.append(bool(q))
                                elif formula[indx] == 'r': # if its a r add rs value
                                    stack.append(bool(r))
                                elif formula[indx] == 's': # if its an s add ss value
                                    stack.append(bool(s))
                                elif formula[indx] == 't': # if its a t add ts value
                                    stack.append(bool(t))
                                else:
                                    stack.append(formula[indx]) # else add the operand
                                indx += 1
                                while(isinstance(stack[-1], bool) and ((len(stack) > 1 and stack[-2] == 'N') or (len(stack) > 2 and isinstance(stack[-2], bool) and stack[-3] in operations))): # if the stack has a length greater than two and is in the the form Nx or length greater than 3 and is in the form Axx with x being pqrst and A being KACE evaluate
                                    if(isinstance(stack[-1], bool) and len(stack) > 1 and stack[-2] == 'N'): # if it is an N case
                                        w = stack.pop() # pop the letter
                                        stack.pop() # pop N
                                        stack.append(not w) # push opposite of letter
                                    else:
                                        w = stack.pop() # pop letter 1
                                        x = stack.pop() # pop letter 2
                                        action = stack.pop() # pop operand
                                        if action == 'K': # if K push and
                                            stack.append(w and x)
                                        elif action == 'A': # if A push or
                                            stack.append(w or x)
                                        elif action == 'C': # if C push implies
                                            if w and not x: stack.append(False)
                                            else: stack.append(True)
                                        elif action == 'E': # if E push equals
                                            stack.append(w == x)
                            if stack[-1] == False: # if the final condition is a False
                                print('not') # print not while setting fail to break out of all loops to next line
                                fail = True
                                break
                        if fail == True:
                            break
                    if fail == True:
                        break
                if fail == True:
                    break
            if fail == True:
                break
        if fail == False: # if it never failed print tautology
            print('tautology')

    formula = list(input().strip()) # strip next line to evaluate in while loop