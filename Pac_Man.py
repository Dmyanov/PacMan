import pygame
import sys
import random

class Game:
    #Game initialisation
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 625), pygame.RESIZABLE) 
        pygame.display.set_caption("PacMan") 
        self.path = "C:\\Users\\denis\\Desktop\\pacman"
        self.clock = pygame.time.Clock() 
        self.text_font = pygame.font.Font(None, 40)
        self.map = Map(self.path, self.screen) 
        self.red_Ghost = Red_Ghost(self.map.get_barrier_array(), self.path + "/red_ghost.png", self.path + "/frightend_mode.png", self.path + "/home_mode.png", self.screen) 
        self.pink_Ghost = Pink_Ghost(self.map.get_barrier_array(), self.path + "/pink_ghost.png", self.path + "/frightend_mode.png", self.path + "/home_mode.png", self.screen)
        self.blue_Ghost = Blue_Ghost(self.map.get_barrier_array(), self.path + "/blue_ghost.png", self.path + "/frightend_mode.png", self.path + "/home_mode.png", self.screen)
        self.orange_Ghost = Orange_Ghost(self.map.get_barrier_array(),self.path + "/orange_ghost.png", self.path + "/frightend_mode.png", self.path + "/home_mode.png", self.screen)
        self.Player = PacMan(self.path, self.map.get_barrier_array(), self.map.get_coin_array(), self.map.get_power_pellet_array(), self.screen, self.text_font)
        self.gamemode = "played"
        self.start_time = pygame.time.get_ticks()
        
        self.game_loop()
        
    #Loop in where the game logic is placed
    def game_loop(self):
        while True:
            while self.gamemode == "played":
                self.events()
                if self.red_Ghost.collision(self.Player.player_pos_x, self.Player.player_pos_y) == "paused": 
                    if self. red_Ghost.frightend_mode == False and self.red_Ghost.home_mode == False:
                        self.gamemode = "paused"
                    if self.red_Ghost.frightend_mode == True:
                        self.red_Ghost.frightend_mode = False
                        self.red_Ghost.home_mode = True
                        self.red_Ghost.turn()
                if self.pink_Ghost.collision(self.Player.player_pos_x, self.Player.player_pos_y) == "paused":
                    if self. pink_Ghost.frightend_mode == False and self.pink_Ghost.home_mode == False:
                        self.gamemode = "paused"
                    if self.pink_Ghost.frightend_mode == True:
                        self.pink_Ghost.frightend_mode = False
                        self.pink_Ghost.home_mode = True
                        self.pink_Ghost.turn()
                if self.blue_Ghost.collision(self.Player.player_pos_x, self.Player.player_pos_y) == "paused":
                    if self. blue_Ghost.frightend_mode == False and self.blue_Ghost.home_mode == False:
                        self.gamemode = "paused"
                    if self.blue_Ghost.frightend_mode == True:
                        self.blue_Ghost.frightend_mode = False
                        self.blue_Ghost.home_mode = True
                        self.blue_Ghost.turn()
                if self.orange_Ghost.collision(self.Player.player_pos_x, self.Player.player_pos_y) == "paused":
                    if self.orange_Ghost.frightend_mode == False and self.orange_Ghost.home_mode == False:
                        self.gamemode = "paused"
                    if self.orange_Ghost.frightend_mode == True:
                        self.orange_Ghost.frightend_mode = False
                        self.orange_Ghost.home_mode = True
                        self.orange_Ghost.turn()
                
                self.Player.player_movement()
                
                self.map.draw_map() 
                self.Player.draw_player(self.red_Ghost, self.pink_Ghost, self.blue_Ghost, self.orange_Ghost)
                self.Player.draw_score() 
                

                self.red_Ghost.calc_target(self.Player.player_pos_x, self.Player.player_pos_y)
                self.red_Ghost.draw_ghost(self.screen)

                self.pink_Ghost.calc_target(self.Player.player_pos_x, self.Player.player_pos_y, self.Player.player_direction)
                self.pink_Ghost.draw_ghost(self.screen)
                
                self.blue_Ghost.calc_target(self.red_Ghost.ghost_pos_x, self.red_Ghost.ghost_pos_y, self.pink_Ghost.target_x_pos, self.pink_Ghost.target_y_pos)
                self.blue_Ghost.draw_ghost(self.screen)
                
                self.orange_Ghost.calc_target(self.Player.player_pos_x, self.Player.player_pos_y)
                self.orange_Ghost.draw_ghost(self.screen)
                pygame.display.update()
                self.clock.tick(60)
            while self.gamemode == "paused":
                self.events()
                self.map.draw_map()
                self.Player.draw_player(self.red_Ghost, self.pink_Ghost, self.blue_Ghost, self.orange_Ghost)
                self.Player.draw_score()
                pygame.display.update()
                self.clock.tick(60) 
    #events checking for Player input and changing the state of the Ghosts depending on how long the game is running
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:    
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_UP:
                    self.Player.move_up()
                if event.key == pygame.K_DOWN:
                    self.Player.move_down()
                if event.key == pygame.K_LEFT:
                    self.Player.move_left()
                if event.key == pygame.K_RIGHT:
                    self.Player.move_right()
        if 7000 < pygame.time.get_ticks()-self.start_time < 7017:
            self.red_Ghost.mode = "chase"
            self.pink_Ghost.mode = "chase"
            self.blue_Ghost.mode = "chase"
            self.orange_Ghost.mode = "chase"
        if 27000 < pygame.time.get_ticks()-self.start_time < 27017:
            self.red_Ghost.mode = "scatter"
            self.pink_Ghost.mode = "scatter"
            self.blue_Ghost.mode = "scatter"
            self.orange_Ghost.mode = "scatter"
        if 34000 < pygame.time.get_ticks()-self.start_time < 34017:
            self.red_Ghost.mode = "chase"
            self.pink_Ghost.mode = "chase"
            self.blue_Ghost.mode = "chase"
            self.orange_Ghost.mode = "chase"
        if 54000 < pygame.time.get_ticks()-self.start_time < 54017:
            self.red_Ghost.mode = "scatter"
            self.pink_Ghost.mode = "scatter"
            self.blue_Ghost.mode = "scatter"
            self.orange_Ghost.mode = "scatter"
        if 59000 < pygame.time.get_ticks()-self.start_time < 59017:
            self.red_Ghost.mode = "chase"
            self.pink_Ghost.mode = "chase"
            self.blue_Ghost.mode = "chase"
            self.orange_Ghost.mode = "chase"
        if 79000 < pygame.time.get_ticks()-self.start_time < 79017:
            self.red_Ghost.mode = "scatter"
            self.pink_Ghost.mode = "scatter"
            self.blue_Ghost.mode = "scatter"
            self.orange_Ghost.mode = "scatter"
        if 84000 < pygame.time.get_ticks()-self.start_time < 84017:
            self.red_Ghost.mode = "chase"
            self.pink_Ghost.mode = "chase"
            self.blue_Ghost.mode = "chase"
            self.orange_Ghost.mode = "chase"
        if self.Player.score == 271:
            self.gamemode = "paused"
