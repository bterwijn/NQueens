
from NQueens.Board.Board import *
from NQueens.ConstructiveAlgorithms.Random import *

class HillClimber:
    
    def hillClimber(board,maxSteps=100000):
        """ Hill climb a board with all queens set until all conflicts are removed. Each steps 
        select a conflict queen and swaps its x coordinate with a random other queen. Stop 
        when after 'maxSteps' (default: 1000000) step conflicts remain. """
        nrConflictsRemaining=board.getNrConflicts()
        print("nrConflicts after randomization:",nrConflictsRemaining)
        step=0
        while nrConflictsRemaining>0:
            nrConflicts1=board.getNrConflicts()
            if nrConflicts1<nrConflictsRemaining: 
                nrConflictsRemaining=nrConflicts1
                print("nrConflictsRemaining:",nrConflictsRemaining,
                      " after ",step," steps") # print remaining conflicts to indicate progress
            if nrConflicts1==0: # check if we are done
                break 
            q1=board.getRandomConflictQueen() # random conflict queen
            if q1>=0: # if q1 is valid
                q2=random.randint(0,board.getN()-1) # random normal queen
                board.swap(q1,q2) # swap the thw queens, hoping to get less conflicts
                #print(board.toString())
                nrConflicts2=board.getNrConflicts()
                if nrConflicts2>nrConflicts1: # if more conflicts then 
                    board.swap(q1,q2)         # undo the swap by swapping again
            step+=1
            if step>maxSteps:
                return False
        return True

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Hill Climb a N-Queens board.")
        print("usage: "+sys.argv[0]+" <N> [<filename>]")
        print("<N>       : size of the board")
        print("<filename>: save solution to file, or print solution when filename is 'p'")
    else:
        N=int(sys.argv[1])
        board=Board(N,randomizeUnusedX=True)
        Random.randomize(board)
        if HillClimber.hillClimber(board): # if all conflicts solved
            if len(sys.argv)>2:
                if sys.argv[2]=="p":
                    print(board.toString())
                else:
                    board.saveQueensXs(sys.argv[2])
