import random
import numpy

def initialize_board():
    matrix = []
    for i in range(4):
        matrix.append([0]*4)
    add_new_tile(matrix)
    add_new_tile(matrix)
    return matrix

def add_new_tile(matrix):
    empty_tiles=[]
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                empty_tiles.append((i,j))
    if empty_tiles:
        i , j = random.choice(empty_tiles)
        matrix[i][j] = 2
    return matrix
def compress(matrix):
    new_mat = []
    for _ in range(4):
        new_mat.append([0] * 4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if matrix[i][j] != 0:
                new_mat[i][pos] = matrix[i][j]
                pos += 1
    return new_mat

def merge(matrix):
        for i in range(4):
            for j in range(3):
                if matrix[i][j] == matrix[i][j+1] and matrix[i][j] != 0:
                    matrix[i][j] *= 2
                    matrix[i][j+1] = 0
        return matrix

def move_left(matrix):
    compressed = compress(matrix)
    merged = merge(compressed)
    final_matrix = compress(merged)
    return final_matrix 

def transpose(matrix):
    transposed = numpy.transpose(matrix)
    return transposed

def reverse(matrix):
    reversed = numpy.fliplr(matrix)
    return reversed
def move_up(matrix):
    transposed = transpose(matrix)
    moved = move_left(transposed)
    final_matrix = transpose(moved)
    return final_matrix
def move_down(matrix):
    tranposed = transpose(matrix)
    moved = move_left(tranposed)
    reverses = reverse(moved)
    final_matrix = transpose(reverses)
    return final_matrix
def move_right(matrix):
    reversed_board = reverse(matrix)
    moved = move_left(reversed_board)
    final_matrix = reverse(moved)
    return final_matrix
def is_game_over(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return False
            if j < 3 and matrix[i][j] == matrix[i][j+1]:
                return False
            if i < 3 and matrix[i][j] == matrix[i + 1][j]:
                return False 
    return True
def has_won(matrix):
    for i in matrix:
        if 2048 in i:
            return True
    return False    
def print_board(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))
    print()


def game():
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    board = initialize_board()
    while True:
        print_board(board)
        if has_won(board) == True:
            print("You have won!")
            break
        if is_game_over(board) == True:
            print("You have lost!")
            break
        move = input("Where do you want to move? ")
        if move == "W" or move == "w":
            board = move_up(board)
        if move == "S" or move == "s":
            board = move_down(board)
        if move == "D" or move == "d":
            board = move_right(board)
        if move == "A" or move == "a":
            board = move_left(board)
        board = add_new_tile(board)

game()