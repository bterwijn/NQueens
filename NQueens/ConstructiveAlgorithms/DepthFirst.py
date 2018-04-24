
from NQueens.Board.Board import *

def depthFirstRecursive(board):
    """ Recursive Depth First Search algorithm. """
    if board.isDone(): # recursive stop condition
        print("***** FOUND SOLUTION:")
        print(board.toString())
    else:
        unusedX=board.getUnusedX() # Get and change board private member, bit ugly but fast.
                                   # Note that after trying all entries 'unusedX' has
                                   # again its original order. 
        size=len(unusedX)
        for i in range(size): # try all unusedX values
            x=unusedX.popleft() # pop from front
            if board.setNextQueen(x):       # try to set the queen on position x
                depthFirstRecursive(board)  # calls itself recursively to set next queen
            board.unsetLastQueen()          # undo the current queen to try other positions
            unusedX.append(x) # append at rear

def depthFirst(board):
    """ Depth First Search algorithm. """
    n=board.getN()
    if n+10>sys.getrecursionlimit():
        sys.setrecursionlimit(n+10) # set sufficient recursion depth
    depthFirstRecursive(board)

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Depth first search a N-Queens board.")
        print("usage: "+sys.argv[0]+" <N>")
        print("<N>       : size of the board")
    else:
        N=int(sys.argv[1])
        board=Board(N,randomizeUnusedX=False)
        depthFirst(board)
 
