import random

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

board = initialize_board()
print(board)
compressed_board = compress(board)
print(compressed_board)
print(merge(compressed_board))