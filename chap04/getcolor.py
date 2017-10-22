import random

def get_color(color_name, is_random):
    color = 0
    color_list = [[255, 255, 255] , [255, 0, 0] , [255, 255, 0] , [0, 255, 0], [0, 0, 0]]
    if not is_random:
        if color_name == "white":
            color = 0
        if color_name == "red":    
            color = 1
        if color_name == "yellow": 
            color = 2
        if color_name == "lime":
            color = 3
        if color_name == "black":
            color = 4    
    else:    
            
        color = random.randint(0 , 4)
            
    return color_list[color]    