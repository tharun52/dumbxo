"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    n = 9-board.count(EMPTY)
    if n%2==0:
        return X
    else:
        return O
    """
    xcount=0
    ocount=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                xcount+=1
            elif board[i][j]==O:
                ocount+=1
    if xcount<ocount:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    s=set()
    for i in range(len(board)):
        for j in range(len(board[1])):
            if board[i][j]==EMPTY:
                s.add((i,j))
    return s

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action!!!")
    else:
        board1 = copy.deepcopy(board)
        board1[action[0]][action[1]] = player(board)
        return board1

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                return None
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                return None
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
        else:
            return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in [X, O]:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j]==None:
                    return False
        return True
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board)==X:
            value, move = minval(board)
            return move
        else:
            value, move = maxval(board)
            return move
            
def maxval(board):
    v = float('-inf') 
    move = None
    if terminal(board):
        return utility(board), None
    for action in actions(board):
        #v = max(v, minval(result(borad, action)))
        aux, act = minval(result(board, action))
        if aux>v:
            v = aux
            move = action
            if v==1:
                return v, move
    return v, move

def minval(board):
    v = float('inf') 
    move = None
    if terminal(board):
        return utility(board), None
    for action in actions(board):
        #v = max(v, minval(result(borad, action)))
        aux, act = maxval(result(board, action))
        if aux<v:
            v = aux
            move = action
            if v==-1:
                return v, move
    return v, move
