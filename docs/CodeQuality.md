# Code Quality

## Modularity

> Wikipedia: Modular programming is a software design technique that
> emphasizes separating the functionality of a program into independent,
> interchangeable modules, such that each contains everything necessary
> to execute only one aspect of the desired functionality.

Separating in different modules makes software easier to understand,
change and test because you can think about each module on it own
without having to think about all the other software at the same
time.

An example of modularity in this project is the separation of
the Board class and the Diagonals class. The Board class only deals
with the X coordinate of the queens, whereas the Diagonals class keeps
track of the conflicts.

It is not always obvious to see how software can be separated in
independent modules but it will be worth your time and energy to
search for good separations even after software has already been
written. It just makes things much easier. If a module or function is
getting too big, try to find a way to split it in different parts.

### Counter example

The software would be more difficult to understand if the Board and
Diagonal would together form one big class. Function
[Board.setQueen()](https://github.com/bterwijn/NQueens/blob/master/NQueens/Board/Board.py#L83)
then might get intertwined with function
[Diagonals.addQueen()](https://github.com/bterwijn/NQueens/blob/master/NQueens/Board/Diagonals.py#L22).

## Abstraction

> Wikipedia: Abstraction is a technique for hiding complexity of
> computer systems. It works by establishing a level of simplicity on
> which a person interacts with the system, suppressing the more complex
> details below the current level.

Abstraction is another way to make software easier to understand. A
module or function has a particular purpose but when we use it we do
not care about the details required to fulfil it's purpose, we only
care about the result. These details are best hidden away in the
module or function behind an interface.

You could say the interface of a car is it's steering wheel, pedals
and gear shifter. When you drive your car you do not think about the
detais of how the fuel in the engine moves the pistons and through the
transmission rotates the wheels. An automatic car, that doesn't have a
gear shift, has a higher level of abstraction, and a self driving car
an even higher level as more and more detail are hidden away.

Abstraction in combination with modularity allows to have different
levels of abstraction in the software. Modules at the top only deal
with high level things and modules at the bottom only deal with the
details of a particular part of the software. All communication
between the modules goes via simplified interfaces that hide as much
detail as possible.

<img src="https://github.com/bterwijn/NQueens/blob/master/docs/AbstractionHierarchy.png">

An example of this hierarchy from top to bottom are the Algorithm,
Board and Diagonals classes.

### Counter example

Exposing the details of how the Diagonal class [keeps track of the
number of
conflicts](https://github.com/bterwijn/NQueens/blob/master/NQueens/Board/Board.py#L83)
to the Board class is not a good idea. If the Board class would use
these details it would get more complex and the chance of making
mistakes would be higher. In addition we would not be able to change
the conflict tracking of the Diagonal class without also having to
change the Board class. Instead the board class now simple calls the
[Diagonals.addQueen()](https://github.com/bterwijn/NQueens/blob/master/NQueens/Board/Board.py#L87)
function to add a queen and
[Diagonals.getNrConflicts()](https://github.com/bterwijn/NQueens/blob/master/NQueens/Board/Board.py#L126)
and
[Diagonals.getConflictQueens()](https://github.com/bterwijn/NQueens/blob/master/NQueens/Board/Board.py#L139)
to get the desired conflict information.

## Duplicate code

> Wikipedia: Duplicate code is a computer programming term for a
> sequence of source code that occurs more than once, either within a
> program or across different programs owned or maintained by the same
> entity.

Often it seems easiest to copy and paste some existing software and
adapt it to implement new functionality. This might work as a quick
fix but introduces unecessary lines of code that makes the software
more complex and is likely to cause complications when later changes
are required. In these cases it is better to identify what logic you
want to reuse and move that logic to a function that can then be
called from wherever the logic is wanted.

### Counter example

The Hill Climber algorithm wants to start with a randomized state. To
get to a randomized state we don't copy software from the Random class
but instead we [call a function of the Random class from within the
Hill Climber
class](https://github.com/bterwijn/NQueens/blob/master/NQueens/IterativeAlgorithms/HillClimber.py#L11)
to reuse it's logic.

## Redundant code

> Wikipedia: Redundant code is source code or compiled code in a
> computer program that is unnecessary, such as: recomputing a value
> that has previously been calculated and is still available, code that
> is never executed (known as unreachable code), code which is executed
> but has no external effect (e.g., does not change the output produced
> by a program; known as dead code).

### Example


## Style

> Wikipedia: Programming style is a set of rules or guidelines used when
> writing the source code for a computer program. It is often claimed
> that following a particular programming style will help programmers
> read and understand source code conforming to the style, and help to
> avoid introducing errors.

Choosing a style with your team and consistantly following it can
avoid errors and irritation. Some important style conventions you may
want to talk about are:

* naming of variables/functions/classes/modules: capitals, underscores
* using a '_' prefix for name of private/internal details of classes
* how to write comments and documentation

### Example

The conventions used in this project are:

* classes start with a capital, functions and variables with a small case character
* a '_' prefix is used for private/internal details of a class
* inline comments are use to clarify otherwise difficult logic
* we use Python Docstring to write documentation for each class and function

As can be seen in for example the
[Board](https://github.com/bterwijn/NQueens/blob/master/NQueens/Board/Board.py)
class.

## Documentation

> Wikipedia: Software documentation is written text or illustration that
> accompanies computer software or is embedded in the source code. It
> either explains how it operates or how to use it, and may mean
> different things to people in different roles.

Write sufficient documentation so that people can understand your
source code. First so that your team members can understand it so you
don't have to repeatedly explain it before they can build on top of
your contribution. Secondly so that the people grading your source
code can understand it. Software that is hard to understand is likely
to get a lower grade than software that is easy to understand.
