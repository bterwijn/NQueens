
class Diagonals:
    """Represents all diagonals of a board in a particular direction, either top-right or top-left.    
    Attributes:
    _n              -- the size of the board (the board is square)
    _diagonals      -- a list where each element is a set of queens that are on a particular diagonal
    _conflictQueens -- set of conflicting queens over all diagonals
    _nrConflicts    -- number of conflicts, 2 queens on 1 diogonal counts as 1 conflict, 3 queens as 2, etc.
    """
    def __init__(self,n):
        """ Initialize the diagonals for a board of size n (the board is square). """
        self._n=n
        self._diagonals=[set([]) for i in range(n*2-1)]
        self._conflictQueens=set([])
        self._nrConflicts=0
        
    def _index(self,x,y):
        """ Compute diagonal index for queen at coordinate (x,y). 
            This function is to be overridden by subclasses. """
        return -1; # invalid index as placeholder
        
    def addQueen(self,x,y):
        """ Add queen at coordinate (x,y) to the diagonals and update conflicts. 
        Return True when adding didn't result in a conflict """
        i=self._index(x,y)
        length=len(self._diagonals[i])
        if length==1: # if conflict with 1 queen then add first queen too
            q1=next(iter(self._diagonals[i]))
            self._conflictQueens.add(q1)
        self._diagonals[i].add(y)
        length=len(self._diagonals[i])
        if length>1:
            self._conflictQueens.add(y)
            self._nrConflicts+=1
        return len(self._diagonals[i])==1 # True if only one queen is on this diagonal

    def removeQueen(self,x,y):
        """ Remove queen at coordinate (x,y) to the diagonals and update conflicts. """
        i=self._index(x,y)
        self._diagonals[i].remove(y)
        length=len(self._diagonals[i])
        if length>0:
            self._nrConflicts-=1
            self._conflictQueens.remove(y)
        if length==1: # if conflict with 1 queen then remove first queen too
            q1=next(iter(self._diagonals[i]))
            self._conflictQueens.remove(q1)

    def getConflictQueens(self):
        """ Get the queens that are in conflict. """
        return self._conflictQueens

    def getNrConflicts(self):
        """ Get the number of conflicts. """
        return self._nrConflicts
        
    def toString(self):
        """ Return a string representation of the Diagonals class. """
        ret=str(self._conflictQueens)+": "
        for i in self._diagonals:
            ret+=str(i)+" "
        return ret

class DiagonalsTopLeft(Diagonals):
    """ Represents all diagonals of a board in top-left direction by inheriting from Diagonals class. """
    def __init__(self,n):
        print("  initializing diagonals Top Left")
        Diagonals.__init__(self,n) # initialize super class

    def _index(self,x,y):
        """ Computes diagonal index for queen at coordinate (x,y) for Top-Left diagonals. """
        return y+x;
    
class DiagonalsTopRight(Diagonals):
    """ Represents all diagonals of a board in top-right direction by inheriting from Diagonals class. """
    def __init__(self,n):
        print("  initializing diagonals Top Right")
        Diagonals.__init__(self,n) # initialize super class

    def _index(self,x,y):
        """ Computes diagonal index for queen at coordinate (x,y) for Top-Right diagonals. """
        return self._n-1-y+x;
