"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid.
The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.
But we will not be playing this game. You will be the referee for this games results. You are given a result of a game and you must 
determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X" if the X-player wins and "O"
if the O-player wins. If the game is a draw, return "D".

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.

Example:
checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"
checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"
"""

#first method
LINES = (((0,0),(0,1),(0,2)),
    ((1,0),(1,1),(1,2)),
    ((2,0),(2,1),(2,2)),
    ((0,0),(1,0),(2,0)),
    ((0,1),(1,1),(2,1)),
    ((0,2),(1,2),(2,2)),
    ((0,0),(1,1),(2,2)),
    ((0,2),(1,1),(2,0)))

def xs_os_referee(game_result):
    for line in LINES:
        res = judge([game_result[x][y] for x,y in line])
        if res == 'X' or res == 'O':
            return res
    return 'D'

def judge(data):
    if data.count('X') == 3 or data.count('O') == 3:
        return data[0]
    else:
        return 'D'
        
#second method
def os_xs_referee(game_result):
    rows = (
        list(board) +                                # normal rows
        list(zip(*board)) +                          # columns
        [(board[0][0], board[1][1], board[2][2])] +  # first diagonal
        [(board[0][2], board[1][1], board[2][0])]    # second diagonal
    )
    for row in rows:
        row = ''.join(row)
        if row == 'XXX':
            return 'X'
        if row == 'OOO':
            return 'O'
    return 'D'
    
if __name__ == '__main__':
    assert os_xs_referee([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert os_xs_referee([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert os_xs_referee([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert os_xs_referee([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