class PacMan:
    def __init__(self, path, map_barrier_array, coin_array, power_pellet_array, screen, text_font): 
        self.player_skin_up = pygame.image.load(path + "/pac_man_1_up.png")
        self.player_skin_down = pygame.image.load(path + "/pac_man_1_down.png")
        self.player_skin_left = pygame.image.load(path + "/pac_man_1_left.png")
        self.player_skin_right = pygame.image.load(path + "/pac_man_1_right.png")
        self.player_skin_closed = pygame.image.load(path + "/pac_man_2.png")
        self.aktueller_player_skin = self.player_skin_left 
        self.draw_skin = self.aktueller_player_skin 
        self.skin_counter = 0  
        self.SPEED = 1.5625 
        self.speed = self.SPEED 
        self.player_pos_x = 300 
        self.player_pos_y = 150
        self.player_direction = "left"   
        self.next_move = ""
        self.barrier_array = map_barrier_array 
        self.score = 0 
        self.coin_array = coin_array 
        self.power_pellet_array = power_pellet_array 
        self.start_frightend_time = 9000000000000 
        self.screen = screen 
        self.text_font = text_font 
        self.score_text = self.text_font.render("Score: " + str(self.score), False, (255,255,255))
        
    def move_up(self):
        for barrier in self.barrier_array:
            if barrier.y_pos_barrier < self.player_pos_y <= (barrier.y_pos_barrier + 25): 
                if (barrier.x_pos_barrier - 25)  < self.player_pos_x < (barrier.x_pos_barrier + 25):
                    self.next_move = "up"                  
                    return
        self.player_direction = "up"
        self.next_move = ""
        self.speed = self.SPEED
        self.aktueller_player_skin = self.player_skin_up 
    def move_down(self):
        for barrier in self.barrier_array:
            if barrier.y_pos_barrier <= (self.player_pos_y + 25) < (barrier.y_pos_barrier + 25):
                if (barrier.x_pos_barrier - 25) < self.player_pos_x < (barrier.x_pos_barrier + 25):
                    self.next_move = "down"
                    return
        if (self.player_pos_x, self.player_pos_y) == (300, 250): 
            return
        self.player_direction = "down"
        self.next_move = "" 
        self.speed = self.SPEED
        self.aktueller_player_skin = self.player_skin_down
    def move_left(self):
        for barrier in self.barrier_array:
            if (barrier.y_pos_barrier - 25) < self.player_pos_y < (barrier.y_pos_barrier + 25):
                if (barrier.x_pos_barrier) < self.player_pos_x <= (barrier.x_pos_barrier + 25):
                    self.next_move = "left"
                    return
        self.player_direction = "left"
        self.next_move = ""
        self.speed = self.SPEED
        self.aktueller_player_skin = self.player_skin_left
    def move_right(self):
        for barrier in self.barrier_array:
            if (barrier.y_pos_barrier - 25) < self.player_pos_y < (barrier.y_pos_barrier + 25):
                if (barrier.x_pos_barrier) <= (self.player_pos_x + 25) < (barrier.x_pos_barrier + 25):
                    self.next_move = "right"
                    return
        self.player_direction = "right"
        self.next_move = ""
        self.speed = self.SPEED
        self.aktueller_player_skin = self.player_skin_right
    def player_movement(self):
        if self.player_direction == "up":
            self.player_pos_y -= self.speed 
        elif self.player_direction == "down":
            self.player_pos_y += self.speed
        elif self.player_direction == "left":
            self.player_pos_x -= self.speed
        elif self.player_direction == "right":
            self.player_pos_x += self.speed
        if (self.player_pos_x, self.player_pos_y) == (0, 300) and self.player_direction == "left":
            self.player_pos_x, self.player_pos_y = 600, 300 
        if (self.player_pos_x, self.player_pos_y) == (600, 300) and self.player_direction == "right":
            self.player_pos_x, self.player_pos_y = 0, 300
        if self.player_pos_y == 300 and self.player_pos_x > 600:
            self.player_pos_x = 590
        
        if self.next_move == "up":
            self.move_up()
        if self.next_move == "down":
            self.move_down()
        if self.next_move == "left":
            self.move_left()
        if self.next_move == "right":
            self.move_right()        
                

    def draw_player(self, red_Ghost, pink_Ghost, blue_Ghost, orange_Ghost):
        self.colission_detection(red_Ghost, pink_Ghost, blue_Ghost, orange_Ghost)
        if self.skin_counter % 7 == 0: 
            if self.skin_counter % 2 == 0:
                self.draw_skin = self.player_skin_closed
                self.skin_counter +=1
            else:
                self.draw_skin = self.aktueller_player_skin
                self.skin_counter += 1
        else:
            self.skin_counter += 1
        self.screen.blit(self.draw_skin, (self.player_pos_x, self.player_pos_y)) 
    def draw_score(self):
        self.screen.blit(self.score_text, (700, 200)) 
        
    def colission_detection(self, red_Ghost, pink_Ghost, blue_Ghost, orange_Ghost):
        if self.player_direction == "up":
            for barrier in self.barrier_array:
                if self.player_pos_x == barrier.x_pos_barrier:
                    if barrier.y_pos_barrier <= self.player_pos_y <= (barrier.y_pos_barrier + 25):
                        self.speed = 0
                    
        elif self.player_direction == "down":
            for barrier in self.barrier_array:
                if self.player_pos_x == barrier.x_pos_barrier:
                    if barrier.y_pos_barrier <= (self.player_pos_y + 25) <= (barrier.y_pos_barrier + 25):
                        self.speed = 0

        elif self.player_direction == "right":
            for barrier in self.barrier_array:
                if self.player_pos_y == barrier.y_pos_barrier:
                    if barrier.x_pos_barrier <= (self.player_pos_x + 25) <= (barrier.x_pos_barrier + 25):
                        self.speed = 0

        elif self.player_direction == "left":
            for barrier in self.barrier_array:
                if self.player_pos_y == barrier.y_pos_barrier:
                    if barrier.x_pos_barrier <= self.player_pos_x <= (barrier.x_pos_barrier + 25):
                        self.speed = 0

        for coin in self.coin_array: 
            if (self.player_pos_x, self.player_pos_y) == (coin.x_pos, coin.y_pos): 
                self.coin_array.remove(coin)
                self.score +=1
                self.score_text = self.text_font.render("Score: " + str(self.score), False, (255,255,255))
        for pellet in self.power_pellet_array: 
            if (self.player_pos_x, self.player_pos_y) == (pellet.x_pos, pellet.y_pos): 
                self.power_pellet_array.remove(pellet) 
                red_Ghost.turn() 
                pink_Ghost.turn()
                blue_Ghost.turn()
                orange_Ghost.turn()
                red_Ghost.frightend_mode = True 
                pink_Ghost.frightend_mode = True
                blue_Ghost.frightend_mode = True
                orange_Ghost.frightend_mode = True
                
                self.start_frightend_time = pygame.time.get_ticks()
        if (pygame.time.get_ticks() - self.start_frightend_time) > 5000: 
                red_Ghost.frightend_mode = False
                pink_Ghost.frightend_mode = False
                blue_Ghost.frightend_mode = False
                orange_Ghost.frightend_mode = False
