

> ##第三次作业
> 
- 作业L1 在屏幕上用字符拼出自己姓名的英文
- 作业L2 在屏幕上用字符拼出任意次序的姓名
- 作业L3 在80*80点阵上用字符拼出你想画的东西，希望脑洞大开！（比如字符，火柴人，实现移动、旋转等等）

## level1&2 : Reflect My Name 
###Abstract
   Theoretically, this code(if finished) is capable of printing all letters from "A" to "Z" in a dot pattern. However, I spend my time mainly on level3, which evidently represents my enthusiasm for Python. So listed as follows is my semi-manufactured code only to print my name with the effect of specular reflection.

### Code   
	from collections import Counter
	from time import sleep
	import os
	
	B =[(9, 8 ,0), (6, 8,0), (7, 8, 0), (8, 8,0),  (6, 9,0),  (10, 9,0), (6, 10,0), (7, 10,0), ( 8, 10,0), ( 9, 10,0), ( 6, 11,0), (10, 11,0), (6, 12,0), (7, 12,0), (8, 12,0), (9, 12,0)]
	O =[(14, 8,0), (15, 8,0),(16, 8,0), (17, 9,0), (13, 9,0), (13, 10,0),(17,10,0), (13,11,0), (17, 11,0), (16, 12,0), (15, 12,0), (14, 12,0)]
	S =[(21, 8,0), (22, 8,0),(23, 8,0), (24, 8,0), (20, 9,0), (23, 10,0),(22,10,0), (21,10,0), (24, 11,0), (21, 12,0), (20, 12,0), (22, 12,0), (23, 12,0)]
	H =[(27, 8,0), (31, 8,0),(27, 9,0), (31, 11,0),(27, 11,0), (27,12,0),(31,12,0), (27,10,0), (28, 10,0), (29, 10,0), (30, 10,0), (31, 10,0),(31, 9,0)]
	E =[(34, 8,0), (35, 8,0),(36, 8,0), (37, 8,0),  (38, 8,0), (34,9,0), (34,10,0), (35,10,0), (36, 10,0), (37, 10,0), (38, 10,0), (34, 11,0), (34,12,0),(35,12,0),(36,12,0),(37,12,0),(38,12,0)]
	N =[(41, 11,0),(41, 8,0),(41, 9,0), (45, 8,0), (42, 9,0),  (45,9,0), (45,10,0), (43,10,0), (41, 10,0), (44, 11,0), (45, 11,0), (45, 12,0), (41,12,0)]
	
	direction =  [  ( 1, 1),
	                ( -1,1),
	                (-1,-1),
	                ( 1,-1),
	                ( 1, 1),
	                ( -1,1),
	                        ] # reserve 2 more directions
	
	def List(book,Xs,Ys):
	    u = [remove(c) for c in book]
	    return u
	
	def nextstep(book,Xs,Ys):
	    u = [move(c,Xs,Ys) for c in book]
	    return u
	 
	def move(pixel,Xs,Ys):
	    x,y,a = pixel
	    Xs,Ys = Xs - 2 ,Ys - 2
	    if( x<2 or  x>Xs or  y<2 or y>Ys ):
	        if( ( x == y and a == 2 ) or ( x - y  == Xs - Ys and a == 0 ) or ( x + y == Ys + 2 and a == 1) or ( x + y == Xs + 2 and a == 3 )):
	            if(a+2 >3):
	                a -= 2
	            else:
	                a += 2
	        else:
	            for i in range(4):
	                mark=[0]*6
	                x,y = remove(pixel)
	                dx, dy = direction[i]
	                x,y  = x+dx, y+dy
	                if (a+2 >3):
	                    mark[a-2]=1
	                else :
	                     mark[a+2]=1
	                if ( x<1 or  x>Xs+1 or  y<1 or y>Ys+1 ):
	                    continue
	                elif (mark[i]==1):
	                    continue
	                else:
	                    a=i
	                    return (x,y,a)           
	    dx, dy = direction[a]
	    x,y  = x+dx, y+dy
	    return (x,y,a)     
	                        
	def remove(pixel):
	    x,y,a = pixel
	    return (x,y)
	
	def display(book, Xs,Ys):
	    for y in range(Ys+1):
	        print ''.join('*' if (x, y) in List(book,Xs,Ys) else ' ' for x in range(Xs+1))
	    sleep (0.03)
	    i = os.system('cls')
	 
	    
	def run(Xs,Ys,steps,book):     
	    display(book,Xs,Ys)
	    if steps > 0 :
	        run(Xs,Ys, steps-1, nextstep(book,Xs,Ys))    
	
	        
	run(60,20,2016,B+O+S+H+E+N)

