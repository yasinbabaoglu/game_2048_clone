# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 12:17:44 2022

@author: Yasin
"""

import random
import sys
import pygame as pg
import time

template = {
    2:["darkgoldenrod1", 65, 160],
    4:["darkmagenta", 62, 160],
    8:["aqua", 65, 160],
    16:["deeppink1", 55, 160],
    32:["firebrick2", 50, 160],
    64:["greenyellow", 50, 160],
    128:["burlywood1", 40, 160],
    256:["darkorange4", 33, 160],
    512:["yellow", 38, 160],
    1024:["slategray", 22, 162],
    2048:["black", 16, 162],
    4096:["indigo", 16, 162],
    8192:["darkblue", 24, 162]
    }

class TwentyFortyEight:
    def __init__(self):
        self.matrix = []
        self.before = []
        self.row = 4
        self.col = 4
        self.num_i = 0
        self.num_j = 0
        self.score = 0
        self.high_score = 0
        self.temp_score = 0
        self.init()
        self.win_flag = True
        self.screen_size = 830, 730
        self.width_cell = (self.screen_size[0] - 200 - 2 * 15) // self.row
        self.height_cell = (self.screen_size[1] - 100 - 2 * 15) // self.col
        self.screen = pg.display.set_mode(self.screen_size)
        self.start_flag = 0
        self.change_score = 0
        self.clicked = False
        self.screen_flag = 0
        self.continue_flag = 0

        pg.init()
        
    #default matrix creation
    def _matrixApend(self):
        self.matrix = []
        self.before = []
        for i in range(self.row):
            temp = []
            temp2 = []
            for j in range(self.col):
                temp.append(0)
                temp2.append(0)
            self.matrix.append(temp)
            self.before.append(temp2)
    
    #initialization
    def init(self):
        self.continue_flag = 0
        self.screen_flag = 0
        self.change_score = 0
        self.start_flag = 0
        self._matrixApend()  
        self.score = 0
        
        
        #generating random number for start
        num_i = random.randint(0, self.col - 1)
        num_j = random.randint(0, self.row - 1)
        for i in range(int(self.row * self.col/8)):
            while not self.matrix[num_i][num_j] == 0:
                num_i = random.randint(0, self.col - 1)
                num_j = random.randint(0, self.row - 1)
            possib = random.random()
            if possib < 0.80:
                self.matrix[num_i][num_j] = 2
            else:
                self.matrix[num_i][num_j] = 4
    
    #movig up
    def moveUp(self):
       
        self.change_score = 0
        j = 0
        while j < self.col:
            #scroll up for each cell (first)
            i = 0
            while i < self.row - 1:
                if self.matrix[i][j] == 0:
                    k = i + 1
                    flag = 0
                    while self.matrix[k][j] == 0:
                        k += 1
                        if k == self.row :
                            flag = 1
                            break
                    if flag == 0:
                        self.matrix[i][j] = self.matrix[k][j]
                        self.matrix[k][j] = 0
                i += 1
            #summation
            i = 1
            while i < self.row:
                if self.matrix[i - 1][j] == self.matrix[i][j] :
                    self.temp_score = self.matrix[i - 1][j] + self.matrix[i][j]
                    self.matrix[i - 1][j] = self.temp_score
                    self.score = self.score + self.temp_score
                    self.matrix[i][j] = 0
                    self.change_score += self.temp_score
                 
                i += 1
            #scroll up for each cell (second times)
            i = 0
            while i < self.row - 1:
                if self.matrix[i][j] == 0:
                    k = i + 1
                    flag = 0
                    while self.matrix[k][j] == 0 :
                        k += 1
                        if k == self.row :
                            flag =1
                            break
                    if flag == 0:
                        self.matrix[i][j] = self.matrix[k][j]
                        self.matrix[k][j] = 0
                i += 1
            j += 1
    
    #moving dowm        
    def moveDown(self):
        self.change_score = 0
        j = 0
        while j < self.col:
            i = self.row - 1
            while i > 0:
                if self.matrix[i][j] == 0:
                    k = i - 1
                    flag = 0
                    while self.matrix[k][j] == 0:
                        k -= 1
                        if k == -1 :
                            flag = 1
                            break
                    if flag == 0:
                        self.matrix[i][j] = self.matrix[k][j]
                        self.matrix[k][j] = 0
                i -= 1
                
            
            i = self.row - 2
            while i > -1:
                if self.matrix[i + 1][j] == self.matrix[i][j] :
                    self.temp_score = self.matrix[i + 1][j] + self.matrix[i][j]
                    self.matrix[i + 1][j] = self.temp_score
                    self.score = self.score + self.temp_score
                    self.matrix[i][j] = 0
                    self.change_score += self.temp_score
                i -= 1
            
            i = self.row - 1
            while i > 0:
                if self.matrix[i][j] == 0:
                    k = i - 1
                    flag = 0
                    while self.matrix[k][j] == 0:
                        k -= 1
                        if k == -1 :
                            flag = 1
                            break
                    if flag == 0:
                        self.matrix[i][j] = self.matrix[k][j]
                        self.matrix[k][j] = 0
                i -= 1
            j += 1       
    
    #moving right
    def moveRight(self):
        self.change_score = 0
        i = 0
        while i < self.row:
            j = self.col - 1
            while j > 0:
                if self.matrix[i][j] == 0:
                    k = j - 1
                    flag = 0
                    while self.matrix[i][k] == 0:
                        k -= 1
                        if k == -1 :
                            flag = 1
                            break
                    if flag == 0:
                        self.matrix[i][j] = self.matrix[i][k]
                        self.matrix[i][k] = 0
                j -= 1
            
            j = self.col - 2
            while j > -1:
                if self.matrix[i][j + 1] == self.matrix[i][j] :
                    self.temp_score = self.matrix[i][j + 1] + self.matrix[i][j]
                    self.matrix[i][j + 1] = self.temp_score
                    self.score = self.score + self.temp_score
                    self.matrix[i][j] = 0
                    self.change_score += self.temp_score
                j -= 1
           
            j = self.col - 1
            while j > 0:
                if self.matrix[i][j] == 0:
                    k = j - 1
                    flag = 0
                    while self.matrix[i][k] == 0:
                        k -= 1
                        if k == -1 :
                            flag = 1
                            break
                    if flag == 0:
                        self.matrix[i][j] = self.matrix[i][k]
                        self.matrix[i][k] = 0
                j -= 1
            i += 1
    
    #moving left
    def moveLeft(self):
        self.change_score = 0
        i = 0
        while i < self.row:
            j = 0
            while j < self.col - 1:
                if self.matrix[i][j] == 0:
                    k = j + 1
                    flag = 0
                    while self.matrix[i][k] == 0:
                        k += 1
                        if k == self.col :
                            flag = 1
                            break
                    if flag == 0:
                        self.matrix[i][j] = self.matrix[i][k]
                        self.matrix[i][k] = 0
                j += 1
            
            j = 1
            while j < self.col:
                if self.matrix[i][j - 1] == self.matrix[i][j] :
                    self.temp_score = self.matrix[i][j - 1] + self.matrix[i][j]
                    self.matrix[i][j - 1] = self.temp_score
                    self.score = self.score + self.temp_score
                    self.matrix[i][j] = 0
                    self.change_score += self.temp_score
                j += 1
           
            j = 0
            while j < self.col - 1:
                if self.matrix[i][j] == 0:
                    k = j + 1
                    flag = 0
                    while self.matrix[i][k] == 0:
                        k += 1
                        if k == self.col :
                            flag = 1
                            break
                    if flag == 0:
                        self.matrix[i][j] = self.matrix[i][k]
                        self.matrix[i][k] = 0
                j += 1
            i += 1
    
    #generating random numbers (after each step)               
    def random(self):
        #empty cell check
        if not self.before == self.matrix:  
            i = 0
            zero_flag = 0
            while i < self.row and zero_flag == 0:
                j = 0
                while j < self.col and zero_flag == 0:
                    if self.matrix[i][j] == 0:
                        zero_flag = 1
                    j += 1
                i+=1
                
            if zero_flag == 1:
                self.num_i = random.randint(0, self.row-1)
                self.num_j = random.randint(0, self.col-1)
                
                while not self.matrix[self.num_i][self.num_j] == 0:
                    self.num_i = random.randint(0, self.col - 1)
                    self.num_j = random.randint(0, self.row - 1) 
                possib = random.random()
                if possib < 0.80:
                    self.matrix[self.num_i][self.num_j] = 2 
                else:
                    self.matrix[self.num_i][self.num_j] = 4
    
    #keep the highest score made by the user            
    def highScore(self):
        file = "highscore.txt"
        try:
            file_input = open(file, "r+")
            self.high_score = int(file_input.read())
        except:
            file_input = open(file, "w+") 
            file_input.write(str(0))
            self.high_score = 0
        file_input.close()
       
        if self.score > self.high_score:
            self.high_score = self.score
            file_output = open(file, "w")
            file_output.write(str(self.high_score))
            file_output.close()    
    
    #undo process
    def undo(self):
        for row in range(self.row):
            for col in range(self.col):
                self.before[row][col] = self.matrix[row][col]
    
    #drawing numbers from template
    def output_numbers(self, output, row, col, control = 0):
        
        font = pg.font.SysFont('bahnschrift', int(self.height_cell / 2.4))
        offset =  int(self.height_cell/18)        
        n_text = font.render(str(output), True, pg.Color(template.get(output)[0]))
        self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + offset + template.get(output)[1], (row * self.height_cell) - offset + template.get(output)[2]))

    #drawing texts and others
    def draw_numbers(self, control = 0):
        
        font_star = pg.font.SysFont('bahnschrift', self.height_cell // 3)    
        font_score = pg.font.SysFont('bahnschrift', self.height_cell // 3)
        text_score = font_score.render("Score", True, pg.Color('black'))
        text_high = font_score.render("High", True, pg.Color('black'))
        number_score = font_score.render(str(self.score), True, pg.Color('black'))
        number_high_score = font_score.render(str(self.high_score), True, pg.Color('black'))
        self.screen.blit(text_score, pg.Vector2((self.screen_size[0] - 185), 110))
        self.screen.blit(text_high, pg.Vector2((self.screen_size[0] - 185), 310))
        self.screen.blit(text_score, pg.Vector2((self.screen_size[0] - 185), 360))
        self.screen.blit(number_score, pg.Vector2((self.screen_size[0] - 185), 180))
        self.screen.blit(number_high_score, pg.Vector2((self.screen_size[0] - 185), 430))
                         
        row = 0
        while row < self.row:
            col = 0
            while col < self.col:
                output = self.matrix[row][col]
                if not output == 0:
                    if self.num_i == row and self.num_j == col and control == 0 and self.start_flag == 1:
                        self.output_numbers(output, row, col, 1)
                        if output == 2:
                            n_text = font_star.render("*", True, pg.Color("darkgoldenrod1"))
                            self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + 50, (row * self.height_cell) + 155))
                        elif output == 4:
                            n_text = font_star.render("*", True, pg.Color('darkmagenta'))
                            self.screen.blit(n_text, pg.Vector2((col * self.width_cell) + 50, (row * self.height_cell) + 155))
                        
                    else:
                        self.output_numbers(output, row, col)
                col += 1
            row += 1    
                
    #drawing background and grids
    def draw_background(self, control = 0):
        if control == 0:
            self.screen.fill(pg.Color("white"))
            pg.draw.rect(self.screen, pg.Color("black"), pg.Rect(15,115,self.screen_size[0] - 200 - 2 * 15,self.screen_size[1] - 100 - 2 * 15),5)
            
            i = 1
            while (i * self.width_cell) < (self.screen_size[0] - 200 - 2 * 15):
                pg.draw.line(self.screen, pg.Color("black"), pg.Vector2((i * self.width_cell) + 15, 115), pg.Vector2((i * self.width_cell) + 15, self.screen_size[1] - 15 - 3) , 5)
                i += 1
                
            i = 1
            while (i * self.height_cell) < (self.screen_size[1] - 100 - 2 * 15):
                pg.draw.line(self.screen, pg.Color("black"), pg.Vector2(15, (i * self.height_cell) + 115), pg.Vector2(self.screen_size[0] - 200 - 15 - 3, (i * self.height_cell) + 115), 5)
                i += 1
       
        
    #create buttons        
    def button(self):
       
        restart_rect = pg.draw.rect(self.screen, pg.Color("black"), pg.Rect(100,30,170,50),5)
        undo_rect = pg.draw.rect(self.screen, pg.Color("black"), pg.Rect(370,30,170,50),5)
        
        font_button = pg.font.SysFont('bahnschrift', self.height_cell // 4)
        text_restart = font_button.render("RESTART", True, pg.Color('black'))
        text_undo = font_button.render("UNDO", True, pg.Color('black'))
        self.screen.blit(text_restart, pg.Vector2(107, 31))
        self.screen.blit(text_undo, pg.Vector2(407, 31))
        
        #Get mouse position
        
        position = pg.mouse.get_pos()
        
        #Clicked conditions for restart
        if restart_rect.collidepoint(position):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.init()
                self.clicked = True
            
         
        #Clicked conditions for undo
        if undo_rect.collidepoint(position):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False: 
                for row in range(self.row):
                    for col in range(self.col):
                        self.matrix[row][col] = self.before[row][col]
                self.score = self.score - self.change_score
                self.change_score = 0
                self.clicked = True
                
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
    #game over screen
    def game_over(self):
        if self.screen_flag == 1:
            self.screen.fill(pg.Color("white"))        
            
            
            restart_rect = pg.draw.rect(self.screen, pg.Color("black"), pg.Rect(self.screen_size[0] // 2 - 100, self.screen_size[1] // 2 - 25,200,50),5)
                        
            font_button = pg.font.SysFont('bahnschrift', self.height_cell // 4 )
            font_text = pg.font.SysFont('bahnschrift', self.height_cell // 2 )
            text_game_over = font_text.render("GAME OVER !", True, pg.Color('black'))
            text_new_game = font_button.render("NEW GAME", True, pg.Color('black'))
            self.screen.blit(text_game_over, pg.Vector2(190, 100))
            self.screen.blit(text_new_game, pg.Vector2(self.screen_size[0] // 2 - 95, self.screen_size[1] // 2 - 25))  
            pg.display.update()
            
            self.clicked == False
            position = pg.mouse.get_pos()
            if restart_rect.collidepoint(position):
                if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.init()
                    self.clicked = True
    #win screen                
    def win(self):
        if self.screen_flag == 2:
            self.screen.fill(pg.Color("white"))        
            
            restart_rect = pg.draw.rect(self.screen, pg.Color("black"), pg.Rect(self.screen_size[0] // 2 - 205, self.screen_size[1] // 2 - 25,200,50),5)
            continue_rect = pg.draw.rect(self.screen, pg.Color("black"), pg.Rect(self.screen_size[0] // 2 + 25, self.screen_size[1] // 2 - 25,200,50),5)
                        
            font_button = pg.font.SysFont('bahnschrift', self.height_cell // 4 )
            font_text = pg.font.SysFont('bahnschrift', self.height_cell // 2 )
            text_game_over = font_text.render("WIN!", True, pg.Color('black'))
            text_new_game = font_button.render("NEW GAME", True, pg.Color('black'))
            text_continue = font_button.render("CONTINUE", True, pg.Color('black'))
            self.screen.blit(text_game_over, pg.Vector2(330, 100))
            self.screen.blit(text_new_game, pg.Vector2(self.screen_size[0] // 2 - 200, self.screen_size[1] // 2 - 25))  
            self.screen.blit(text_continue, pg.Vector2(self.screen_size[0] // 2 + 38, self.screen_size[1] // 2 - 25))  
            pg.display.update()
            
            self.clicked == False
            position = pg.mouse.get_pos()
            if restart_rect.collidepoint(position):
                if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    print(2)            
                    self.init()
                    self.clicked = True

            self.clicked == False
            
            if continue_rect.collidepoint(position):
                if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.screen_flag = 0
                    self.continue_flag = 1
                    self.clicked = True
                    time.sleep(0.5)
            
               
    def game_loop(self):
         for event in pg.event.get():
             if event.type == pg.QUIT:
                 pg.quit()
                 sys.exit()
             if event.type == pg.KEYDOWN:
                 if event.key == pg.K_UP: #Up
                     self.start_flag = 1
                     self.undo()
                     self.moveUp()
                     self.draw_background()
                     self.button()
                     self.draw_numbers(1)
                     pg.display.flip()
                     time.sleep(0.2)
                     self.random()
                     
                 elif event.key == pg.K_DOWN: #Down
                     self.start_flag = 1
                     self.undo()
                     self.moveDown()
                     self.draw_background()
                     self.button()
                     self.draw_numbers(1)
                     pg.display.flip()
                     time.sleep(0.2)
                     self.random()
                     
                 elif event.key == pg.K_RIGHT: #Right
                     self.start_flag = 1
                     self.undo()
                     self.moveRight()
                     self.draw_background()
                     self.button()
                     self.draw_numbers(1)
                     pg.display.flip()
                     time.sleep(0.2)
                     self.random()
                 
                 elif event.key == pg.K_LEFT: #Left
                     self.start_flag = 1
                     self.undo()    
                     self.moveLeft()
                     self.draw_background()
                     self.button()
                     self.draw_numbers(1)
                     pg.display.flip()
                     time.sleep(0.2)
                     self.random()
                 
                 elif event.key == pg.K_r: #Restart
                     self.init()
                 
                 elif event.key == pg.K_x: #Undo
                     for row in range(self.row):
                         for col in range(self.col):
                             self.matrix[row][col] = self.before[row][col]
                     self.score = self.score - self.change_score
                     self.change_score = 0
                     
         if self.screen_flag == 0:
            self.highScore()
            self.draw_background()
            self.draw_numbers()
            self.button()
         elif self.screen_flag == 1:
             self.game_over()
         elif self.screen_flag == 2:
             self.win()

         pg.display.set_caption('2048')
         pg.display.flip()
         pg.display.update()

    
    def lose_control(self):
        count = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.matrix[i][j] == 0:
                    count += 1
        if count == 0:
            flag_equal = 0
            for i in range(self.row-1):
                for j in range(self.col-1):
                    if self.matrix[i][j] == self.matrix[i][j+1] or self.matrix[i][j] == self.matrix[i+1][j]:
                        flag_equal = 1
            if flag_equal == 0:
                if not  (self.matrix[self.row-1][self.col-1] == self.matrix[self.row-2][self.col-1]) and  not (self.matrix[self.row-1][self.col-1] == self.matrix[self.row-1][self.col-2]):
                    self.screen_flag = 1 # gameover
                    time.sleep(0.5)
                    
    def win_control(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.matrix[i][j] == 2048:
                    self.screen_flag = 2
                    #time.sleep(0.5)
                    break
            if self.screen_flag == 2:
                break
    
    def run(self):
        while self.win_flag == True:
            self.game_loop()   
            if self.screen_flag == 0:
                self.lose_control()
                if self.continue_flag == 0:
                    self.win_control()

           
        pg.quit()
        sys.exit()
                    

matris = TwentyFortyEight()
matris.run()
