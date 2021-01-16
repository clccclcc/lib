# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:38:11 2020

@author: clccclcc
"""
'''
puzzlelib.py 함수 설명
* puzzle_show(퍼즐,타이틀 메시지): msg 타이틀로 퍼즐을 보여 줌 
* puzzle_ini(x크기,y크기,난이도):일정 크기의 퍼즐을  새로 생성  하고 일정한 난이도로 섞는다.
* puzzle_move(퍼즐,방향): 특정 방향으로 공백을 옮김 (left,right,up,down)
* puzzle_check_same(퍼즐1,퍼즐2): 퍼즐1과 2가 같은지 검
* puzzle_check_gameover(퍼즐): 퍼즐의 종료 여부를 확인 
* puzzle_help(): 도움말 출력     
* puzzle_getclone(퍼즐): 입력된 퍼즐과 동일한 퍼즐 객체 1개 생성 
* puzzle_simulation(시작퍼즐,명령경로,움직임 경로 리스트 , 개당 시뮬레이션 시간차  ) 
    
'''

import random
import copy 
import time

def puzzle_show_v0(puzzle,msg=''):
    print('--------')
    print(msg)
    
    for y in puzzle:
        print(y)
    print('--------')

def puzzle_show(puzzle,msg=''):
    # 2021.1.9
    print('--------')
    print(msg)
    
    for y in puzzle:
        msg=''
        for x in y:
            if 0 == x:
                x=''
            #msg='{}\t{}'.format(msg,x)
            msg='%s\t%3s' % (msg,x)
            
        print(msg)
    print('--------')
  
    
def find_blankpos(puzzle):
    ysize=len(puzzle)
    xsize=len(puzzle[0])
    for y in range(ysize):
        for x in range(xsize):
            if 0==puzzle[y][x]:
                return x,y
    return -1,-1

def puzzle_ini(xsize,ysize,loop=100):    
    data=[]    
    
    val=1
    for y in range(ysize):
        d=[]
        for x in range(xsize):
            d.append(val)
            val = val + 1
            if val == xsize*ysize:
                val=0
        data.append(d)
        
    data_goal=copy.deepcopy(data)    
    
    sx=xsize - 1
    sy=ysize - 1
    for i in range(loop):
        dx = sx
        dy=sy
        dir = random.randint(0,3)
        if 0 == dir:
            dx = sx + 1
            if move(data,sx,sy,dx,dy):
                sx = sx + 1
                pass
        elif 1==dir:
            dx = sx - 1
            if move(data,sx,sy,dx,dy):
                sx = sx - 1
                pass

        elif 2==dir:
            dy = sy + 1
            if move(data,sx,sy,dx,dy):
                sy = sy + 1
                pass

        else:
            dy = sy - 1
            if move(data,sx,sy,dx,dy):
                sy = sy - 1
                pass
        
    return data,data_goal


    
def move(puzzle,x,y,dx,dy,check=False):    
    ysize=len(puzzle)
    xsize=len(puzzle[0])
    if x < 0 or y < 0 or dx < 0 or dy < 0:
        return False
    if xsize <= x or ysize <= y or xsize <= dx or ysize <= dy:
        return False
    
    if 0==puzzle[y][x] :
        if False == check:
            t=puzzle[dy][dx]
            puzzle[dy][dx] = puzzle[y][x]
            puzzle[y][x]=t
            
        return True       
    else:
        return False
    
def puzzle_move_v0(puzzle,dir):
    sx,sy=find_blankpos(puzzle)    
    re=False
    if "left" == dir:        
        re=move(puzzle,sx,sy,sx-1,sy)
    elif "right" == dir:        
        re = move(puzzle,sx,sy,sx + 1,sy)
    elif "up" == dir:
        re = move(puzzle,sx,sy,sx,sy-1)
    elif "down" == dir:
        re = move(puzzle,sx,sy,sx,sy+1)
        
    return re
 
def puzzle_move(puzzle,dir):
    # 2021.1.9
    sx,sy=find_blankpos(puzzle)    
    re=False
    if "left" == dir or 'l' == dir:        
        re=move(puzzle,sx,sy,sx-1,sy)
    elif "right" == dir or 'r' == dir:        
        re = move(puzzle,sx,sy,sx + 1,sy)
    elif "up" == dir or 'u' == dir:
        re = move(puzzle,sx,sy,sx,sy-1)
    elif "down" == dir or 'd'==dir:
        re = move(puzzle,sx,sy,sx,sy+1)
        
    return re
         
def puzzle_check_same(puzzle,puzzle_goal):
    ysize= len(puzzle)
    xsize = len(puzzle[0])
    for y in range(ysize):        
        for x in range(xsize):
           if puzzle_goal[y][x] != puzzle[y][x]:
               return False           
    return True        

def puzzle_check_gameover(puzzle):
    val=1
    ysize= len(puzzle)
    xsize = len(puzzle[0])
    for y in range(ysize):
        
        for x in range(xsize):
           if val != puzzle[y][x]:
               return False
           val = val + 1
           if val == xsize*ysize:
               val=0
    return True

def puzzle_help():
    print('----------------------------')
    print('hepuzzle ver 0.1 by clccclcc')
    print('command:  left,right,up,down')
    print('----------------------------')
 
def puzzle_getclone_v0(puzzle):
    return copy.deepcopy(puzzle)

def puzzle_getclone(puzzle):
    t=[]
    for line in puzzle:
        t_line=[]
        for x in line:
            t_line.append(x)
        t.append(t_line)
        
    return t
# from treelib import *

def puzzle_simulation_v0(start,path,dir_index=0,interval=2):
    print("---> Start ans simulation <---" )
    step=0    
    total_step=len(path) - 1
    for p in path:           
        puzzle_move(start,p[dir_index])
        
        puzzle_show(start,p[dir_index] + ":" + str(step) + "/" + str(total_step)) 
         
        time.sleep(interval)
        step +=1
    
    print("---> End ans simulation <---" )
    
def puzzle_simulation(start,path,dir_index=0,interval=2):
    print("---> Start ans simulation <---" )
    step=0    
    total_step=len(path) - 1
    for p in path:           
        p.show()
        puzzle_move(start,p.etc[dir_index])
         
        puzzle_show(start,p.etc[dir_index] + ":" + str(step) + "/" + str(total_step))
        time.sleep(interval)
        step +=1
    
    print("---> End ans simulation <---" )
    
def get_puzzle_path(tree,target_node):
    # print('>>>>>>>>>>>>>>>>')
    path = tree.getpath(target_node) 
    log=[]
    for t_node in path:
        
        log.append(t_node.etc[0])
     
    return log,path