# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 09:25:59 2020

@author: clccclcc
"""
'''
my_get_gameboard() : 게임을 초기화 함 
my_draw() : 게임판을 그림 
my_inputpos() : 사용자로 부터 위치를 입력 받음. 
my_check_win() : 특정 사용자가 이겼는지 체크 함. 
my_next_player() : 다음 순서의 사용자를 알려줌 
my_empty_cells() : 게임판에서 비어 있는 곳의 위치를 알려 줌 

'''
MY_BLANK=' '
# =============================================================================
# 새로운 게임 보드를 만듬 
# =============================================================================
def my_get_gameboard(xsize,ysize):
    board=[]
    for y in range(ysize):
        line=[]
        for x in range(xsize):
            line.append(MY_BLANK)
        board.append(line)
        
    return board
#--------------------------------
def my_empty_cells(board):
    cells=[]
    
    ysize = len(board)
    xsize = len(board[0])
    #print("x,ysize",xsize,ysize)
    for y in range(ysize):
        for x in range(xsize):
            if board[y][x]== MY_BLANK:
                cells.append((x,y))
    return cells
 
#--------------------------------
def my_valid_move(x,game_board):    
    return x in my_empty_cells(game_board)
    #data=my_empty_cells(game_board)
    #print("@:",data)
 
#-----------------------------------
def my_draw(board):
    ysize = len(board)
    xsize=len(board[0])
    line='    '
    for x in range(xsize):
        msg = "%2s" % (x )
        line = line + msg + '|'
    print(line)
    
    for y in range(ysize):
        line=" %2s| " % (y)        
        for x in range(xsize):
            line = line + board[y][x] + '| '
        print(line)
 
#-----------------------------------
def my_move(x,player,game_board):
    #print("my_move:",my_valid_move(x,game_board),x)
    try:
        if my_valid_move(x,game_board):
            game_board[x[1]][x[0]]=player
            return True
    except :
        pass
        # print(" invalid position ..")
        
    return False
 
#----------------------------------------------
# def my_evaluate(board,goal_size):
#     if my_check_win(board,'x',goal_size)    :
#         score = 1
#     elif my_check_win(board,'o',goal_size):
#         score = -1
#     else:
#         score = 0
        
#     return score
#----------------------------------------------
#working
def lib_evaluate_checkH(board,tx,ty,p_value,dx,dy):
    ysize = len(board)
    xsize = len(board[0])
    goal_count = 0
    while True:
        tx=tx + dx
        ty=ty + dy
        if tx < 0 or xsize <= tx:
            break
        if ty < 0 or ysize <= ty:
            break
        
        if board[ty][tx] == p_value or board[ty][tx] == MY_BLANK :
            goal_count += 1            
        else:
            break
    return goal_count

def my_evaluate_heuristic(board,goal_size,xpos,ypos,maxPlayer):

    #print(">>>>>>")
    if maxPlayer:
        p_value='x'
    else:
        p_value='o'
       
    score = 0.0
    
    t_count1 = lib_evaluate_checkH(board,xpos,ypos,p_value,-1,0)
    t_count2 = lib_evaluate_checkH(board,xpos,ypos,p_value,1,0)
    if goal_size <= (t_count1 + t_count2) :
        score += 0.1

    t_count1 = lib_evaluate_checkH(board,xpos,ypos,p_value,0,-1)
    t_count2 = lib_evaluate_checkH(board,xpos,ypos,p_value,0,1)
    if goal_size <= (t_count1 + t_count2) :
        score += 0.1
    
    t_count1 = lib_evaluate_checkH(board,xpos,ypos,p_value,-1,-1)
    t_count2 = lib_evaluate_checkH(board,xpos,ypos,p_value,1,1)
    if goal_size <= (t_count1 + t_count2) :
        score += 0.1
    
    t_count1 = lib_evaluate_checkH(board,xpos,ypos,p_value,1,-1)
    t_count2 = lib_evaluate_checkH(board,xpos,ypos,p_value,-1,1)
    if goal_size <= (t_count1 + t_count2) :
        score += 0.1
    
    #print("<<<")
    return score 
#---------------------------------------------
def my_check_win(board,player,goal_size):
    ysize = len(board)
    xsize = len(board[0])
    for y in range(ysize):
        for x in range(xsize):
            if board[y][x] == player:
                # x-line check
                goal=True
                for i in range(goal_size):
                    if  xsize <= (x + i):
                        goal=False
                        break
                    
                    if board[y][x+i] != player:
                        goal=False
                        break
                if goal :
                    return True
                
                # y-line check
                goal=True
                for i in range(goal_size):
                    if ysize <= (y+i):
                        goal=False
                        break
                    
                    if board[y+i][x] != player:
                        goal=False
                        break
                if goal:
                    return True
                
                # 4-line check
                goal=True
                for i in range(goal_size):
                    if  xsize <= (x + i):
                        goal=False
                        break
                    if ysize <= (y+i):
                        goal=False
                        break
                    if board[y+i][x+i] != player:
                        goal=False
                        break
                if goal:
                    return True
                    
                # 3-line check
                goal=True
                for i in range(goal_size):
                    if  (x - i) < 0:
                        goal=False
                        break
                    if ysize <= (y+i):
                        goal=False
                        break
                    if board[y+i][x-i] != player:
                        goal=False
                        break
                if goal:
                    return True
    return False
 
#----------------------------------------------
# =============================================================================
# 게임 종료를 확인 
# =============================================================================
def my_game_over(board,goal_size):
    #print("gameover:",my_check_win(board,'x',goal_size),my_check_win(board,'o',goal_size))
    return my_check_win(board,'x',goal_size) or my_check_win(board,'o',goal_size)

def my_inputpos(msg):
    data = input(msg)
    data_pos = data.split(' ')
    data_pos = [int(x) for x in data_pos]
    return data_pos


# =============================================================================
# 다음 플레이어를 가지고 옴 
# =============================================================================
def my_next_player(player):
    if 'x' == player:
        return 'o'
    else:
        return 'x'
    
    
    
    
    
    