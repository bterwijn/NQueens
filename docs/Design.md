# Design

A design helps us to communicate and think our choices through before
we deal with the implementation details of the programming
language. The design consists of 3 different algorithms for which we
write pseudo code to get a idea how each could be implemented:

* Random
* Depth First
* Hill Climber

## Random

The Random algorithm will for the current queen try many random x
coordinates from the unusedX set and will use the x coordinate that
results in the fewest number of conflicts. Then it will repeat this
for the next queen until all queens are set. This may produce a
solution with conflicts.

```
randomize( board )
   while not board.allQueensSet()
      x = getBestXForNextQUeen( board , 500 )
      board.setNextQueen(x)
   print( "SOLUTION: " , board )

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
the next queen until all queens are set. This will produce all
possible solutions with no conflicts.

```
depthFirst( board )
    if board.allQueensSet()
        print( "SOLUTION: " , board )
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
queens in the hope of removing a conflict. If the number of conficts
gets worse it will swap them back. This is repeated until all
conflicts are resolved.

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
   print( "SOLUTION: " , board )
```

## Classes

Based on the pseudo code above we choose to decompose the software in
the following classes:

* Random, the random algorithm
* DepthFirst, the depth-first algorithm
* HillClimber, the hill-climber algorithm
* Board, represents the board and positions of queens
* DiagonalsTopLeft, represents queens and conflicts on the top-left diagonals
* DiagonalsTopRight, represents queens and conflicts on the top-right diagonals
* Diagonals, logic for efficient conflict checking

The relation between these classes can be represented in an informal
UML class diagram with the algorithms in pink and the representation
of the state (datastructure) in blue.

<img src="https://github.com/bterwijn/NQueens/blob/master/docs/umletino.png">

For which the legend is:

<img src="https://github.com/bterwijn/NQueens/blob/master/docs/umlLegend.png">

Having used the design to plan the high-level structure of the source
code, we can now start writing it and deal with all the implementation
details. We can simply go back and change the design when we learn
more about the problem and discover it should be changed.