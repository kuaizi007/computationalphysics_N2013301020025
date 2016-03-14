## *level1&2 : Print My Name*
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


###Background 


> Life is a "game" or cellular automaton - an evolving computational state system - developed by a Cambridge mathematician named John Conway.



> The idea is simple: start with a board of dimensions (x,y). Populate the board with an initial pattern of occupied and empty cells. In every turn, the rules are:



>
1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by over-population.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.                                        
> ——Wikipedia

###Code
	from collections import Counter
	from time import sleep
	import os

	neighboring_cells = [(-1, -1), (-1, 0), (-1, 1), 
	                     ( 0, -1),          ( 0, 1), 
	                     ( 1, -1), ( 1, 0), ( 1, 1)]
	blinker = {(1, 0), (1, 1), (1, 2)}
	block   = {(0, 0), (1, 1), (0, 1), (1, 0)}
	toad    = {(1, 2), (0, 1), (0, 0), (0, 2), (1, 3), (1, 1)}
	glider  = {(0, 1), (1, 0), (0, 0), (0, 2), (2, 1)}
	world   = (block | offset(blinker, (5, 2)) | offset(glider, (15, 5)) | offset(toad, (25, 5))
	           | {(18, 2), (19, 2), (20, 2), (21, 2)} | offset(block, (35, 7)))

	def life(world, N):
    	for g in range(N+1):
        	display(world, g)
        	counts = Counter(n for c in world for n in offset(neighboring_cells, c))
        	world = {c for c in counts 
                if counts[c] == 3 or (counts[c] == 2 and c in world)}
 
	def offset(cells, delta):
    	(dx, dy) = delta
    	return {(x+dx, y+dy) for (x, y) in cells}
 
	def display(world, g):
    	print '          GENERATION {}:'.format(g)
    	Xs, Ys = zip(*world)
    	Xrange = range(min(Xs), max(Xs)+1)
    	for y in range(min(Ys), max(Ys)+1):
       		print ''.join('#' if (x, y) in world else '.'
            	for x in Xrange)
    	sleep(0.1)
    	i = os.system('cls')
 
	life(world, 5)
	while True: input()	

## Reference

- [pikipity: 用 Pygame 编写的生命游戏](http://pikipity.github.io/blog/the-game-of-life-using-pygame.html )
- [Rosetta Code: Conway's Game of Life](http://rosettacode.org/wiki/Conway%27s_Game_of_Life#Python)
- [Allen B. Downey: Think Python: How to Think Like a Computer Scientist](http://greenteapress.com/wp/think-python/ )