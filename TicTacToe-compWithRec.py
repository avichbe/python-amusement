"""
author: avichay ben lulu 301088670
tic tac toe with evaluation method that choose wisely for the computer and write the winners in DB
i create three main Types:
Board, Game, Player->Computer
Game co't create instance of Board and run the game with play().
"""
import pandas as pd
import random
from random import choice


class Board:

    def __init__(self, from_board=None):
        self.board = (from_board or [' '] * 9).copy()

    # print the array
    def to_string(self):
        return ' {}|{}|{}\n {}|{}|{} \n {}|{}|{}'.format(*self.board)

    # deep clone
    def clone(self):
        return Board(self.board)

    """
        input: self.
        output: mark of computer.
         goal: make random move.
    """

    def random_move(self):
        # because only the computer can do random move - set mark as the computer
        mark = 'o'
        # return random legal options - than use choice to randomly choose one from them
        random_options = [i for i in range(9) if self.board[i] == ' ']
        legal_random_move = choice(random_options)
        self.board[legal_random_move] = mark
        return self.victory(mark)

    """
        input: mark of player, location on board.
        output: mark of player.
        goal: make move on the board with given player mark and location.
    """

    def move(self, mark, location):
        # no need to check validity of the location cause it had been checked in make_move
        self.board[location] = mark
        return self.victory(mark)

    """
        input: mark.
        output: bool.
        goal: return Y/N if this move win the game.
    """

    def victory(self, mark):
        victory_in_board = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [2, 4, 6],
            [0, 4, 8],
        ]
        # nesting for, every board situation check in victoryInBoard depended the mark
        # if victory exist - the all boolean values in the row will be true, then use
        # all to return the all 3 value - then we need only one true of third to declare a victory so i use any
        # - that return true if one of the literals is true.
        return any([all([self.board[x] == mark for x in i]) for i in victory_in_board])

    """
        input: self.
        output: bool.
        goal: if there's no ' ' in the array -> draw - return True.
   """

    def draw(self):
        return ' ' not in self.board

    """
        input: location on board.
        output: bool.
        goal: if there's no ' ' in the array -> draw - return True.
   """

    def legal_move(self, location):
        if location > 8 or location < 0 or self.board[location] != ' ':
            return False
        return True


class Game:
    """
        input: Plyer1, Player2.
        initialize Board instance then put the players in list, then return randomly which one will start and
        then initiate play()
    """

    def __init__(self, p1, p2):
        self.board = Board()
        self.players = [p1, p2]
        self.turn = random.choice([True, False])
        self.play()

    """
        input: self.
        output: none.
        goal: the heart of the game. this method run the game - start with first random move if the computer 
        playing, then till draw or victory take one step after one. each turn play by make_move that override depend on 
        the player.
   """

    def play(self):
        # first round - if computer chosen - play randomly
        if self.turn:
            self.board.random_move()
            self.turn = not self.turn
        # start playing - run until break from wining/draw
        while True:
            curr_player = self.players[int(self.turn)]
            print(self.board.to_string())
            # for each player the method make move works
            move = curr_player.make_move(self.board)
            winner = self.board.move(curr_player.mark, move)
            if winner:
                print(f'congrats {curr_player.name} you are the winner')
                winner_to_csv(curr_player.name, True)
                break
            if self.board.draw():
                print('draw')
                winner_to_csv(self.players[0].name, False)
                winner_to_csv(self.players[1].name, False)
                break
            self.turn = not self.turn

        print(self.board.to_string())  # print the final game board.

"""
Player class - contain player info and Player move.
"""


class Player:
    """
        input: name.
        goal: initialize Player, with name, mark and opponent mark.
    """

    def __init__(self, name):
        self.name = name
        self.mark = 'x'
        self.op_mark = 'o'

    """
        input: board.
        output: location in board.
        goal: checking for validity of the move - if yes continue otherwise looped in while until valid  
   """

    def make_move(self, board):
        move = input(f'This is the current board, {self.name} please pick 0-8\n')
        while True:
            move = int(move)
            if board.legal_move(move):
                if board.legal_move(move):
                    return move
            else:
                move = input('Illegal move, please try again.\n')


"""
Computer class - inherit from Player and override the method make_move.
"""


class Computer(Player):
    def __init__(self):
        self.name = 'computer'
        self.mark = 'o'
        self.op_mark = 'x'

    def make_move(self, board):
        moves = []
        for i in range(9):
            if board.legal_move(i):
                moves.append((self.evaluation(board, i), i))
        return sorted(moves)[-1][1]
        # moves = [(0.9, 0), (0.1, 1), (0.9, 2), (0.1, 3), (1, 4), (0.1, 5), (0.9, 6), (0.1, 7), (0.8, 8)]

    """
        input: board, depth of moves on the board, turn - to define between Computer turn to Player turn
        output: score of given i - calculated by computer.
        goal: recursively returning score of given i.
    """

    def evaluation(self, board, i, turn=True):
        new_board = board.clone()
        new_board.move(self.mark if turn else self.op_mark, i)
        if new_board.victory(self.mark):
            return 1
        elif new_board.victory(self.op_mark):
            return -1
        elif new_board.draw():
            return 0
        else:
            all_options = 0
            n_options = 0
            for i in range(9):
                if new_board.legal_move(i):
                    run = self.evaluation(new_board, i, not turn)
                    all_options += run
                    n_options += 1
        return all_options / n_options


"""
input: none
return: none.
goal: using pandas to read from csv file and print the list of players with thier score
in descending order.
"""
def show_high_scores():
    df = pd.read_csv('players.csv')
    print(df.sort_values(['score'], ascending=False))


"""
input: player (name) and boolean victory or draw.
return: none.
goal: using pandas to read from csv move to list to find if specific name is inside the
table or to open a new record. add 1 or 2 depend wining or draw
"""
def winner_to_csv(player, victory=True):
    df = pd.read_csv('players.csv')
    names = df['players'].tolist()
    if player in names:
        ind = df.index[df['players'] == player]
        if victory:
            df.loc[ind, 'score'] += 2
        else:
            df.loc[ind, 'score'] += 1
    else:
        df = df.append({'players': player, 'score': 2 if victory else 1}, ignore_index=True)
    df.to_csv('players.csv', index=False)


while True:
    str1 = input(f'please enter ShowHighScores other press any button to continue with the game or press q to quit')
    if str1 == 'ShowHighScores':
        show_high_scores()

    if str1 == 'q':
        break

    Game(Player(input(f'please enter p1')), Computer())
