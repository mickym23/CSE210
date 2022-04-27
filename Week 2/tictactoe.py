###########################################
# Assignment: W02 Prove: Tic Tac Toe Game #
# Author: Mikhail Cedras                  #
# Class: CSE210                           #
###########################################

from tabnanny import check
import time

def main():
    print('\nWelcome to the game of Tic Tac Toe!!')
    
    # time.sleep(1.5)

    player = ''
    board_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    display_board(board_nums)
    while (not check_win(board_nums) and not check_draw(board_nums)): 
        # list of variable tiles 
        player = get_player(player)
        board_nums = change_tile(player, board_nums)
        print(board_nums)
        # print(board_nums)
        display_board(board_nums)
    print(f' Outside loop: {board_nums}')
    if check_win(board_nums):
        print(f'Congratulations! The winner is \'{player}\'')    
    elif (check_draw(board_nums)):
        pg = input(f'It\'s a draw! Do you want to play again? (y/n): ')
        if pg.strip().lower() == 'y':
            main()
        else:
            print('\n Thank you for playing!')

# Print Board
def display_board(board_nums):
    print()
    print(f'{board_nums[0]}|{board_nums[1]}|{board_nums[2]}')
    print('-+-+-')
    print(f'{board_nums[3]}|{board_nums[4]}|{board_nums[5]}')
    print('-+-+-')
    print(f'{board_nums[6]}|{board_nums[7]}|{board_nums[8]}')

def get_player(current_player):
    if current_player == '' or current_player == 'o':
        current_player = 'x'
    else:
        current_player = 'o'
    
    return current_player

def change_tile(player, board_nums):
    tile = int(input(f'{player}\'s turn to choose a square (1-9): '))
    i = board_nums.index(tile)
    board_nums = board_nums[:i]+[player]+board_nums[i+1:]
    return board_nums

def check_win(board_nums):
    return (board_nums[0] == board_nums[1] == board_nums[2] or
        board_nums[3] == board_nums[4] == board_nums[5] or
        board_nums[6] == board_nums[7] == board_nums[8] or
        board_nums[0] == board_nums[4] == board_nums[8] or
        board_nums[2] == board_nums[4] == board_nums[6] or
        board_nums[0] == board_nums[3] == board_nums[6] or
        board_nums[1] == board_nums[4] == board_nums[7] or
        board_nums[2] == board_nums[5] == board_nums[8])

def check_draw(board_nums):
    print(f'First check draw: {board_nums}')
    if all([isinstance(x, str) for x in board_nums]):
        return True
    else:
        return False
main()
