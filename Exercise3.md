

> ##第三次作业
> 
- 作业L1 在屏幕上用字符拼出自己姓名的英文
- 作业L2 在屏幕上用字符拼出任意次序的姓名
- 作业L3 在80*80点阵上用字符拼出你想画的东西，希望脑洞大开！（比如字符，火柴人，实现移动、旋转等等）

## *level1&2 : Print My Name*
### Code    
     [Print My Name](https://github.com/endeavor19/computationalphysics_N2013301020025/blob/master/py/Print%20My%20Name.py)
     
### Display


## *level3 : Conway's Game of Life*


###Background 


> Life is a "game" or cellular automaton - an evolving computational state system - developed by a Cambridge mathematician named John Conway.



> The idea is simple: start with a board of dimensions (x,y). Populate the board with an initial pattern of occupied and empty cells. In every turn, the rules are:



>
1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by over-population.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.      

> Additionally, The queen bee shuttle (or basic shuttle
) is a period 30 shuttle oscillator in which a queen bee travels back and forth between two stabilizing ends. It was found by Bill Gosper in 1970 and was the first period 30 oscillator to be found.                            
> ——Wikipedia ![](http://www.conwaylife.com/w/images/c/c2/Queenbeeshuttle.png "Queen bee shuttle")


###Code
	
	from collections import Counter
	from time import sleep
	import os

	neighboring_cells = [(-1, -1), (-1, 0), (-1, 1), 
	                     ( 0, -1),          ( 0, 1), 
	                     ( 1, -1), ( 1, 0), ( 1, 1)]
	block   = {(0, 0), (1, 1), (0, 1), (1, 0)}
	world   = (offset(block, (5, 15)) | {(10, 15), (13, 15), (13, 14),(13, 16),(11, 14),(11, 16),(12, 13),(14, 13),(14, 12),(14, 17),(14, 18), (12, 17)} | offset(block, (25, 15)))
   				#Set the coordinates of initial world.

	def life(world, N):
    	for g in range(N+1):
        	display(world, g)
        	counts = Counter(n for c in world for n in offset(neighboring_cells, c))
        	world = {c for c in counts 
                if counts[c] == 3 or (counts[c] == 2 and c in world)} 
                # Apply the Game Of Life rule set to every cell.
 
	def offset(cells, delta):
    	(dx, dy) = delta
    	return {(x+dx, y+dy) for (x, y) in cells}
 				# Offset all the cells by delta, a (dx, dy) vector.

	def display(world, g):
    	print '          GENERATION {}:'.format(g)
    	Xs, Ys = zip(*world)
    	Xrange = range(min(Xs), max(Xs)+1)
    	for y in range(min(Ys), max(Ys)+1):
       		print ''.join('#' if (x, y) in world else '.'
            	for x in Xrange)
    	sleep(0.03)
    	i = os.system('cls')
 
	life(world,200)
	
###Display
   ![queen bee shuttle](https://raw.githubusercontent.com/endeavor19/computationalphysics_N2013301020025/master/gof.gif )

## Reference

- [pikipity: 用 Pygame 编写的生命游戏](http://pikipity.github.io/blog/the-game-of-life-using-pygame.html )
- [Rosetta Code: Conway's Game of Life](http://rosettacode.org/wiki/Conway%27s_Game_of_Life#Python)
- Allen B. Downey：[ Think Python: How to Think Like a Computer Scientist](http://greenteapress.com/wp/think-python/ )
