
from NQueens.Board.Board import *

def randomize(board,tries=500):
    """ Randomize a board. For each queen go over the next 'tries' elements 
    in _unusedX and use the first x that results in the fewest possible conflicts."""
    n=board.getN()
    while not board.isDone():
        if board.nrUnusedX()%10000==0: # print remaining unplaced queens to indicate progress
            print("queens to be placed:",board.nrUnusedX())
        x=board.sampleBestXForNextQueen(tries)
        board.setNextQueen(x)

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Randomize a N-Queens board.")
        print("usage: "+sys.argv[0]+" <N> [<filename>]")
        print("<N>       : size of the board")
        print("<filename>: save solution to file, or print solution when filename is 'p'")
    else:
        N=int(sys.argv[1])
        board=Board(N,randomizeUnusedX=True)
        randomize(board)
        if len(sys.argv)>2:
            if sys.argv[2]=="p":
                print(board.toString())
            else:
                board.saveQueensXs(sys.argv[2])
