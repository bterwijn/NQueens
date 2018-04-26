
from NQueens.Board.Board import *

class Random:
    
    def randomize(board,nrTries=500):
        """ Randomize a board. For each queen go over the next 'nrTries' elements 
        in _unusedX and use the first x that results in the fewest possible conflicts."""
        n=board.getN()
        while not board.allQueensSet():
            if board.nrUnusedX()%10000==0: # print remaining unplaced queens to indicate progress
                print("queens to be placed:",board.nrUnusedX())
            x=Random.getBestXForNextQueen(board,nrTries)
            board.setNextQueen(x)
            
    def getBestXForNextQueen(board,nrTries):
        """ Return x position for the next queen. Go over the next 'nrTries' elements 
        in _unusedX and return the first x that results in the fewest possible conflicts. """
        if nrTries>board.nrUnusedX():
            nrTries=board.nrUnusedX()
        unusedX=board.getUnusedX() # Get and change board private member, bit ugly but fast.
        startNrConflicts=board.getNrConflicts()
        bestNrConflicts=sys.maxsize
        bestX=-1
        tried=deque()
        for i in range(nrTries):
            x=unusedX.popleft() # remove arbitrary element from deque but,
            tried.append(x)     # remember it to put it back later
            board.setNextQueen(x)
            nrConflicts=board.getNrConflicts()
            board.unsetLastQueen()
            if nrConflicts<bestNrConflicts:
                bestNrConflicts=nrConflicts
                bestX=x
                if nrConflicts==startNrConflicts: # zero additional conflict, can't improve so break
                    break
        while len(tried)>0: # put back the tried elements minus x
            i=tried.popleft()
            if not i==bestX:
                unusedX.append(i)
        return bestX
    
if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Randomize a N-Queens board.")
        print("usage: "+sys.argv[0]+" <N> [<filename>]")
        print("<N>       : size of the board")
        print("<filename>: save solution to file, or print solution when filename is 'p'")
    else:
        N=int(sys.argv[1])
        board=Board(N,randomizeUnusedX=True)
        Random.randomize(board)
        if len(sys.argv)>2:
            if sys.argv[2]=="p":
                print(board.toString())
            else:
                board.saveQueensXs(sys.argv[2])
