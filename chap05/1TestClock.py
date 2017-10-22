import sys, random, math, pygame
from pygame.locals import *
from datetime import datetime, date, time
from tkinter import *



tk = Tk()



class Clock():
    def __init__(self):
        self.pos_x = 300
        self.pos_y = 250
        self.radius = 250
        self.middle_radius = 25
        self.x0 = 0
        self.x1 = 0
        self.y0 = 0
        self.y1 = 0
        self.angle = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.counter = 0
        self.target = [0,0]
        self.canvas = Canvas(tk, bg = "blue" ,width=600, height=500)

        self.canvas.pack(expand=YES, fill=BOTH)
        
        self.i = ""
        self.w = ""

    def print_text(self,x, y, display_text):
        self.canvas.create_text(x,y, text = display_text, fill = "yellow", font="Times")    
        
        
    def wrap_angle(self, angle):
        return angle % 360    
        
    def draw_circle(self):
        
        self.x0 = self.pos_x - self.radius
        self.y0 = self.pos_y - self.radius
        self.x1 = self.pos_x + self.radius
        self.y1 = self.pos_y + self.radius
        self.canvas.create_oval(self.x0, self.y0, self.x1, self.y1, width=3, fill="blue")
    
    
    def draw_numbers(self):    
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
        
        tk.after(10,self.get_time)
        
    def cover_middle(self):
        
        self.canvas.create_oval(self.pos_x + self.middle_radius, 
                                self.pos_y + self.middle_radius,
                                self.pos_x - self.middle_radius,
                                self.pos_y - self.middle_radius, fill  = "yellow")  
        
    def draw_hour_hand(self):
                
        self.hour_angle = self.wrap_angle( self.hours * (360/12) - 90 ) 
        self.hour_angle = math.radians( self.hour_angle )
        
        self.hour_x = math.cos( self.hour_angle ) * (self.radius-80)
        self.hour_y = math.sin( self.hour_angle ) * (self.radius-80)
        
        self.target = (self.pos_x+self.hour_x,self.pos_y+self.hour_y)
        
        
        
        self.canvas.create_line(self.pos_x, self.pos_y, self.target[0] , self.target[1], width=15, fill="black", arrow=LAST)            
    
        
        tk.after(10, self.draw_hour_hand)
        
        
        
    def draw_minutes_hand(self):     
        
        self.canvas.delete(self.w)
        self.minutes_angle = self.wrap_angle( self.minutes * (360/60) - 90 ) 
        self.minutes_angle = math.radians( self.minutes_angle )
        
        self.minutes_x = math.cos( self.minutes_angle ) * (self.radius-60)
        self.minutes_y = math.sin( self.minutes_angle ) * (self.radius-60)
        
        self.target = (self.pos_x+self.minutes_x,self.pos_y+self.minutes_y)
        
        
        
        self.w = self.canvas.create_line(self.pos_x, self.pos_y, self.target[0] , self.target[1], width=10, fill="orange", arrow=LAST)            
    
        
        tk.after(10, self.draw_minutes_hand)
    
    
    
    def draw_seconds_hand(self):
        
          
        self.canvas.delete(self.i)
        
        self.seconds_angle = self.wrap_angle( self.seconds * (360/60) - 90 ) 
        self.seconds_angle = math.radians( self.seconds_angle )
        
        self.seconds_x = math.cos( self.seconds_angle ) * (self.radius-40)
        self.seconds_y = math.sin( self.seconds_angle ) * (self.radius-40)
       
        
        self.target = (self.pos_x+self.seconds_x,self.pos_y+self.seconds_y)
        
        
        self.i = self.canvas.create_line(self.pos_x, self.pos_y, self.target[0] , self.target[1], width=5, fill='yellow', arrow=LAST)     
               
    
        
        tk.after(10, self.draw_seconds_hand)
        
        

def main():     
    
    c = Clock()
    
    c.draw_circle()
    c.draw_numbers()
    c.cover_middle()
    c.get_time()
    c.draw_hour_hand()
    c.draw_minutes_hand()
    c.draw_seconds_hand()
    tk.after(10, c.draw_hour_hand)
    tk.after(10, c.draw_minutes_hand)
    tk.after(10, c.draw_seconds_hand)
    
    tk.after(1000, c.get_time)
    mainloop()
    

main()

    
    