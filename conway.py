import os
import random
import time
from itertools import count

def get_new_state(grid, neighbors):
    if grid == 0 and neighbors == 3:
        return 1
    elif grid == 1 and (neighbors == 2 or neighbors == 3):
        return 1
    else:
        return 0

def get_neighbors(grid, i, j):
    neighbors = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            elif i + x < 0 or i + x >= len(grid):
                continue
            elif j + y < 0 or j + y >= len(grid[0]):
                continue
            elif grid[i + x][j + y] == 1:
                neighbors += 1
    return neighbors

def print_grid(grid, i):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Generation " + str(i), '\n\n')
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                print(u"\u2588", end='')
            else:
                print(' ', end='')
        print()
    print()
    print('\n')
    time.sleep(0.1)

def update_grid(grid):
    updated_grid = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = get_neighbors(grid, i, j)
            updated_grid[i][j] = get_new_state(grid[i][j], neighbors)
    return updated_grid

def generate_initial_grid(density):
    grid = [[0 for i in range(180)] for j in range(30)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if random.random() < density:
                grid[i][j] = 1
    return grid

def game_loop():
    # randomly populating the board with a population density in the range [0.2, 0.35]
    # the grid's density will be randomly generated time the game is played
    density = random.uniform(0.2, 0.35)
    grid = generate_initial_grid(density)
    
    #infinite loop for the game to play indefinitely
    for i in count(0):
        print_grid(grid,i)
        grid = update_grid(grid)

if __name__ == '__main__':
    game_loop()