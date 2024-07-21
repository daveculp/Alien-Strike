#!/usr/bin/env python

import random, pygame, sys, glob, time, os
from GameSprite import GameSprite
from Starfield import *

#======================================================================
#                       CLASS SECTION                                 =
#======================================================================


# The class for our player sprite 
class Player(GameSprite):
    def __init__(self, player_image_filename):
        GameSprite.__init__(self,1, player_image_filename )
        self.rectangle.x = SCREEN_WIDTH//2
        self.rectangle.y = SCREEN_HEIGHT-55
        self.smart_bombs = 2
        self.delta_x = 20
        self.shot_delay = 20
        self.four_way_shot = False
        self.last_shot_fired=0
        
        self.shield = GameSprite(num_frames=1, image_filename="./media/sprites/player_shield.png")
        self.shield.delta_x = 0
        self.shield.delta_y = 0
        self.shield.active = False
        
        self.missile_list=list()
        self.player_missile_images = load_images("./media/sprites/player_missile",2)

    def spawn_missile(self):
        new_missile_left = Missile(missile_image_data=self.player_missile_images)
        new_missile_left.update_count = 5
        new_missile_left.rectangle.x = player.rectangle.x + 15
        new_missile_left.rectangle.y = SCREEN_HEIGHT - 55
        new_missile_left.delta_y = -7 
        new_missile_left.active = True
        self.missile_list.append(new_missile_left)
    
        new_missile_right = Missile(missile_image_data=self.player_missile_images)
        new_missile_right.update_count = 5
        new_missile_right.rectangle.x = player.rectangle.x + 30
        new_missile_right.rectangle.y = SCREEN_HEIGHT - 55
        new_missile_right.delta_y = -7
        new_missile_right.active = True
        self.missile_list.append(new_missile_right)
        
        if player.four_way_shot == True:
            new_missile_left = Missile(missile_image_data=self.player_missile_images)
            new_missile_left.update_count = 5
            new_missile_left.rectangle.x = player.rectangle.x 
            new_missile_left.rectangle.y = SCREEN_HEIGHT - 45
            new_missile_left.delta_y = -7
            new_missile_left.active = True
            self.missile_list.append(new_missile_left)
    
            new_missile_right = Missile(missile_image_data=self.player_missile_images)
            new_missile_right.update_count = 5
            new_missile_right.rectangle.x = player.rectangle.x + 45
            new_missile_right.rectangle.y = SCREEN_HEIGHT - 45
            new_missile_right.delta_y = -7
            new_missile_right.active = True
            self.missile_list.append(new_missile_right)
            
        self.last_shot_fired = self.ticks
        
class Missile(GameSprite):
    def __init__(self, missile_image_data=None):
        GameSprite.__init__(self,image_data = missile_image_data)
        self.delta_x = 0
        self.delta_y = -8
        self.active = False

#======================================================================
#                       FUNCTIONS SECTION                             =
#======================================================================

def stereo_pan(x_pos):
    """Adjust the left and right volume based upon scren ccordinates """
    right_volume = float(x_pos) / SCREEN_WIDTH
    left_volume = 1.0 - right_volume
    if game_sound_state == True:
        return (left_volume, right_volume)
    else:
        return(0, 0)

def play_sound(sound, x_pos):
    """Play passed in sound object on new channel"""
    channel = sound.play()
    if channel is not None:
        left, right = stereo_pan(x_pos)
        channel.set_volume(left, right)
        
              
def load_images(image_filename, num_frames):
    frames=list()
    if num_frames == 1:
        temp_image = pygame.image.load(image_filename)
        frames.append(temp_image)
    else:
        for x in range (0,num_frames):
            sprite_filename = image_filename+str(x)+".png"
            temp_image = pygame.image.load(sprite_filename)
            frames.append(temp_image)
    return frames
    