class Map():
    def __init__(self, path, screen):
               
        self.map_buildings = open(path + "/map.txt", "r")
        self.background = pygame.image.load(path + "/background.png")
        self.map_array = [] 
        self.map_barrier_array = [] 
        self.coin_array = [] 
        self.power_pellet_array = [] 
        self.screen = screen
        
        for i in range(25):
            self.map_array.append(self.map_buildings.readline()) 
            self.map_array[i] = self.map_array[i][:-1] 
           
        for j in range(len(self.map_array)): 
            for k in range(len(self.map_array[j])): 
                if self.map_array[j][k] == "x": 
                    self.map_barrier_array.append(Barrier(25*k, 25*j, path))
                if self.map_array[j][k] == "*":
                    self.coin_array.append(Coin(25*k, 25*j, path))
                if self.map_array[j][k] == "+":
                    self.power_pellet_array.append(Power_Pellet(25*k, 25*j, path))
        
    
    def draw_map(self):
        self.screen.blit(self.background, (0, 0)) 
        for element in self.map_barrier_array: 
            self.screen.blit(element.barrier_skin, (element.x_pos_barrier, element.y_pos_barrier))
        for element in self.coin_array: 
            self.screen.blit(element.skin, (element.x_pos, element.y_pos))
        for element in self.power_pellet_array:
            self.screen.blit(element.skin, (element.x_pos, element.y_pos))
    def get_barrier_array(self):
        return self.map_barrier_array 
    def get_coin_array(self):  
        return self.coin_array
    def get_power_pellet_array(self):  
        return self.power_pellet_array
        

