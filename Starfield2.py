import random, pygame

SCROLL_TOP_BOTTOM = 1
SCROLL_LEFT_RIGHT = 2
SCROLL_BOTTOM_TOP = 3
SCROLL_RIGHT_LEFT = 4
    
class Starfield(object):
    #parameter star_field_list is a list of lists in the following form
    #for each star field: [numstars, radius, velocity]
    #example:
    #   star_field_struct =  [
    #   [400, 1, 1],
    #   [100, 2, 3],
    #   [20, 4, 6]
    #   ]

    
    def __init__(self, width, height, x_range, y_range, star_field_list, scroll_dir=SCROLL_TOP_BOTTOM, colored=True):
        self.width = width
        self.height = height
        self.x_range = x_range
        self.y_range = y_range
        self.scroll_dir = scroll_dir
        
        self.star_fields = list()
        self.star_field_colors = list()
        self.star_field_radius = list()
        self.star_field_vel = list()
        
        self.__populate_fields( star_field_list, colored)
        
    def __populate_fields(self, star_field_list, colored):
        for field_num in range ( 0, len(star_field_list) ):
            new_star_field = list()
            new_color_field = list()
            self.star_field_radius.append(star_field_list[field_num][1])
            self.star_field_vel.append(star_field_list[field_num][2])
            
            for stars in range (0, star_field_list[field_num][0] ):
                point = [random.randint(self.x_range[0],self.x_range[1]), random.randint(self.y_range[0], self.y_range[1]) ]
                if colored==True:
                    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255) )
                else:
                    color =(255,255,255)
                new_star_field.append(point)
                new_color_field.append(color)
            self.star_fields.append(new_star_field)
            self.star_field_colors.append(new_color_field)
            
    def update(self):
        for field_num, field in enumerate(self.star_fields):
            for num in range(0, len(field) ):
                if self.scroll_dir == SCROLL_TOP_BOTTOM :
                    y=field[num][1]
                    y += self.star_field_vel[field_num]
                    if y>=self.height: y = (self.height-y)
                    field[num][1] = y
                elif self.scroll_dir == SCROLL_BOTTOM_TOP:
                    y=field[num][1]
                    y -= self.star_field_vel[field_num]
                    if y<=0: y = (self.height-(-y))
                    field[num][1] = y
                elif self.scroll_dir== SCROLL_LEFT_RIGHT:
                    x=field[num][0]
                    x -= self.star_field_vel[field_num]
                    if x<0: x = (self.width-(-x))
                    field[num][0] = x
                elif self.scroll_dir== SCROLL_RIGHT_LEFT:
                    x=field[num][0]
                    x += self.star_field_vel[field_num]
                    if x>=self.width: x = (self.width-x)
                    field[num][0] = x
                    
    def draw(self, screen):
        for field_num, field in enumerate(self.star_fields):     
            for pos,color in zip(self.star_fields[field_num], self.star_field_colors[field_num]):
                if self.star_field_radius[field_num] == 1:
                    screen.set_at( (pos[0],pos[1]), color )
                else:
                    pygame.draw.circle(screen, color, (pos[0],pos[1]), self.star_field_radius[field_num], 0)

