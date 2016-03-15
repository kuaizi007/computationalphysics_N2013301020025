

> ##第三次作业
> 
- 作业L1 在屏幕上用字符拼出自己姓名的英文
- 作业L2 在屏幕上用字符拼出任意次序的姓名
- 作业L3 在80*80点阵上用字符拼出你想画的东西，希望脑洞大开！（比如字符，火柴人，实现移动、旋转等等）

## *level1&2 : Print My Name*
###Abstract
   Theoretically, this code(if finished) is capable of printing all letters from "A" to "Z" in a dot pattern. However, I spend my time mainly on level3, which evidently represents my enthusiasm for Python. Therefore here lies my semi-manufactured code only to print my name in an arbitrary sequence.

### Code   
     _=['       ','       ','       ','       ','       ']
     B=[' ****  ',' *   * ',' ****  ',' *   * ',' ****  ']
     O=['  ***  ',' *   * ',' *   * ',' *   * ','  ***  ']
     S=['  **** ',' *     ','  ***  ','     * ',' ****  ']    
     H=[' *   * ',' *   * ',' ***** ',' *   * ',' *   * '] 
     E=[' ***** ',' *     ', ' *****',' *     ',' ***** ']
     N=[' *   * ',' **  * ','  * * *',' *  ** ',' *   * ']
     repository = {' ':_,'b':B,'o':O,'s':S,'h':H,'e':E,'n':N}

     letters= raw_input('please type letters from "boshen" ').lower()
     l= len(letters)

     for y in range(5):    
         letters_pixel =_
         for x in range(l):
             letters_pixel[y]+=repository[letters[x]][y]
         print letters_pixel[y]
    
     while True: input()

## *level3 : Conway's Game of Life*
###Abstract
   I used to realize Conway's Game of Life in C or C++. Unfortunately, it always turns out that honing my programming skills is definetely necessary. Having devoted hours to debugging this code, I render it to attain my standards successfully.

###Background 


> Life is a "game" or cellular automaton - an evolving computational state system - developed by a Cambridge mathematician named John Conway.



> The idea is simple: start with a board of dimensions (x,y). Populate the board with an initial pattern of occupied and empty cells. In every turn, the rules are:



>
1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by over-population.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.      

> For instance, the queen bee shuttle (or basic shuttle
) is a period 30 shuttle oscillator in which a queen bee travels back and forth between two stabilizing ends. It was found by Bill Gosper in 1970 and was the first period 30 oscillator to be found.                            
![the queen bee shuttle](https://github.com/endeavor19/computationalphysics_N2013301020025/blob/master/gof.gif)——Wikipedia

###Code
	from collections import defaultdict
	from time import sleep
	import os
	
	L1 = [(9, 8), (6, 8), (7, 8), (8, 8), (14, 8), (15, 8), (16, 8), (21, 8), (22, 8), (23, 8), (24, 8), (27, 8), (31, 8), (34, 8), (35, 8), (36, 8), (37, 8), (38, 8), (41, 8), (45, 8)]
	L2 = [(6, 9), (10, 9), (17, 9), (13, 9), (20, 9), (27, 9), (34, 9), (41, 9), (42, 9), (45, 9)]
	L3 = [(6, 10), (7, 10), (8, 10), (9, 10), (13, 10), (17, 10), (23, 10), (22, 10), (21, 10), (27, 10), (28, 10), (29, 10), (30, 10), (31, 10), (34, 10), (35, 10), (36, 10), (37, 10), (38, 10), (45, 10), (43, 10), (41, 10)] 
	L4 = [(6, 11), (10, 11), (13, 11), (17, 11), (24, 11), (31, 11), (27, 11), (34, 11), (41, 11), (44, 11), (45, 11)]
	L5 = [(6, 12), (7, 12), (8, 12), (9, 12),(16, 12), (15, 12), (14, 12), (21, 12),(20, 12), (22, 12), (23, 12), (27, 12), (31, 12), (38, 12), (37, 12), (36, 12), (35, 12), (34, 12), (41, 12),(45, 12)]
	NAME = L1 + L2 + L3 + L4 + L5
	
	def neighbors(cell):
	    x,y = cell
	    r = range(-1,2)
	    return [(x+dx, y+dy) for dx in r for dy in r if not (dx, dy) == (0, 0)]
	 
	def frequencies(cells):
	    res = defaultdict(int)  # To avoid KeyErrors
	    for cell in cells:
	        res[cell] += 1
	    return res
	 
	def lifeStep(cells):
	    freqs = frequencies([n for c in cells for n in neighbors(c)])
	    return [k for k in freqs if freqs[k]==3 or (freqs[k]==2 and k in cells)]
	 
	def printWorld(cells, Xs, Ys):
	    for y in range(0, Ys):
	        print ''.join('#' if (x, y) in cells else '.'
	                      for x in range(0, Xs))
	    sleep(1)
	    i = os.system('cls')
	 
	def runLife(Xs, Ys, steps, cells):
	    printWorld(cells, Xs, Ys)
	    if 0 < steps:
	        runLife(Xs, Ys, steps-1, lifeStep(cells))
	        
	runLife(50,20,30,NAME)
###Display
![LEVEL3](https://github.com/endeavor19/computationalphysics_N2013301020025/blob/master/level3.gif)

## Reference

- [Conway's Game of Life - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life )
- [Rosetta Code: Conway's Game of Life](http://rosettacode.org/wiki/Conway%27s_Game_of_Life#Python)
- [Allen B. Downey: Think Python: How to Think Like a Computer Scientist](http://greenteapress.com/wp/think-python/ )