class Barrier():
    def __init__(self, x_pos, y_pos, path):  
        self.barrier_skin = pygame.image.load(path + "/barrier.png")
        self.x_pos_barrier = x_pos
        self.y_pos_barrier = y_pos
#class Enemy
class Coin():
    def __init__(self, x_pos, y_pos, path): 
        self.skin = pygame.image.load(path + "/coin.png")
        self.x_pos = x_pos
        self.y_pos = y_pos
class Power_Pellet():
    def __init__(self, x_pos, y_pos, path): 
        self.skin = pygame.image.load(path + "/power_pellet.png")
        self.x_pos = x_pos
        self.y_pos = y_pos

#parent Ghost class
class Ghost():
    def __init__(self, target_x_pos, target_y_pos, ghost_pos_x, ghost_pos_y, barrier_array, facing_direction, skin, frightend_skin, home_skin): 
        self.target_x_pos = target_x_pos
        self.target_y_pos = target_y_pos
        self.ghost_pos_x = ghost_pos_x
        self.ghost_pos_y = ghost_pos_y
        self.barrier_array = barrier_array
        self.last_move = facing_direction
        self.ghost_direction = ""
        self.speed = 1.25
        self.real_skin = pygame.image.load(skin)
        self.skin = self.real_skin
        self.frightend_skin = pygame.image.load(frightend_skin)
        self.home_skin = pygame.image.load(home_skin)
        self.mode = "scatter"
        self.frightend_mode = False
        self.home_mode = False
    def check_move_up(self): 
        for barrier in self.barrier_array:
            if barrier.y_pos_barrier < self.ghost_pos_y <= (barrier.y_pos_barrier + 25):
                if (barrier.x_pos_barrier - 25)  < self.ghost_pos_x < (barrier.x_pos_barrier + 25):                
                    return
        
        return "up"
    def check_move_down(self):
        for barrier in self.barrier_array:
            if barrier.y_pos_barrier <= (self.ghost_pos_y + 25) < (barrier.y_pos_barrier + 25):
                if (barrier.x_pos_barrier - 25) < self.ghost_pos_x < (barrier.x_pos_barrier + 25):
                    return
        if (self.ghost_pos_x, self.ghost_pos_y) == (300, 250):
            return
        return "down"
    def check_move_left(self):
        for barrier in self.barrier_array:
            if (barrier.y_pos_barrier - 25) < self.ghost_pos_y < (barrier.y_pos_barrier + 25):
                if (barrier.x_pos_barrier) < self.ghost_pos_x <= (barrier.x_pos_barrier + 25):
                    
                    return
        
        return "left"
    def check_move_right(self):
        for barrier in self.barrier_array:
            if (barrier.y_pos_barrier - 25) < self.ghost_pos_y < (barrier.y_pos_barrier + 25):
                if (barrier.x_pos_barrier) <= (self.ghost_pos_x + 25) < (barrier.x_pos_barrier + 25):
                    return
        return "right"
    def turn(self):
        if self.ghost_direction == "up":
            self.ghost_direction = "down"
            self.last_move = "down"
        elif self.ghost_direction == "down":
            self.ghost_direction = "up"
            self.last_move = "up"
        elif self.ghost_direction == "left":
            self.ghost_direction = "right"
            self.last_move = "right"
        elif self.ghost_direction == "right":
            self.ghost_direction = "left"
            self.last_move = "left"
    def calc_next_move(self, x_pos, y_pos):
        
        if self.frightend_mode == True:
            self.skin = self.frightend_skin
            self.dir_poss = [] 
            if self.last_move == "up":
                if self.check_move_up() == "up":
                    self.dir_poss.append("up")
                if self.check_move_left() == "left":
                    self.dir_poss.append("left")
                if self.check_move_right() == "right":
                    self.dir_poss.append("right")

            if self.last_move == "down":
                if self.check_move_down() == "down":
                    self.dir_poss.append("down")
                if self.check_move_left() == "left":
                    self.dir_poss.append("left")
                if self.check_move_right() == "right":
                    self.dir_poss.append("right")

            if self.last_move == "left":
                if self.check_move_up() == "up":
                    self.dir_poss.append("up")
                if self.check_move_left() == "left":
                    self.dir_poss.append("left")
                if self.check_move_down() == "down":
                    self.dir_poss.append("down")

            if self.last_move == "right":
                if self.check_move_up() == "up":
                    self.dir_poss.append("up")
                if self.check_move_down() == "down":
                    self.dir_poss.append("down")
                if self.check_move_right() == "right":
                    self.dir_poss.append("right")
            
            self.ghost_direction = random.choice(self.dir_poss) 
        if self.home_mode == True:
            if (self.ghost_pos_x % 2.5) != 0: 
                self.ghost_pos_x += 1.25
            if (self.ghost_pos_y % 2.5) != 0:
                self.ghost_pos_y += 1.25
            self.speed = 2.5 
            self.min_dist = 900000000 
            self.skin = self.home_skin  
            self.target_x_pos = 300
            self.target_y_pos = 200
            if (self.ghost_pos_x, self.ghost_pos_y) == (275, 250):
                (self.target_x_pos, self.target_y_pos) = (300, 250)
            if (self.ghost_pos_x, self.ghost_pos_y) == (325, 250):
                (self.target_x_pos, self.target_y_pos) = (300, 250)
            if (self.ghost_pos_x, self.ghost_pos_y) == (300, 250):
                self.last_move = "down"
                self.ghost_direction = "down"
                self.ghost_pos_y += self.speed
            if (self.ghost_pos_x, self.ghost_pos_y) == (300, 300):
                self.home_mode = False
                self.speed = 1.25
                self.turn()

            if self.last_move == "up":
                if self.check_move_up() == "up": 
                    if abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y-25-self.target_y_pos)**2 < self.min_dist: 
                        self.ghost_direction = "up"
                        self.min_dist = abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y-25-self.target_y_pos)**2
                if self.check_move_left() == "left":
                    if abs(self.ghost_pos_x-25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "left"
                        self.min_dist = abs(self.ghost_pos_x-25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2
                if self.check_move_right() == "right":
                    if abs(self.ghost_pos_x+25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "right"
                        self.min_dist = abs(self.ghost_pos_x+25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2
            if self.last_move == "down":
                if self.check_move_left() == "left":
                    if abs(self.ghost_pos_x-25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "left"
                        self.min_dist = abs(self.ghost_pos_x-25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2
                if self.check_move_down() == "down":
                    if abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y+25-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "down"
                        self.min_dist = abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y+25-self.target_y_pos)**2
                if self.check_move_right() == "right":
                    if abs(self.ghost_pos_x+25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "right"
                        self.min_dist = abs(self.ghost_pos_x+25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2
            if self.last_move == "left":
                if self.check_move_up() == "up":
                    if abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y-25-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "up"
                        self.min_dist = abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y-25-self.target_y_pos)**2
                if self.check_move_left() == "left":
                    if abs(self.ghost_pos_x-25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "left"
                        self.min_dist = abs(self.ghost_pos_x-25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2
                if self.check_move_down() == "down":
                    if abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y+25-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "down"
                        self.min_dist = abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y+25-self.target_y_pos)**2
            if self.last_move == "right":
                if self.check_move_up() == "up":
                    if abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y-25-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "up"
                        self.min_dist = abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y-25-self.target_y_pos)**2
                if self.check_move_down() == "down":
                    if abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y+25-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "down"
                        self.min_dist = abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y+25-self.target_y_pos)**2
                if self.check_move_right() == "right":
                    if abs(self.ghost_pos_x+25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "right"
                        self.min_dist = abs(self.ghost_pos_x+25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2


        if self.frightend_mode == False and self.home_mode == False: 
            self.skin = self.real_skin
            self.target_x_pos = x_pos
            self.target_y_pos = y_pos
            self.min_dist = 900000000
            if self.last_move == "up":
                if self.check_move_up() == "up":
                    if abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y-25-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "up"
                        self.min_dist = abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y-25-self.target_y_pos)**2
                if self.check_move_left() == "left":
                    if abs(self.ghost_pos_x-25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "left"
                        self.min_dist = abs(self.ghost_pos_x-25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2
                if self.check_move_right() == "right":
                    if abs(self.ghost_pos_x+25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "right"
                        self.min_dist = abs(self.ghost_pos_x+25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2
            if self.last_move == "down":
                if self.check_move_left() == "left":
                    if abs(self.ghost_pos_x-25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "left"
                        self.min_dist = abs(self.ghost_pos_x-25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2
                if self.check_move_down() == "down":
                    if abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y+25-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "down"
                        self.min_dist = abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y+25-self.target_y_pos)**2
                if self.check_move_right() == "right":
                    if abs(self.ghost_pos_x+25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "right"
                        self.min_dist = abs(self.ghost_pos_x+25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2
            if self.last_move == "left":
                if self.check_move_up() == "up":
                    if abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y-25-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "up"
                        self.min_dist = abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y-25-self.target_y_pos)**2
                if self.check_move_left() == "left":
                    if abs(self.ghost_pos_x-25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "left"
                        self.min_dist = abs(self.ghost_pos_x-25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2
                if self.check_move_down() == "down":
                    if abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y+25-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "down"
                        self.min_dist = abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y+25-self.target_y_pos)**2
            if self.last_move == "right":
                if self.check_move_up() == "up":
                    if abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y-25-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "up"
                        self.min_dist = abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y-25-self.target_y_pos)**2
                if self.check_move_down() == "down":
                    if abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y+25-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "down"
                        self.min_dist = abs(self.ghost_pos_x-self.target_x_pos)**2 + abs(self.ghost_pos_y+25-self.target_y_pos)**2
                if self.check_move_right() == "right":
                    if abs(self.ghost_pos_x+25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2 < self.min_dist:
                        self.ghost_direction = "right"
                        self.min_dist = abs(self.ghost_pos_x+25-self.target_x_pos)**2 + abs(self.ghost_pos_y-self.target_y_pos)**2

        self.ghost_movement()
    def ghost_movement(self):
        if (self.ghost_pos_x, self.ghost_pos_y) == (300,300):
            self.ghost_direction = "up"
            self.ghost_pos_y -= self.speed
        if self.ghost_direction == "up":
            self.ghost_pos_y -= self.speed
            self.last_move = "up"
        elif self.ghost_direction == "down":
            self.ghost_pos_y += self.speed
            self.last_move = "down"
        elif self.ghost_direction == "left":
            self.ghost_pos_x -= self.speed
            self.last_move = "left"
        elif self.ghost_direction == "right":
            self.ghost_pos_x += self.speed
            self.last_move = "right"
        if (self.ghost_pos_x, self.ghost_pos_y) == (0, 300) and self.ghost_direction == "left":
            self.ghost_pos_x, self.ghost_pos_y = 600, 300
            self.last_move = "left"
        if (self.ghost_pos_x, self.ghost_pos_y) == (600, 300) and self.ghost_direction == "right":
            self.ghost_pos_x, self.ghost_pos_y = 0, 300
            self.last_move = "right"
        if self.ghost_pos_y == 300 and self.ghost_pos_x > 600:
            self.ghost_pos_x = 590
        
      
    def draw_ghost(self, screen):
        
        screen.blit(self.skin, (self.ghost_pos_x, self.ghost_pos_y)) 
    def collision(self, x_pos, y_pos):
        if abs(self.ghost_pos_x - x_pos) < 15:
            if abs(self.ghost_pos_y-y_pos) < 15:
                return "paused"
class Red_Ghost(Ghost):
    def __init__(self, barrier_array, skin, frightend_skin, home_skin, screen): 
        self.screen = screen
        self.barrier_array = barrier_array
        self.skin = skin
        self.frightend_skin = frightend_skin
        self.home_skin = home_skin
        super().__init__(575, 25, 300, 250, self.barrier_array, "right", self.skin, self.frightend_skin, self.home_skin)
    def calc_target(self, x_pos, y_pos): 
        if self.mode == "scatter":
            self.x_pos = 575 
            self.y_pos = 25
        if self.mode == "chase":
            self.x_pos = x_pos
            self.y_pos = y_pos
   
        self.calc_next_move(self.x_pos, self.y_pos)
class Pink_Ghost(Ghost):
    def __init__(self, barrier_array, skin, frightend_skin, home_skin, screen):
        self.screen = screen
        self.barrier_array = barrier_array
        self.skin = skin
        self.frightend_skin = frightend_skin
        self.home_skin = home_skin
        super().__init__(25, 25, 250, 300, self.barrier_array, "right", self.skin, self.frightend_skin, self.home_skin)
    def calc_target(self, x_pos, y_pos, player_direction):
        if self.mode == "scatter":
            self.x_pos = 25
            self.y_pos = 25
        if self.mode == "chase":
            self.x_pos = x_pos
            self.y_pos = y_pos
            if player_direction == "up":
                self.y_pos -= 50
            if player_direction == "down":
                self.y_pos += 50
            if player_direction == "left":
                self.x_pos -= 50
            if player_direction == "right":
                self.x_pos += 50
      
        self.calc_next_move(self.x_pos, self.y_pos)

class Blue_Ghost(Ghost):
    def __init__(self, barrier_array, skin, frightend_skin, home_skin, screen):
        self.screen = screen
        self.barrier_array = barrier_array
        self.skin = skin
        self.frightend_skin = frightend_skin
        self.home_skin = home_skin
        super().__init__(575, 550, 300, 300, self.barrier_array, "up", self.skin, self.frightend_skin, self.home_skin)
    def calc_target(self,x_pos_red, y_pos_red, x_pos_pink_target, y_pos_pink_target):
        if self.mode == "scatter":
            self.x_pos = 575
            self.y_pos = 550
        if self.mode == "chase":
            if (x_pos_red-x_pos_pink_target) <= 0:
                self.x_pos = x_pos_pink_target + abs(x_pos_red-x_pos_pink_target)
            if (x_pos_red-x_pos_pink_target) > 0:
                self.x_pos = x_pos_pink_target - abs(x_pos_red-x_pos_pink_target)
            if (y_pos_red-y_pos_pink_target) <= 0:
                self.y_pos = y_pos_pink_target + abs(y_pos_red - y_pos_pink_target)
            if (y_pos_red-y_pos_pink_target) > 0:
                self.y_pos = y_pos_pink_target - abs(y_pos_red-y_pos_pink_target)
    
        self.calc_next_move(self.x_pos, self.y_pos)

class Orange_Ghost(Ghost):
    def __init__(self, barrier_array, skin, frightend_skin, home_skin, screen):
        self.screen = screen
        self.barrier_array = barrier_array
        self.skin = skin
        self.frightend_skin = frightend_skin
        self.home_skin = home_skin
        super().__init__(25, 550, 350, 300, self.barrier_array, "left", self.skin, self.frightend_skin, self.home_skin)
    def calc_target(self, x_pos_pacman, y_pos_pacman): 
        if self.mode == "scatter":
            self.x_pos = 25
            self.y_pos = 550
       
        if self.mode == "chase":
            if abs(self.ghost_pos_x/25-x_pos_pacman/25)**2 + abs(self.ghost_pos_y/25-y_pos_pacman/25)**2 > 64:
                self.x_pos = x_pos_pacman
                self.y_pos = y_pos_pacman
            else:
                self.x_pos = 25
                self.y_pos = 550

        self.calc_next_move(self.x_pos, self.y_pos) 

game = Game()