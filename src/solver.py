import setup.initialise as init
import sudoku.rules as rules
import os


def main():
    x = input("please enter a file name. If you wish to create a new file,\nenter the name of the file you would like to create. ")
    if not os.path.isfile(x+".txt"):
        f = open(x + '.txt', 'w')
        board = init.setup_board()
        blank = init.visualise_board(board)
        f.write(blank)
        f.close()
        input("I have created a file called " + x + " on the filesytem. \nPlease enter your sudoku in this file and press enter.")

    f = open(x+".txt")
    sudoku = f.read()
    print(sudoku)
    input("I am going to use this sudoku, hit enter to continue.")

    board = init.parse_board(sudoku)
    provided = init.provided_points(board)
    rules.run_event_loop(board, provided)
    print()
    print(init.visualise_board(board))
    solved = init.validate_board(board)
    print(init.get_message(solved))


sample = []
easy = []
medium = []
hard = []
expert = []
good_grief = []




# easy
easy.append("")
easy[0] += " 3 5 . | 6 . 2 | . . 4\n"
easy[0] += " . . 7 | . 4 . | . 1 3\n"
easy[0] += " . 6 9 | 8 3 1 | . . 7\n"
easy[0] += " ---------------------\n"
easy[0] += " 5 . 3 | . . . | . 9 6\n"
easy[0] += " . . . | 3 . . | 7 4 5\n"
easy[0] += " 9 4 6 | . . . | 8 . .\n"
easy[0] += " ---------------------\n"
easy[0] += " 6 9 2 | 4 . . | . . 8\n"
easy[0] += " 8 . . | 7 . 3 | . . .\n"
easy[0] += " . . 4 | . 2 . | . . 1"


medium.append("")
medium[0] += " . . . | . . 2 | 6 7 .\n"
medium[0] += " 8 6 3 | . . . | . . 5\n"
medium[0] += " . . 7 | 5 . 8 | . . .\n"
medium[0] += " ---------------------\n"
medium[0] += " . . . | . 8 . | 4 9 7\n"
medium[0] += " . 7 . | . . . | . 8 .\n"
medium[0] += " . 5 . | . 3 . | 1 . 6\n"
medium[0] += " ---------------------\n"
medium[0] += " . . 1 | 9 . 6 | . . .\n"
medium[0] += " 4 3 . | . 5 . | . 6 .\n"
medium[0] += " . 2 . | . 7 . | . 1 ."

# hard
hard.append("")
hard[0] += " 6 4 . | . . 1 | 7 . 2\n"
hard[0] += " 8 . 7 | . . 9 | . 1 .\n"
hard[0] += " . . 1 | . 7 . | . . 9\n"
hard[0] += " ---------------------\n"
hard[0] += " . . 6 | . 5 7 | . . .\n"
hard[0] += " 2 . . | . . . | . . .\n"
hard[0] += " . 5 . | 2 8 . | . . .\n"
hard[0] += " ---------------------\n"
hard[0] += " . 6 . | 4 . 5 | . . 3\n"
hard[0] += " . 8 . | . 6 . | . . 4\n"
hard[0] += " . . . | . . . | 1 . 5"

# expert
expert.append("")
expert[0] += " . . 9 | . 4 7 | . . .\n"
expert[0] += " . . . | . . . | 1 . 6\n"
expert[0] += " . 8 . | . 2 . | . . .\n"
expert[0] += " ---------------------\n"
expert[0] += " 8 . 1 | . . 3 | . . .\n"
expert[0] += " . 7 3 | . . . | . . .\n"
expert[0] += " . . . | . . . | . 5 4\n"
expert[0] += " ---------------------\n"
expert[0] += " . . . | 2 . . | . . 1\n"
expert[0] += " 3 . . | . . 9 | . 7 .\n"
expert[0] += " . 9 . | 8 . 6 | . 4 ."

# incredibly hard
good_grief.append("")
good_grief[0] += " . . . | 1 . . | 6 . 5\n"
good_grief[0] += " . . . | . . 6 | . . .\n"
good_grief[0] += " . . 2 | 5 . 9 | . 3 .\n"
good_grief[0] += " ---------------------\n"
good_grief[0] += " 9 . . | . 7 . | . 6 .\n"
good_grief[0] += " 2 . . | . 3 . | 1 . .\n"
good_grief[0] += " . . . | . . . | 3 . 2\n"
good_grief[0] += " ---------------------\n"
good_grief[0] += " 7 . . | . . . | . . .\n"
good_grief[0] += " . 4 . | . . . | . 2 .\n"
good_grief[0] += " . . 1 | . 6 5 | 4 . ."

if __name__ == "__main__":
    main()
