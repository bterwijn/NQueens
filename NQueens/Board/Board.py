import sys,os
import random
from collections import deque

from NQueens.Board.Diagonals import *

class Board:
    """Represents a chess board for the N-Queen problem. Queen number Y
    will always be placed on row number Y, so that for each queen only 
    the X variable has to be chosen. The X variables are chosen from the 
    '_unusedX' set so that conflicts can only occur on the diagonals.
    
    Attributes:
    _n         -- the size of the board (the board is square)
    _queensX   -- a list of x coordinates of queens (initially empty)
    _unusedX   -- a deque of x coordinates that are not yet used by queens
    _diagTL    -- all diagonals in the top-left direction
    _diagTR    -- all diagonals in the top-right direction
    """
    def __init__(self,n,randomizeUnusedX=False):
        """ Initialize board
        Arguments:
        n                -- the size size of the board (the board is square)
        randomizeUnusedX -- indicates of the '_unusedX' set is randomized or not (default: False)
        """
        print("initializing Board")
        self._n=n
        self.reset(randomizeUnusedX)
        
    def reset(self,randomizeUnusedX):
        """ Clear all queens from the board and restores _unusedX and diagonals accordingly. 
        randomize -- indicates of the '_unusedX' set is randomized or not (default: False)
        """
        self._queensX=[]
        if not randomizeUnusedX:
            self._unusedX=deque(range(self._n))
        else:
            unusedXList=list(range(self._n))
            random.shuffle(unusedXList)
            self._unusedX=deque(unusedXList)
        self._diagTR=DiagonalsTopRight(self._n)
        self._diagTL=DiagonalsTopLeft(self._n)
        
    def getN(self):
        """ Get the size of the board. """
        return self._n;

    def nrQueensSet(self):
        """ Get the number of queens set on the board. """
        return len(self._queensX)

    def nrUnusedX(self):
        """ Get the number of unused X coordinates of the board. """
        return len(self._unusedX)

    def getUnusedX(self):
        """ Get the unused X coordinates. """
        return self._unusedX
    
    def toString(self):
        """ Return a string representation of the board """
        ret=""
        #ret+="_unusedX: "+str(self._unusedX)+os.linesep
        ret+="_queensX: "+str(self._queensX)+os.linesep
        ret+=self.queensToString()
        #ret+="diagTR:"+self._diagTR.toString()+os.linesep
        #ret+="diagTL:"+self._diagTL.toString()+os.linesep
        ret+="nrConflicts:"+str(self.getNrConflicts())+os.linesep
        return ret

    def queensToString(self):
        """ Return a string representation of all queens on the board. """
        ret=""
        for y in range(self._n):
            if y>=self.nrQueensSet(): # if queen is not set print empty line
                ret+=". "*self._n
            else:                     # else print 'Q' on right X coordinate 
                x=self._queensX[y];
                ret+=". "*x+"Q "+". "*(self._n-x-1);
            ret+=os.linesep
        return ret

    def setQueen(self,q,x):
        """ Set queen 'q' to X coordinate 'x'. Return False if a conflict 
        is created, True otherwise. """
        self._queensX[q]=x # set queen to x
        noConflictTR=self._diagTR.addQueen(x,q)
        noConflictTL=self._diagTL.addQueen(x,q)
        return noConflictTR and noConflictTL

    def setNextQueen(self,x):
        """ Set the next queen to X coordinate 'x'. Return False if a conflict 
        is created, True otherwise. """
        self._queensX.append(-1) # append new element to queensX
        return self.setQueen(self.nrQueensSet()-1,x) # use setQueen() to set its value

    def unsetQueen(self,q):
        """ Unset queen 'q' from X coordinate 'x'. Return the x coordinate. """
        x=self._queensX[q]  # remove from last queen
        self._queensX[q]=-1 # invalid value
        self._diagTR.removeQueen(x,q)
        self._diagTL.removeQueen(x,q)
        return x
    
    def unsetLastQueen(self):
        """ Unset the last queen. Return its x coordinate. """
        x=self.unsetQueen(self.nrQueensSet()-1)
        self._queensX.pop() # remove last from queensX
        return x
    
    def allQueensSet(self):
        """ Check if all queens are on the board. """
        return self.nrQueensSet()==self._n

    def getDiagonalsTopLeft(self):
        """ Get the Diagonals Top-Left object. """
        return self._diagTL

    def getDiagonalsTopRight(self):
        """ Get the Diagonals Top-Right object. """
        return self._diagTR
    
    def getNrConflicts(self):
        """ Get the number of conflicts of the board. 
        This is the sum on conflicts of both diagonal objects. """
        return self._diagTR.getNrConflicts()+self._diagTL.getNrConflicts()

    def swap(self,q1,q2):
        """ Swap the X coordinate of queen 'q1' and 'q2'. """
        if q1!=q2: # do not swap with itself
            x1=self.unsetQueen(q1)
            x2=self.unsetQueen(q2)
            self.setQueen(q1,x2)
            self.setQueen(q2,x1)

    def getRandomConflictQueen(self):
        """ Get a random conflict queen from the top-left or top-right diagonals """
        c=[]
        c1=self._diagTL.getConflictQueens()
        if len(c1)>0:
            c.append(c1)
        c2=self._diagTR.getConflictQueens()
        if len(c2)>0:
            c.append(c2)
        q=-1 # invalid index to indicate there are no conflict queens
        if len(c)>0:
            #print("conflicts: ",c1,c2)
            conflictSet=random.sample(c,1)[0] # choose between top-left or top-right if both have conflicts
            q=random.sample(conflictSet,1)[0] # random sample one from the set of conflicts
        return q
    
    def saveQueensXs(self,filename):
        """ Save all X coordinates of the queens to 'filename'. 
        This represents a solutions to the N-Queen probleem. """
        myFile = open(filename, 'w')
        for i in self._queensX:
            myFile.write("%s " % i)
