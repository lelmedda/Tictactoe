import numpy as np
import math

 """The board positions are numbered as follows:
    1 2 3
    4 5 6
    7 8 9
    """
'''
class Board(object):

    def _init_(self):
      self.board =

    def initialize(self):
      self.current_board =
      self.current_player = # 'X' or '0'

    def display_board(self):

    def is_move_legal(self, ):


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
def create_board():
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
    board = np.array([row_1,row_2,  row_3])

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

    # vertical wins
    '''
    for i in range(0,4):
        win_moves.append(np.array([row_1[i], row_2[i], row_3[i], row_4[i]]))
        win_moves.append(np.array([row_1[i], row_2[i], row_3[i], row_4[i]]))
        win_moves.append(np.array([row_1[i], row_2[i], row_3[i], row_4[i]]))
    '''
    for i in range(0,2):
        win_moves.append(np.array([row_1[i], row_2[i], row_3[i]]))

    i = 0
    '''
    # diagonal wins from the left
    d_l=[row_1[i], row_2[i+1], row_3[i+2], row_4[i+3]]
    # diagonal wins from the right
    d_r=[row_1[i+3], row_2[i+2], row_3[i+1], row_4[i]]
    '''
    d_l=[row_1[i], row_2[i+1], row_3[i+2]]
    d_r=[row_3[i+2], row_1[i+1], row_2[i]]

    win_moves.append(np.array(d_l))
    win_moves.append(np.array(d_r))

    #print("board", board)
    #print("board[1]", board[1])
    #print("board[1][0]", board[1][0])
    #print("win_moves", win_moves)
    return board, all_cells, win_moves

def is_game_over(filled_cell_player ):
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
def minimax(filled_cell_player, alpha, beta, human_turn):
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
                score = minimax(filled_cell_player, alpha, beta, False)
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
                score = minimax(filled_cell_player, alpha, beta, True)
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


def minimax(filled_cell_player, all_cells, depth, human_turn):
    result = is_game_over(filled_cell_player )

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
                score = minimax(filled_cell_player, all_cells, depth+1, False)
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
                score = minimax(filled_cell_player,  all_cells, depth+1, True)
                del filled_cell_player[cell]
                max_score = max(max_score, score)
            #    print("SCORE", score)
            #    print("SCORE MAX", max_score)
        return max_score

def get_ai_move(filled_cell_player, all_cells):
    best_score = -1000
    best_move = None
    #for i in range(0, len(all_cells)):
        #if all_cells[i] not in filled_cell_player.keys():
    for cell in all_cells:
        if cell not in filled_cell_player.keys():
        #    print("cell", cell)
            filled_cell_player[cell] = 'ai'
            score = minimax(filled_cell_player, all_cells, 0, True)
            #print("ai score", score)
            #print("potential", cell)
            del filled_cell_player[cell]
            if score > best_score :
                best_score  = score
                best_move = cell
    #print("ai best score", best_score)
    return best_move

def get_human_move():
    cell = input("Enter a number (human) :\n")
    if cell not in filled_cell_player.keys() and cell in all_cells:
        return cell
    else:
        print("Please try again")
        get_human_move()

if __name__ == "__main__":

    # initialize variables
    filled_cell_player = {}
    human_turn = True
    board, all_cells, win_moves= create_board()
    print("win_moves", win_moves)

    while True:

        # check if end of the game reached
        result = is_game_over(filled_cell_player)
        if result == 'human':
            print("winner is ", result)
            break
        if result == 'ai':
            print("winner is ", result)
            break
        if result == 'draw':
            print("winner is ", result)
            break

        #for filled_cell in filled_cell_player.keys():

        #    print("cell", filled_cell)
        #    print("player", filled_cell_player[filled_cell])



        if human_turn == True:
            human_move = get_human_move()
            filled_cell_player[human_move] = 'human'
            human_turn = False

        # AI turn
        if human_turn == False:
        #    key = minimax(filled_cell_player, -1000, 1000, False)
            ai_move = get_ai_move(filled_cell_player, all_cells)
            filled_cell_player[ai_move] = 'ai'

            print("ai move",ai_move)
            human_turn = True


        # check if move is legal and add it to human
        #if [row, col] not in human_move_list and [row, col] not in ai_move_list:
        # ==> remove from available cells list and add to dictionary as player's cell






        # AI move
        #else:
