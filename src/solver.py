import setup.board as init
import sudoku.rules as rules
import os
import time

def main():
    x = ''
    while x != 'no':
        x = input("\nplease enter a file name. If you wish to create a new file,\nenter the name of the file you would like to create. ")
        if not os.path.isfile(x+".txt"):
            f = open(x + '.txt', 'w')
            board = init.setup_board()
            blank = init.visualise_board(board)
            f.write(blank)
            f.close()
            input("I have created a file called " + x + " on the filesytem. \n Please enter your sudoku in this file and press enter.")

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
        x = input("\nwould you like me to solve another sudoku?(yes/no) ")
    time.sleep(3)

if __name__ == "__main__":
    main()
