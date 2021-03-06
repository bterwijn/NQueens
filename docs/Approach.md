# Approach

A queen on a chessboard threatens all positions on its horizontal,
vertical and both diagonal lines as indicated in blue.
<img src="https://github.com/bterwijn/NQueens/blob/master/docs/1queen.png" height="400" >

If a queen threatens a positions where another queen is on we speak of
a conflict.
<img src="https://github.com/bterwijn/NQueens/blob/master/docs/2queensConflicts.png" height="400" >

The aim is to find a position for all queens that doesn't result in
any conflict. To simplify things we assign a unique Y coordinate to
each queen. This rules out any horizontal conflicts without loss of
generality.
<img src="https://github.com/bterwijn/NQueens/blob/master/docs/fixedYs.png"
height="400" >

To simplify further we let each queen select its X coordinate from a
set we call 'unusedX', from which each coordinate can be used only
once. As a result we rule out any vertical conflicts too.

<img src="https://github.com/bterwijn/NQueens/blob/master/docs/unusedXExample.png" height="400" >

This way we reduce the state-space to all possible assignments of n
queens to n Xs:
```
   state-space(n) = n!
```

Conflicts can now only occur on either the 'Top-Left' or 'Top-Right'
diagonals.
<img src="https://github.com/bterwijn/NQueens/blob/master/docs/Diagonals.png" height="400" >
