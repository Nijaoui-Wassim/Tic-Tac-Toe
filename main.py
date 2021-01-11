#space invader (ship and bullets)
import math
import random
import pygame
from pygame import mixer

#grid size
num_of_coll = 3
#margin between squares in pixels
margin = 5

#initializing pygame
pygame.init()

#init score
score_value = 0

#define fonts
font = pygame.font.Font("assets//Sportive-Regular.ttf", 32)
font2 = pygame.font.Font("assets//font2.otf", 100)

#font size
TextX = 10
TextY = 10

#creating game window
screen_w = 800
screen_h = 600
screen = pygame.display.set_mode((screen_w,screen_h))

#change title
pygame.display.set_caption("TikTacToe")

#change icon
icon = pygame.image.load("assets//o.png") #define icon

pygame.display.set_icon(icon)             #set the icon

current_move = 1

#both icons from Flaticon by Freepik
#add 2 images
x_move = pygame.image.load("assets//x_128.png") #define x 128px
o_move = pygame.image.load("assets//o_128.png") #define o 128px
neutre = pygame.image.load("assets//neutre.png") #define o 128px


#Load background image
#bg = pygame.image.load("assets//background.jpg")
bg = pygame.image.load("assets//blue.jpg")

#Load background music
mixer.music.load("assets//bck_music.mp3")
# mixer.music.play(-1)

game_ended = False
end_line_index1 = 0
end_line_index2 = 0
Color_line=(0,255,0)
count_till_endscreen = 0
winner ="TIE"

boxes =[]
image_X =[]
image_Y =[]
values =[]
X_init= screen_w/9
Y_init= screen_h*(1/9)
box_side = 128
StepY= box_side + num_of_coll*margin

X_init= X_init - box_side
Y_init = Y_init-StepY

for i in range(num_of_coll):
    Y_init = Y_init + StepY
    temp_jump = 128
    for j in range(num_of_coll):
        boxes.append(pygame.Rect(temp_jump, Y_init , box_side, box_side))
        box_state = "show"
        image_X.append(temp_jump)
        image_Y.append(Y_init)
        temp_jump = X_init+margin*num_of_coll + box_side + box_side + temp_jump
        values.append("nothing")

print(boxes)

#rect_pipe_down = pygame.Rect(pipe_X[i], temp_h-20 , 64, screen_h-temp_h)  
            
#  pygame.draw.rect(screen, [255, 0, 0], rect_player, 0)

def game_over(x,y, winner):
    screen.fill((255,255,255,0.5)) #change background color - RGB
    game_o = font2.render("GAME OVER",True, (0, 0, 0))
    winsc = font2.render('"'+ winner.upper() + '" is the WINNER',True, (0, 0, 0))
    screen.blit(game_o, (x, y))
    screen.blit(winsc, (x, y+200))

def draw_winner(ind1, ind2):
    global end_line_index1, end_line_index2
    Color_line=(0,255,0)
    end_line_index1 = boxes[ind1].center
    end_line_index2 = boxes[ind2].center
    pygame.draw.line(screen, Color_line, end_line_index1 , end_line_index2)
    
def set_pictures(IND):
    if values[IND] == "nothing":
        screen.blit(neutre, (image_X[IND], image_Y[IND]))
    elif values[IND] == "x":
        screen.blit(x_move, (image_X[IND], image_Y[IND]))
    elif values[IND] == "o":
        screen.blit(o_move, (image_X[IND], image_Y[IND]))


def show_score(x,y):
    score = font.render("Score : " + str(score_value),True, (255, 255, 255))
    screen.blit(score, (x, y))

running = True


while running:
    #INSIDE OF THE GAME LOOP
    screen.blit(bg, (0, 0))
    
    for event in pygame.event.get():      #get all user events
        try:
            if event.type == pygame.QUIT:     # pressing the close button = Pygame.Quit
                running = False               #quit the window
                pygame.display.quit()
                pygame.quit()       #closing window - add quit event
                break
            #get MOUSE clicks
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                #collidepoint(x, y)
                for box in boxes:
                    index = boxes.index(box)
                    if box.collidepoint(pos) and values[index] == "nothing":
                        print("You did CLICK this box ",box)
                        if current_move ==1:
                            current_move = 0                            
                            values[index] = "x"
                        else:
                            current_move = 1
                            values[index] = "o"                           
                            

                
        except Exception as e:
            print(e)
        
    #anything that you want to stay inside thescreen need to be inside the while loop
 
    try:  
        for box in boxes:
            pygame.draw.rect(screen, [255, 255, 255], box, 1)
            index = boxes.index(box)
            set_pictures(index)
        
        if not game_ended:
            #looking for winner
            #vertical
            for i in range(3):    
                if values[i*num_of_coll] == values[i*num_of_coll+1] and values[i*num_of_coll+1] == values[i*num_of_coll+2] and values[i*num_of_coll] != "nothing":
                    print("Player " +values[i*num_of_coll] + " is the WINNER")
                    winner = values[i*num_of_coll]
                    draw_winner(i*num_of_coll , i*num_of_coll+2)
                    game_ended = True
            #horizontal
            for i in range(3):    
                if values[i] == values[i+num_of_coll] and values[i+num_of_coll] == values[i+num_of_coll*2]  and values[i] != "nothing":
                    print("Player " +values[i] + " is the WINNER")
                    winner = values[i]
                    draw_winner(i, i+num_of_coll*2)
                    game_ended = True

            if values[0] == values[4] and values[4] == values[8] and values[4] != "nothing":
                print("Player " +values[0] + " is the WINNER") 
                draw_winner(0, 8)
                winner = values[0]
                game_ended = True

            if values[2] == values[4] and values[4] == values[6] and values[4] != "nothing":
                print("Player " +values[2] + " is the WINNER")   
                draw_winner(2, 6)
                winner = values[2]
                game_ended = True
            counter = 0
            for i in range(len(boxes)):
                if (values[i] == "nothing"):
                    counter += 1
            if counter == 0:
                print("TIE")   
                #draw_winner(2, 4)
                game_ended = True            
        if game_ended:
            if count_till_endscreen> 1000:
                game_over((screen_w/2)-120, (screen_h/2)-40, winner)
            else:
                pygame.draw.line(screen, Color_line, end_line_index1 , end_line_index2 , 9)
                count_till_endscreen += 1
        pygame.display.update()   #to update screen            

        
    except Exception as e:
        print(e)
