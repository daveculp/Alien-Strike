'''Game sprite class for using animated sprites in a pygame module.
pass in either image data or a filename but not both.

Keyword arguments:
num_frames -- number of frames the sprite has.  Only needed 
when passing in a filename

image_filename -- A PNG only file with the PNG extension stripped off.

image_data -- A list of pygame surfaces that contain the animation 
frames of the sprite.
'''

    
import pygame 

class GameSprite(pygame.sprite.Sprite):
 
    def __init__(self, num_frames=None, image_filename=None, image_data=None):
        pygame.sprite.Sprite.__init__(self)
        self.active = False
        self.delta_x = 0
        self.delta_y = 0
        self.frames = []
        if num_frames == None:
            self.num_frames = 1
        else:
            self.num_frames = num_frames
        self.current_frame = 0
        #if image_filename == None and image_data == None:
        #    print("You must pass either a filename or image data to the Sprite constructor")
        #    return
        if image_filename != None:
            self.load_frames(image_filename)
        elif image_data != None:
            self.frames = image_data
            self.num_frames = len(image_data)

        try:
            self.rectangle = self.frames[0].get_rect()
        except:
            print("You must pass either a filename or image data to the Sprite constructor")     
        self.update_count = 0
        self.ticks = 0
        self.width = self.rectangle.width
        self.height = self.rectangle.height
        self.x = 0
        self.y = 0
    
    def load_frames(self, image_filename):
        if self.num_frames == 1:
            temp_image = pygame.image.load(image_filename)
            self.frames.append(temp_image)
        else:
            for x in range (0,self.num_frames):
                sprite_filename = image_filename+str(x)+".png"
                temp_image = pygame.image.load(sprite_filename)
                self.frames.append(temp_image)
                
    def update(self):
        self.ticks += 1
        if self.num_frames > 1:
            if self.ticks % self.update_count == 0:
                self.current_frame += 1
                if self.current_frame == len(self.frames):
                    self.current_frame = 0
            self.rectangle = self.rectangle.move( (self.delta_x, self.delta_y) ) 
        
    def set_pos(self,x,y):
        self.rectangle.x, self.rectangle.y = (x,y)
        
    def get_pos(self):
        return self.rectangle.x, self.rectangle.y 
    
    def draw(self,screen):
        if self.active == True:
            self.rectangle = screen.blit(self.frames[self.current_frame], self.rectangle)
    
