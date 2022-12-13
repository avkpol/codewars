# DESCRIPTION:
# Knight vs King
# If you are not familiar with chess game you can learn more Here .
#
# Here is the chess board (rows, denoted by numbers, are called ranks, columns, denoted by a letter, are called files):
#
# alt text
#
# You put a Knight and a King in the board.
#
# Complete the method that tell us which one can capture the other one.
#
# You are provided with two object array; each contains an integer (the rank, first item) and a string/char (the file, second item) to show the position of the pieces in the chess board.
#
# Return:
#
# "Knight" if the knight is putting the king in check,
# "King" if the king is attacking the knight
# "None" if none of the above occur
# Example:
#
# knight = [7, "B"], king = [6, "C"]  ---> "King"
# Check the test cases and Happy coding :)

def knight_vs_king (knight_position, king_position):
    #added "fake fields" f1, f2, f3, f4" to overcome "list out of range "error
    columns = ['f1','f2','A','B','C','D','E','F','G','H','f3','f4']
    # define x, y coordinates
    x = (list(knight_position))[0]
    y = (list(knight_position))[1]
    # find proper column letter
    y = columns.index(y)
    # define moves reletively a cell
    x_up = x + 1
    x_dw = x - 1
    x_upup = x + 2
    x_dwdw = x - 2
    y_ct = columns[y]
    y_lf = columns[y - 1]
    y_rt = columns[y + 1]
    y_lflf = columns[y - 2]
    y_rtrt = columns[y + 2]
    # define possible king moves
    kg_pos = ([x_up,y_lf], [x_up, y_rt], [x_up, y_ct], [x_dw, y_lf],
    [x_dw, y_rt], [x_dw, y_ct], [x, y_lf], [x, y_rt])
    # define possible knight moves
    kn_pos = ([x_upup, y_lf], [x_upup, y_rt], [x_up, y_lflf],
    [x_up, y_rtrt], [x_dwdw, y_lf], [x_dwdw, y_rt],
    [x_dw, y_lflf], [x_dw, y_rtrt])
    # loop through coordinates
    knight_coord = [i for i in kg_pos]
    king_coord = [i for i in kn_pos]
    if  list(king_position) in knight_coord:
        return 'King'
    elif list(king_position) in king_coord:
        return 'Knight'
    else:
        return "None"