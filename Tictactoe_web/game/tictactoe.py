import numpy as np
import math

'''The board positions are numbered as follows:
1 2 3
4 5 6
7 8 9
'''
'''
class Board(object):


row = []
#board = np.array()
#print(board)
for i in range(0,4):
    for j in range(0,4):
        row.append((i,j))
        #print('row', row)
'''

#np.concatenate(row, axis=0)
#print(row)

#board_to_key = {}
#dict ={}
filled_cell_player = {}
all_cells = []
win_moves = []
board = []

def create_board():
    global filled_cell_player, win_moves, all_cells, board

#    row_1 = np.arange(0,4)
#    row_2 = np.arange(4,8)
#    row_3 = np.arange(8,12)
#    row_4 = np.arange(12,16)

    row_1 = np.arange(0,3)
    row_2 = np.arange(3,6)
    row_3 = np.arange(6,9)
    #all_cells = np.arange(0,16)
    all_cells = np.arange(0,9)

    #board = np.array([row_1,row_2, row_3, row_4])
    board = np.array([row_1, row_2, row_3])

    '''
    #create dictionary to rename each cell from the Board
    key = 0
    global board_to_key
    for i in range(0,4):
        for j in range(0,4):
            print('i', i)
            print('board[i][j]', board[i][j])
            board[i][j] = key
            board_to_key[key]= board[i][j]
            key = key+1

        #print("row_1.length",row_1.length)

    print("board_to_key in def", board_to_key)
    '''
    win_moves = []

    # horizontal wins
    win_moves.append(row_1)
    win_moves.append(row_2)
    win_moves.append(row_3)
    #win_moves.append(row_4)
    print("win_moves",     win_moves)

    # vertical wins
    '''
    for i in range(0,4):
        win_moves.append(np.array([row_1[i], row_2[i], row_3[i], row_4[i]]))
        win_moves.append(np.array([row_1[i], row_2[i], row_3[i], row_4[i]]))
        win_moves.append(np.array([row_1[i], row_2[i], row_3[i], row_4[i]]))
    '''
    for i in range(0,3):
        win_moves.append(np.array([row_1[i], row_2[i], row_3[i]]))
    #print("for ",     win_moves)

    i = 0
    '''
    # diagonal wins from the left
    d_l=[row_1[i], row_2[i+1], row_3[i+2], row_4[i+3]]
    # diagonal wins from the right
    d_r=[row_1[i+3], row_2[i+2], row_3[i+1], row_4[i]]
    '''
    d_l=[row_1[i], row_2[i+1], row_3[i+2]]
    d_r=[row_1[i+2], row_2[i+1], row_3[i]]
#    print("d_r", d_r)
#    print("d_l", d_l)


    win_moves.append(np.array(d_l))
    win_moves.append(np.array(d_r))
#    print("win_moves",     win_moves)

    return board

#def retreive_board_info():
#    global filled_cell_player, win_moves, all_cells
#    return board, filled_cell_player

def is_game_over():
    global filled_cell_player, win_moves, all_cells

    dict_len = len(filled_cell_player)
    #print("dict_len", dict_len)
    for move in win_moves:
        cnt_human = 0
        cnt_ai = 0
        for cell in move:
            #if in diction keys with player
            #print("cell", cell)
            if cell in filled_cell_player.keys():
                if filled_cell_player[cell] == 'human':
                    cnt_human +=1
                if filled_cell_player[cell] == 'ai':
                    cnt_ai +=1
            else:
                continue

        #if cnt_human == 4:
        if cnt_human == 3:
        #    print("Human won")
        #    print("winning move", move)
            return 'human'
        #if cnt_ai == 4:
        if cnt_ai == 3:
        #    print("ai won")
        #    print("winning move", move)
            return 'ai'
    #if dict_len == 16:
    if dict_len == 9:
        return 'draw'
'''
def minimax(filled_cell_player, alpha, beta, human_turn, win_moves):
    global all_cells
    #print("all_cells", all_cells)

    result = is_game_over(filled_cell_player)
    if result == 1:
    #    print("Human won")
        #exit()
        return result
    if result == -1:
        #print("ai won")
        #exit()
        return result
    if result == 0:
        print("it's a draw")
        #exit()
        return result


    # loop through board and check what cells can be used for legal move
    #print('all_cells', all_cells)
    if human_turn:
        #print("human turn/ minimizing")
        min_score= + 1000
        for i in range(0,len(all_cells)):
            if all_cells[i] not in filled_cell_player.keys():

                filled_cell_player[all_cells[i]] = 'human'



                print('filled_cell_player', filled_cell_player)
                score = minimax(filled_cell_player, alpha, beta, False, win_moves)
                print("SCORE MIN", score)
                del filled_cell_player[all_cells[i]]
                min_score = min(min_score, score)
                beta = min(beta, score)
                #print('filled_cell_player after del', filled_cell_player)

                if beta <= alpha:
                    break
        return min_score
    else:
    #    print("ai turn/ maximizing")
        max_score = -  1000
        # need to loop throughh legal moves and also check is humna and not human alternate
        for i in range(0,len(all_cells)):
            if all_cells[i] not in filled_cell_player.keys():
                #print("all_cells[i]", all_cells[i])
                filled_cell_player[all_cells[i]] = 'ai'
                #print('filled_cell_player', filled_cell_player)
                score = minimax(filled_cell_player, alpha, beta, True, win_moves)
                print("SCORE MAX", score)
                del filled_cell_player[all_cells[i]]
                #print('filled_cell_player after del', filled_cell_player)
                max_score = max(max_score, score)
                alpha = max(alpha, score)
                #print("alpha", alpha)
                if beta <= alpha:
                    break

        return max_score

'''


