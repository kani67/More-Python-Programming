
from tkinter import *


tk = Tk()

canvas = Canvas(tk, bg = "blue" ,width=600, height=500)

canvas.pack(expand=YES, fill=BOTH)



class Rectangle():
    
    def __init__(self):    
        self.pos_x = 0
        self.pos_y = self.pos_x
        self.x1 = self.pos_x + 50
        self.y1 = self.x1
        self.vel_x = 3
        self.vel_y = 4
        self.new_pos_x = 0
        self.new_pos_y = 0
        self.rect_color = "white"
        
        

    def move_rectangle(self):
        
        
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y 
        
         
        
        if self.pos_x > 600 or self.pos_x < 0:
            self.vel_x = -self.vel_x
            self.rect_color = "black"
            
        if self.pos_y > 500 or self.pos_y < 0:
            self.vel_y = -self.vel_y        
            self.rect_color = "red"
        
        canvas.create_rectangle(self.pos_x, self.pos_y, self.x1, self.y1, fill = self.rect_color)
        canvas.after(10, self.move_rectangle)
         
        self.x1 = self.pos_x + 50
        self.y1 = self.x1
        
def main():        
    r = Rectangle()
    tk.after(100,r.move_rectangle)
    mainloop()
    
main()