###Display
   ![LEVEL1&2](https://github.com/endeavor19/computationalphysics_N2013301020025/blob/master/level1%262.gif)
	
## *level3 : Conway's Game of Life*
###Abstract
   Following the methodology of block-based programming, I succeed to materialize the boardless world of Conway's Game of Life with "defaultdict". This code uses defaultdict(int) to create dictionaries that return the result of int, in other words, 0 for any key not in the dictionary.

###Background 


> Life is a "game" or cellular automaton - an evolving computational state system - developed by a Cambridge mathematician named John Conway.



> The idea is simple: start with a board of dimensions (x,y). Populate the board with an initial pattern of occupied and empty cells. In every turn, the rules are:



>
1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by over-population.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.      
       ——Wikipedia

> For instance, the queen bee shuttle (or basic shuttle
) is a period 30 shuttle oscillator in which a queen bee travels back and forth between two stabilizing ends. It was found by Bill Gosper in 1970 and was the first period 30 oscillator to be found.                            
![the queen bee shuttle](https://github.com/endeavor19/computationalphysics_N2013301020025/blob/master/gof.gif)

###Code
	from collections import defaultdict
	from time import sleep
	import os
	
	B =[(9, 8), (6, 8), (7, 8), (8, 8),(6, 9), (10, 9),(6, 10), (7, 10), (8, 10), (9, 10),(6, 11), (10,11),(6, 12), (7, 12), (8, 12), (9, 12)]
	O =[(14, 8), (15, 8), (16, 8),(17, 9), (13, 9),(13, 10), (17, 10),(13, 11), (17, 11), (16, 12), (15, 12), (14, 12)]
	S =[(21, 8), (22, 8), (23, 8), (24, 8),  (20, 9),(23, 10), (22, 10), (21, 10),(24, 11),(21, 12),(20, 12), (22, 12), (23, 12)]
	H =[(27, 8), (31, 8), (27, 9), (31, 11), (27, 11), (27, 12), (31, 12),(27, 10), (28, 10), (29, 10), (30, 10), (31, 10)]
	E =[(34, 8), (35, 8), (36, 8), (37, 8), (38, 8),(34, 9), (34, 10), (35, 10), (36, 10), (37, 10), (38, 	10),(34, 11),(34,12),(35,12),(36,12),(37,12),(38,12)]
	N = [(41, 11), (41, 8),(41, 9),(45, 8),(42, 9), (45, 9),(45, 10), (43, 10), (41, 10),(44, 11), (45, 11),(45, 12),(41,12)]
	NAME = B + O + S + H + E + N
	
	def neighbors(cell):
	    x,y = cell 
	    r = range(-1,2)  
	    return [(x+dx, y+dy) for dx in r for dy in r if (dx, dy) != (0, 0)]
	    	# Enumerate 8 directions to get the neighbors.
	
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
	    
	def display(cells, Xs, Ys):
	    for y in range(Ys):
	        print ''.join('*' if (x, y) in cells else ' ' for x in range(Xs)			
	        	# Connect '*' with ' ' to display cells.
	    sleep(0.03)
	 
	def Life(Xs, Ys, steps, cells):
	    display(cells, Xs, Ys)
	    if 0 < steps:
	    	i = os.system('cls')
	        Life(Xs, Ys, steps-1, nextstep(cells))
	        
	Life(50,20,192,NAME)
	while True: input()
	
###Display
![LEVEL3](https://github.com/endeavor19/computationalphysics_N2013301020025/blob/master/level3.gif)

##Acknowledgment
Thanks to [Ron89](https://github.com/Ron89), who aroused my appetite for further reading material on [Cellular Automata](http://www.worldscientific.com/worldscibooks/10.1142/4702) and [Complexity Science](http://www.worldscientific.com/series/scs).

## Reference

- [Conway's Game of Life - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life )
- [Rosetta Code: Conway's Game of Life](http://rosettacode.org/wiki/Conway%27s_Game_of_Life#Python)
- [Allen B. Downey: Think Python: How to Think Like a Computer Scientist](http://greenteapress.com/wp/think-python/ )
