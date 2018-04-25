# N-Queens

Solver for the N-Queens problem: Place N queens on a chessboard of
size NxN such that no queen threatens another one.

<img src="https://github.com/bterwijn/NQueens/docs/solution.png" align="left" height="400" >

## Files

```
NQueens/
NQueens/NQueens
NQueens/NQueens/Board
NQueens/NQueens/ConstructiveAlgorithms
NQueens/NQueens/IterativeAlgorithms
```

## Usage

```
# Randomly generate a chessboard of size 50 with few conflicts.
python3 -m NQueens.ConstructiveAlgorithms.Random 50 p

# Generate all possible chessboards of size 12 with NO conflicts.
python3 -m NQueens.ConstructiveAlgorithms.DepthFirst 12

# Randomly generate a chessboard of size 10000 and use a hill climber
# to fix conflicts, save the result to file 'solution.txt'.
python3 -m NQueens.IterativeAlgorithms.HillClimber 10000 solution.txt
```

## Authors

* **Bas Terwijn**

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* etc
