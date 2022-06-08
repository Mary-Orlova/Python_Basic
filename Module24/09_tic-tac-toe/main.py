import os
from board_for_game import  Board

os.system('clear')


def get_new_game():
    play_again = input('Сыграть еще раз? (да/нет)').lower()
    if play_again == 'да':
        board.reset()
    else:
        print('Игра завершена')


board = Board()

def print_header():
    print('Игра крестики-нолики\n')


def refresh_screen():
    os.system('clear')
    print_header()
    board.display()


while True:
    refresh_screen()
    x_choice = int(input('\n Выбери позицию для Х (1-9): '))
    board.update_cell(x_choice, 'X')
    refresh_screen()
    if board.is_winner('X'):
        print('\nX выиграл!\n')
        get_new_game()

    if board.is_tie():
        print('\nНичья!\n')
        get_new_game()

    o_choice = int(input('\n Выбери позицию для O (1-9): '))
    board.update_cell(o_choice, 'O')
    if board.is_winner('O'):
        print('\nO выиграл!\n')
        get_new_game()

    if board.is_tie():
        print('\nНичья!\n')
        get_new_game()

# class Board:
#     def __init__(self):
#         self.board = list('123456789')
#         self.wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
#                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
#                      (0, 4, 8), (2, 4, 6))
#
#     def printboard(self,Player=xo):
#         print('Игровое поле')
#         print('\n'.join(' '.join(self.board[x:x + 3]) for x in (0, 3, 6)))
#
#     def score(self):
#         for winner in self.wins:
#             board_win = self.board[winner[0]]
#             if board_win in 'XO' and all(self.board[_] == board_win for _ in winner):
#                 return board_win, [_ + 1 for _ in winner]
#         return None, None
#
#     def finished(self):
#         return all(board_win in 'XO' for board_win in self.board)
#
#     def space(self):
#         return [board_win for board_win in self.board if board_win not in 'XO']
#
#
# class Player:
#     def __init__(self, name):
#         self.name = name
#
#     def my_turn(self, xo):
#         options = Board().space()
#         choice = random.choice(options)
#         Board().board[int(choice) - 1] = xo
#         return choice
#
#     def your_turn(self, xo):
#         options = Board().space()
#         while True:
#             choice = input(" Выбери клетку для позиции %s (%s) : "
#                            % (xo, ''.join(options))).strip()
#             if choice in options:
#                 break
#             print("Не корректный ввод.")
#         Board().board[int(choice) - 1] = xo
#         return choice
#
#     def me(self, xo='X'):
#         Board().printboard()
#         print('\nКомпьютер ставит Х: на клетку №', player.my_turn(xo))
#         return Board().score()
#         assert not s[0], "\n%s Board().wins across %s" % s
#
#     def you(self, xo='O'):
#         Board.printboard(board)
#         print('\nВы ставите O: на клетку №', player.your_turn(xo))
#         return Board().score()
#         assert not s[0], "\n%s Board().wins выиграл - номера зачеркнутых ячеек %s" % s
#
#
# board = Board()
# player = Player('Игрок')
#
# while not Board().finished():
#     game = player.me('X')
#     if game[0]:
#         Board().printboard()
#         print("\n%s выиграл - номера зачеркнутых ячеек %s" %  game)
#         break
#     if not Board().finished():
#         s = player.you('O')
#         if s[0]:
#             Board().printboard()
#             print("\n%s выиграл - номера зачеркнутых ячеек %s" % s)
#             break
#     else:
#         print('что-то пошло не так')