def draw_screen():
    screen.fill( (0,0,0) )
    star_field.draw(screen)
    for missile in player.missile_list:
        missile.draw(screen)
    player.draw(screen)
    player.shield.draw(screen)
    fps=int(clock.get_fps())
    fps_text = font.render("fps: "+str( fps), True, (128, 255, 0))
    screen.blit(fps_text, ((SCREEN_WIDTH-fps_text.get_width())//2, 0))
   
    
def update():
        star_field.update()
        player.update()
        if player.shield.active == True:
            player.shield.rectangle.x=player.rectangle.x-6
            player.shield.rectangle.y=player.rectangle.y-8
            player.shield.update()
        
        for missile in player.missile_list:
            missile.update()
            
def check_bounds():
    for missile in player.missile_list:
        if missile.rectangle.y < 0:
            player.missile_list.remove(missile)


def play_next_song():
    if pygame.mixer.music.get_busy() == False:
        song= song_list[random.randint(0, len(song_list))-1]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(0)
        print ("Playing: +",song)
#======================================================================
#                       END FUNCTIONS SECTION                         =
#====================================================================== 

    

     
#======================================================================
#                       GLOBALS SECTION                               =
#======================================================================

#set globals for our screen width and height
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

END_MUSIC_EVENT = pygame.USEREVENT + 0   
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)
pygame.mixer.music.set_endevent(END_MUSIC_EVENT)


#init the sound mixer, pygame and our screen screen
#pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.set_num_channels(64)

infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h

print(infoObject.current_w, infoObject.current_h)

#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),  pygame.FULLSCREEN)
screen = pygame.display.set_mode((0, 0),  pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)

#clock to keep track of our framerate
clock = pygame.time.Clock()

#Construct StarField List - passed in as [numstars, radius, velocity]
#Make a 3 layer parallax scrolled star field
star_field_struct =  [
    [200, 1, 1],
    [50, 2, 3],
    [10, 4, 6]
    ]
star_field = Starfield(SCREEN_WIDTH, SCREEN_HEIGHT, (4, SCREEN_WIDTH-4), (5, SCREEN_HEIGHT-5), star_field_struct, SCROLL_TOP_BOTTOM)



#load and activate our player sprite
player = Player( "./media/sprites/player.png")
player.delta_x = 0
player.delta_y = 0
player.active = True

#hide the mouse, turn on key repeat and grab the mouse pointer
pygame.mouse.set_visible(False)
pygame.key.set_repeat(1, 500)
pygame.event.set_grab(True)

#load in our music list
song_list = glob.glob("./media/music/tracks/*.mp3")

fps_target = 60 #our frames per second target
font = pygame.font.Font("./media/fonts/zorque.ttf", 24, bold=True)
#======================================================================
#                       MAIN GAME LOOP                                =
#======================================================================
#play_next_song()
song= song_list[random.randint(0, len(song_list))-1]
pygame.mixer.music.load(song)
clock.tick(10)
pygame.mixer.music.play(0)
clock.tick(10)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            player.rectangle.x = event.pos[0]
            if player.rectangle.x > SCREEN_WIDTH - player.width:
                player.rectangle.x = SCREEN_WIDTH - player.width
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if (player.ticks - player.last_shot_fired) > player.shot_delay:
                player.spawn_missile()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            print ("SMART BOMB!!!")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()   
            if event.key == pygame.K_f:
                player.four_way_shot ^= True
            if event.key == pygame.K_s:
                #print ("S pressed!!")
                player.shield.active ^= True
            if event.key == pygame.K_r:
                if player.shot_delay == 1:
                   player.shot_delay = 20
                else:
                    player.shot_delay = 1         
        #if event.type == END_MUSIC_EVENT and event.code == 0:
            #play_next_song()
      
    #main drawing and updating loop             
    update()
    check_bounds()
    draw_screen()
    pygame.display.update()

    clock.tick(fps_target) #set our target frame rate

    #print "fps:", clock.get_fps()
