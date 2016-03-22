from collections import defaultdict
from time import sleep
import os

B =[(9, 8), (6, 8), (7, 8), (8, 8),(6, 9), (10, 9),(6, 10), (7, 10), (8, 10), (9, 10),(6, 11), (10,11),(6, 12), (7, 12), (8, 12), (9, 12)]
O =[(14, 8), (15, 8), (16, 8),(17, 9), (13, 9),(13, 10), (17, 10),(13, 11), (17, 11), (16, 12), (15, 12), (14, 12)]
S =[(21, 8), (22, 8), (23, 8), (24, 8),  (20, 9),(23, 10), (22, 10), (21, 10),(24, 11),(21, 12),(20, 12), (22, 12), (23, 12)]
H =[(27, 8), (31, 8), (27, 9), (31, 11), (27, 11), (27, 12), (31, 12),(27, 10), (28, 10), (29, 10), (30, 10), (31, 10)]
E =[(34, 8), (35, 8), (36, 8), (37, 8), (38, 8),(34, 9), (34, 10), (35, 10), (36, 10), (37, 10), (38,   10),(34, 11),(34,12),(35,12),(36,12),(37,12),(38,12)]
N =[(41, 11), (41, 8),(41, 9),(45, 8),(42, 9), (45, 9),(45, 10), (43, 10), (41, 10),(44, 11), (45, 11),(45, 12),(41,12)]
NAME = B + O + S + H + E + N

def neighbors(cell):
    x,y = cell 
    r = range(-1,2)
    # Enumerate 8 directions to get the neighbors.
    return [(x+dx, y+dy) for dx in r for dy in r if (dx, dy) != (0, 0)]

def frequencies(cells):
    u = defaultdict(int)
    # Use defaultdict to avoid Keyerror.
    for cell in cells:
        u[cell] += 1  
    return u

def nextstep(cells):
    freqs = frequencies([n for c in cells for n in neighbors(c)])
    # Count the neighboring cells.
    return [k for k in freqs if freqs[k]==3 or (freqs[k]==2 and k in cells)]
    # Determine the next state of cells accronding to the number of neighbors.

def display(cells, Xs, Ys):
    for y in range(Ys):
        print ''.join('*' if (x, y) in cells else ' ' for x in range(Xs))
        # Connect '#' with ' ' to display cells.
    sleep(0.03)

def Life(Xs, Ys, steps, cells):
    display(cells, Xs, Ys)
    if 0 < steps:
        i = os.system('cls')
        Life(Xs, Ys, steps-1, nextstep(cells))

Life(50,20,192,NAME)
while True: input()
