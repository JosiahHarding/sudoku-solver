# Sudoku Solver
## A program that solves sudokus puzzles

### Getting set up
Note that you need to run the solver using Python 3 installed and working. You can verify this by running the command:

`python --version`

If this shows the version as being Python 2, you may have Python 3 installed under the name python3. You can check this by running the command:

`python3 --version`

If neither of these work, you will need to validate your python installation. Please check out [this website](https://realpython.com/installing-python/)

### Installing Sudoku Solver
When you extract the zip file you should see `solver.py` in the directory next to this readme. The program is now installed.

### Running the program
Open up a terminal window and navigate to the location of the `solver.py` file. This can be accessed with the following code:

`cd ~/projects/scratch/sudoku-solver`

From here simply execute the command:

`python3 solver.py`

The program will prompt you to enter a name for your sudoku like this:

> please enter a file name. If you wish to create a new file,
> enter the name of the file you would like to create.

The solver ships with 5 sudokus of different difficulty levels. These are called:
- easy
- medium
- hard
- expert
- good grief

You can use one of these puzzles to try the program without having a sudoku of your own. Or you can get a sudoku from [sudoku.com](http://sudoku.com)

Once you've given your sudoku a name or used one of the ones above, the solver will try to find that file on the file system. If it can't it will create a new file called `<your name>.txt` and the program will ask you to enter your sudoku starting position into the file like this:

> I have created a file called `<your name>.txt` on the filesytem. 
> Please enter your sudoku in this file and press enter.

Open the file in your favourite text editor and enter your sudoku starting position numbers by overwriting the `.` characters in the correct locations with a number 1-9. When you are done save the file and come back to the solver program screen to hit enter per the instructions. The program will print the starting position out to the screen for you to confirm:

```
. . . | 1 . . | 6 . 5
 . . . | . . 6 | . . .
 . . 2 | 5 . 9 | . 3 .
 ---------------------
 9 . . | . 7 . | . 6 .
 2 . . | . 3 . | 1 . .
 . . . | . . . | 3 . 2
 ---------------------
 7 . . | . . . | . . .
 . 4 . | . . . | . 2 .
 . . 1 | . 6 5 | 4 . .
```
> I am going to use this sudoku, hit enter to continue.

Once you hit enter the program will cycle through the points that have been updated and run the rules. Each changed point is an "event". The program will tell you how many events it processed, and then show you how far it could go to solve the sudoku:

> processed 131 events

```
 4 7 9 | 1 2 3 | 6 8 5
 5 3 8 | 7 4 6 | 2 1 9
 1 6 2 | 5 8 9 | 7 3 4
 ---------------------
 9 1 3 | 4 7 2 | 5 6 8
 2 5 4 | 6 3 8 | 1 9 7
 6 8 7 | 9 5 1 | 3 4 2
 ---------------------
 7 2 6 | 3 9 4 | 8 5 1
 3 4 5 | 8 1 7 | 9 2 6
 8 9 1 | 2 6 5 | 4 7 3
```
> I solved it!

At this point you can choose to solve another puzzle or to quit.

---

*Note: right now the solver can solve 95% of sudoku puzzles. There are some very difficult rules for solving sudoku puzzles that the program doesn't support. These are [the X wing rule, the X-Y wing rule, the swordfish rule and unique rectangle](https://www.learn-sudoku.com/advanced-techniques.html) rules.*
