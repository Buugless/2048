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
    for i in range(4):
        new_mat.append([0] * 4)
print(initialize_board())