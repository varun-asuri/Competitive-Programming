# “Author: My Name
# It is not ok to post my anonymized solution

import heapq # heapq allows me to use A* in the fastest possible way with a Python built-in priority queue

solved = False # boolean to check if the solitaire is solced
best = 0 # closest I've come to the solution in terms of moves played
starting = 0 # number of starting pegs
row = 0 # row count
column = 0 # column count
size = 0 # total position count

def makeMove(moveBoard, x, newPegs):
    index, move = x
    moveBoard[index] = '.' # assign the current square to period
    moveBoard[index+move] = '.' #assign the square jumping over to period
    moveBoard[index+move+move] = 'o' # assign the square im jumping to to circle
    newPegs.remove(index) # remove current location from peg set
    newPegs.remove(index+move) # remove jumped location from peg set
    newPegs.add(index+move+move) # add jumped location to peg set
    return moveBoard, newPegs

def genPossible(board, spots):
    calc = set()
    n = 0
    for spot in spots: # for every location with a peg
        if spot >= (column*2) and board[spot-column] == 'o' and board[spot-(column*2)] == '.': # if the location is not in the top 2 rows and is by a o. combo
            calc.add( (spot, -column) ) # add the location and change to the move list
            n = n - 1 # add this to move count
        if spot < (size-(column*2)) and board[spot+column] == 'o' and board[spot+(column*2)] == '.': # if the location is not in the bottom 2 rows and is by a o. combo
            calc.add( (spot, column) )
            n = n - 1
        if spot%column > 1 and board[spot-1] == 'o' and board[spot-2] == '.': # if the location is not in the left 2 columns and is by a o. combo
            calc.add( (spot, -1) )
            n = n - 1
        if spot%column < (column-2) and board[spot+1] == 'o' and board[spot+2] == '.': #if the location is not in the right 2 columns and is by a o. combo
            calc.add( (spot, 1) )
            n = n - 1
    return n, calc

boards = [] # store every board I am given in this list
puzzles = int(input()) # number of puzzles given as input
for i in range(puzzles): # loop through the puzzle count for each puzzle
    board = [] # list to store puzzle
    if i == 0:
        s = input().strip() # strip the line
        while(s): # while there are lines
            s = list(s) # convert to list
            column = len(s) # store
            for a in s:
                board.append(a) # add each line in to board
            s = input().strip()
        size = len(board) # store
        row = int(size / column) # store
            
    else:
        for n in range(row): # once i know row and column just loops through
            s = input().strip()
            s = list(s)
            for a in s:
                board.append(a)
    if i < puzzles - 1 and i > 0:
        input()
    boards.append(board)

for board in boards: # for every board found
    solved = False # reset solved variable
    moves = set() # set of moves
    pegs = set() # peg locations
    for i in range(size): # for every location
        if board[i] == 'o': # if there is a peg
            pegs.add(i)
            if i >= (column*2) and board[i-column] == 'o' and board[i-(column*2)] == '.': # if not in top 2 rows and is by a o. combo
                moves.add( (i, -column) ) # add it and the change needed to moves
            if i < (size-(column*2)) and board[i+column] == 'o' and board[i+(column*2)] == '.': # if not in bottom 2 rows and is by a o. combo
                moves.add( (i, column) )
            if i%column > 1 and board[i-1] == 'o' and board[i-2] == '.': # if not in left 2 columns and is by a o. combo
                moves.add( (i, -1) )
            if i%column < (column-2) and board[i+1] == 'o' and board[i+2] == '.': # if not in right 2 columns and is by a o. combo
                moves.add( (i, 1) )
    
    # print(0, len(moves), pegs, moves, ''.join(board), 'starting')
    best = 0
    starting = len(pegs) # store number of pegs
    pq = []
    for move in moves: # for every move
        newBoard, newPegs = makeMove(board.copy(), move, pegs.copy()) # generate the board and pegs
        n, newMoves = genPossible(newBoard, newPegs) # calculate possible moves
        heapq.heappush(pq, (starting - 1, n, newPegs, newMoves, newBoard)) # begin the heapq with the first layer (the starting condition is how many pegs are left, the lesser the better so closer to solution while the second is possible moves, the more the higher chance of reaching the solution so I optimize time)

    while pq:
        given, currMoveCount, currPegs, currMoves, currBoard = heapq.heappop(pq) # pop the next best element from the priority queue
        currMovesMade = starting - given # given is sorted to prioritize starting - movecount so change it to be evaluatable
        # print(currMovesMade, -currMoveCount, currPegs, currMoves, ''.join(currBoard), 'while')
        if currMovesMade > best:
            best = currMovesMade # if this beats the current best store it
        currMovesMade += 1
        for move in currMoves:
            newBoard, newPegs = makeMove(currBoard.copy(), move, currPegs.copy()) # calculate the next board and next peg locations
            n, newMoves = genPossible(newBoard, newPegs) # calculate the possible moves for it
            if currMovesMade == starting - 1: # if there is only one pin left then this is a solution
                # print(currMovesMade, -n, newPegs, newMoves, ''.join(newBoard), 'success')
                solved = True # if solution is found exit the code to output result
                best = currMovesMade # store solution
                break
            if n:
                heapq.heappush(pq, (starting - currMovesMade, n, newPegs, newMoves, newBoard) ) # if there are more moves to the board add it to the heap
            elif currMovesMade > best:
                best = currMovesMade # if this is the end with 0 moves and beats the current best store it
        
        if solved: # if i found a solution exit
            break
        
    print(starting - best, best) # number of pegs minus moved played is always pegs left and the second number is pegs placed