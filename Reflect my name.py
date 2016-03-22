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

        
run(60,20,2125,B+O+S+H+E+N)
