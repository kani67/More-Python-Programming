import sys, random, math, pygame
from pygame.locals import *
from datetime import datetime, date, time
from tkinter import *



tk = Tk()

canvas = Canvas(tk, bg = "blue" ,width=600, height=500)

canvas.pack(expand=YES, fill=BOTH)

#

class Clock():
    def __init__(self):
        self.pos_x = 300
        self.pos_y = 250
        self.radius = 250
        self.x0 = 0
        self.x1 = 0
        self.y0 = 0
        self.y1 = 0
        self.angle = 360
        self.counter = 0
        self.target = [0,0]
        
    
    def wrap_angle(self, angle):
        
        return self.angle % 360
    
    
        
    def print_text(self,x, y, display_text):
        canvas.create_text(x,y, text = display_text, fill = "yellow", font="Times")    
        
    
    def draw_circle(self,pos_x, pos_y, radius):
        
        self.x0 = pos_x - radius
        self.y0 = pos_y - radius
        self.x1 = pos_x + radius
        self.y1 = pos_y + radius
        canvas.create_oval(self.x0, self.y0, self.x1, self.y1, width=3, fill='blue')



    def draw_numbers(self):    

        #draw the clock numbers 1-12
        for n in range(1,13):
            angle = math.radians( n * (360/12) - 90 )
            x = math.cos( angle ) * (self.radius-20)-5
            y = math.sin( angle ) * (self.radius-20)-5
            self.print_text(self.pos_x+x, self.pos_y+y, str(n))


    def get_time(self): 
        self.today = datetime.today()
        self.hours = self.today.hour % 12
        self.minutes = self.today.minute
        self.seconds = self.today.second
        
        
        return self.hours, self.minutes, self.seconds
       
    def draw_hour_handle(self, hours, radius, pos_x, pos_y):
                
        self.hour_angle = self.wrap_angle( hours * (360/12) - 90 ) 
         
        self.hour_angle = math.radians( self.hour_angle )
        self.hour_x = math.cos( self.hour_angle ) * (radius-80)
        self.hour_y = math.sin( self.hour_angle ) * (radius-80)
        
        self.target = (pos_x+self.hour_x,pos_y+self.hour_y)
        
        canvas.create_line(self.target[0] , self.target[1], self.pos_x, self.pos_y, width=6, fill='yellow')
            
        

        #tk.after(1000, self.update_clock)

def quit_program(event):   
    sys.exit() 
    tk.destroy()
    
    
    

def close_window():
    sys,exit()
    tk.destroy()
    
    

    
def main(event= None):
  
    c = Clock() 
    
    while True:
        
        tk.protocol("WM_DELETE_WINDOW", close_window)
        tk.bind("<Escape>", quit_program)
        tk.bind("<q>", quit_program)
              
        clock_time = c.get_time()
        c.counter += 1
        print(c.counter)
        clock_face = c.draw_circle(c.pos_x, c.pos_y, c.radius)
        clock_numbers = c.draw_numbers()
        

        c.draw_hour_handle(c.hours, c.radius, c.pos_x, c.pos_y)
        
        tk.update()
    
       

    
       
    

tk.after(500, main())    
mainloop()






    





