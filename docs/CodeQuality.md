# Code Quality

## Modularity

> Wikipedia: Modular programming is a software design technique that
> emphasizes separating the functionality of a program into independent,
> interchangeable modules, such that each contains everything necessary
> to execute only one aspect of the desired functionality.

Separating in different modules makes software easier to understand,
change and test because you can think about each module on it own
without having to think about all the other software at the same
time. An example of modularity in this project is the separation of
the Board class and the Diagonal class. The Board class only deals
with the X coordinate of the queens, whereas the Diagonal class keeps
track of the conflicts. It is not always obvious to see how software
can be separated in independent modules but it will be worth your time
and energy to search for good separations even after software has
already been written. It just makes things much easier. If a module or
function is getting too big, try to find a way to split it in different
parts.

### Counter example

The software would be more difficult to understand
if the Board and Diagonal would together form one class.

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
levels of abstraction in the software. Module at the top only deal
with high level things and modules at the bottom only deal with the
details of a particular part of the software. All communication
between the modules goes via simplified interfaces.

<img src="https://github.com/bterwijn/NQueens/blob/master/docs/AbstractionHierarchy.png">

### Counter example

Exposing the details about how the Diagonal class keeps track of the
number of conflicts to the Random algorithm is not a good idea. If the
random class would use these details it would get more complex and we
would not be able to change the Diagonal class without also having to
change the Random class.

## Duplicate code

> Wikipedia: Duplicate code is a computer programming term for a
> sequence of source code that occurs more than once, either within a
> program or across different programs owned or maintained by the same
> entity.

## Redundant code

> Wikipedia: Redundant code is source code or compiled code in a
> computer program that is unnecessary, such as: recomputing a value
> that has previously been calculated and is still available, code that
> is never executed (known as unreachable code), code which is executed
> but has no external effect (e.g., does not change the output produced
> by a program; known as dead code).

## Style

> Wikipedia: Programming style is a set of rules or guidelines used when
> writing the source code for a computer program. It is often claimed
> that following a particular programming style will help programmers
> read and understand source code conforming to the style, and help to
> avoid introducing errors.

## Documentation

> Wikipedia: Software documentation is written text or illustration that
> accompanies computer software or is embedded in the source code. It
> either explains how it operates or how to use it, and may mean
> different things to people in different roles.