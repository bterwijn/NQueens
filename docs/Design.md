# Design

We make a design for our software. A design helps us to communicate
and think our choices through before we deal with the implementation
details of the programming language.

We choose to use 3 algorithms for which we write pseudo code:

* Random
* Depth First
* Hill Climber


## Random

The Random algorithm will for the current queen try many random x
coordinates from the unusedX set and will use the x coordinate that
resuts in the fewest number of conflicts. Then it will repeat this for
the next queen until all queens are set.

```
randomize( board )
   while not board.allQueensSet()
      x = getBestXForNextQUeen(board,500)
      board.setNextQueen(x)

getBestXForNextQUeen( board , nrTries )
    bestX = -1
    bestNrConflicts = infinite
    try 'nrTries' remaining x values of board.unusedX
        board.setNextQueen( x )
        if board.getNrConflicts() < bestNrConflicts
            bestX = x
            bestNrConflicts = board.getNrConflicts()
        board.unsetLastQueen()
    return bestX
```

## Depth First

The Depth First algorithm will for the current queen try each x from
the unusedX set. If no conflict occurs it will move on recursively to
the next queen until all queens are set.

```
depthFirst( board )
    if board.isDone()
        print( "solution: ", board )
    else
        try all remaining x values in board.unusedX
            board.setNextQueen( x )
            if board.getNrConflicts() == 0
                depthFirst( board )
            board.unsetLastQueen()
```

## Hill Climber

The Hill Climber algorithm starts with a randomized board. It will
randomly select a queen that causes a conflict and randomly select an
arbitrary queen. It will then swap the X coordinates of these two
queens. If the number of conficts gets worse it will swap them
back. This is repeated until all conflicts are resolved.

```
hillClimber( board )
   randomize( board )
   while board.getNrConflicts() > 0
       nrConflicts1 = board.getNrConflicts()
       q1 = board.getRandomConflictQueen()
       q2 = board.getRandomQueen()
       board.swap( q1 , q2 )
       nrConflicts2 = board.getNrConflicts()
       if nrConflicts2 > nrConflicts1
           board.swap( q1 , q2 )
```
