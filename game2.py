board = [" " for x in range(9)]

def print_board():
    row1 = "|{}| |{}| |{}| ".format(board[0],board[1],board[2],board[3])
    row1 = "|{}| |{}| |{}| ".format(board[4],board[5],board[2],board[6])
    row1 = "|{}| |{}| |{}| ".format(board[7],board[1],board[8],board[9])


print(row1)
print(row2)
print(row3)

print_board( )