def minimax( depth, human_turn):
    global filled_cell_player, win_moves, all_cells

    result = is_game_over()

    if result == 'human':
        return -1
    if result == 'ai':
        return 1
    if result == 'draw':
        return 0

    # loop through board and check what cells can be used for legal move
    if human_turn:
        min_score = 1000
        #for i in range(0, len(all_cells)):
            #if all_cells[i] not in filled_cell_player.keys():
        for cell in all_cells:
            if cell not in filled_cell_player.keys():
                filled_cell_player[cell] = 'human'
                score = minimax(depth+1, False)
                del filled_cell_player[cell]
                min_score = min(min_score, score)
            #    print("SCORE", score)
            #    print("SCORE MIN", min_score)
        return min_score

    else:
        max_score = -  1000
        for cell in all_cells:
            if cell not in filled_cell_player.keys():
                filled_cell_player[cell] = 'ai'
                score = minimax( depth+1, True)
                del filled_cell_player[cell]
                max_score = max(max_score, score)
            #    print("SCORE", score)
            #    print("SCORE MAX", max_score)
        return max_score

def get_ai_move():
    global filled_cell_player, win_moves, all_cells

    best_score = -1000
    best_move = None
    #for i in range(0, len(all_cells)):
        #if all_cells[i] not in filled_cell_player.keys():
    for cell in all_cells:
        if cell not in filled_cell_player.keys():
        #    print("cell", cell)
            filled_cell_player[cell] = 'ai'
            score = minimax( 0, True)
            #print("ai score", score)
            #print("potential", cell)
            del filled_cell_player[cell]
            if score > best_score :
                best_score  = score
                best_move = cell
    #print("ai best score", best_score)
    return best_move

def get_human_move(prompt, board):
    global filled_cell_player, win_moves, all_cells

    while True:
        try:
            human_move = int(input(prompt))
            print("The board look like the following :\n", board)
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if human_move not in all_cells:
            print("Sorry, your response must be one of the numbers in the displayed board.")
            continue
        if human_move in filled_cell_player.keys():
            print("Sorry, it's already taken the following player: ", filled_cell_player[human_move])
            continue
        else:
            #age was successfully parsed, and we're happy with its value.
            #we're ready to exit the loop.
            break
    return human_move

def play():
    # initialize variables
    global filled_cell_player, win_moves, all_cells, board

    human_turn = True
    board = create_board()
    print("win_moves", win_moves)

    while True:
        #retreive_board_info():

        # check if end of the game reached
        result = is_game_over()
        if result == 'human':
            print("winner is ", result)
            break
        if result == 'ai':
            print("winner is ", result)
            break
        if result == 'draw':
            print("winner is ", result)
            break

        if human_turn == True:
            print("The board look like the following :\n", board)
            human_move = get_human_move("Please enter your move: ", board)
            filled_cell_player[human_move] = 'human'
            print("filled_cell_player", filled_cell_player)
            human_turn = False

        # AI turn
        if human_turn == False:
        #    key = minimax(filled_cell_player, -1000, 1000, False, win_moves)
            ai_move = get_ai_move()
            filled_cell_player[ai_move] = 'ai'
            print("ai move", ai_move)
            print("filled_cell_player", filled_cell_player)
            human_turn = True

def initialize():
    global board
    create_board()
    human_turn = True
    return human_turn, board

def get_human_move_dj(human_move):
    global board

    print("The board look like the following :\n", board)
#    human_move = get_human_move("Please enter your move: ", board)
    filled_cell_player[human_move] = 'human'
    print("filled_cell_player", filled_cell_player)

    return filled_cell_player

def get_ai_move_dj():
    ai_move = get_ai_move()
    filled_cell_player[ai_move] = 'ai'
    print("ai move", ai_move)
    print("filled_cell_player", filled_cell_player)

    return filled_cell_player

def play_in_django(human_turn, human_move):
    '''
        Check for the end of the game
        & update boards by: getting human move or generating ai move
    '''
        # Initialize game
    global filled_cell_player, win_moves, all_cells
    winner = None

        # Check for end game
    result = is_game_over()

        # If winner found, return winner and current states of the board
    if result == 'human':
        return winner, filled_cell_player
    if result == 'ai':
        return winner, filled_cell_player
    if result == 'draw':
        return winner, filled_cell_player

        # Update moves
    if human_turn:
        filled_cell_player = get_human_move_dj(human_move)
    else:
        if human_move = None:
            #    key = minimax(filled_cell_player, -1000, 1000, False, win_moves)
            filled_cell_player = get_ai_move_dj()

    return None, filled_cell_player

if __name__ == "__main__":
    play()
