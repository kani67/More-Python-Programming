import sys, random, math
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
        
        self.seconds_hand_line = ""
        self.minutes_hand_line = ""
        self.hours_hand_line = ""
        self.color = "black"
    
    
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
    
    
    def calculate_hand(self, time_type, hand_radius):
        self.hand_angle = self.wrap_angle( time_type * (360/60) - 90 ) 
        self.hand_angle = math.radians( self.hand_angle )
    
        self.hand_x = math.cos( self.hand_angle ) * (self.radius - hand_radius)
        self.hand_y = math.sin( self.hand_angle ) * (self.radius - hand_radius)
        
        
    
    def draw_seconds_hand(self):      
        
        color = "yellow"
        
        self.canvas.delete(self.seconds_hand_line)
        
        self.calculate_hand(self.seconds, hand_radius = 40) 
        self.target = (self.pos_x+self.hand_x,self.pos_y+self.hand_y)
        self.seconds_hand_line = self.canvas.create_line(self.pos_x, self.pos_y, self.target[0] , self.target[1], width=6, fill=color, arrow=LAST) 
         
        
         
        tk.after(10, self.draw_seconds_hand) 
         
         
         
    def draw_minutes_hand(self):
        color = "orange"
        
        self.canvas.delete(self.minutes_hand_line)
        self.calculate_hand(self.minutes, hand_radius = 60)
        self.target = (self.pos_x+self.hand_x,self.pos_y+self.hand_y)
        self.minutes_hand_line = self.canvas.create_line(self.pos_x, self.pos_y, self.target[0] , self.target[1], width=12, fill=color, arrow=LAST)     
               
        
        tk.after(10, self.draw_minutes_hand)        
            
        
    def draw_hours_hand(self):
        color = "black"
        
        self.canvas.delete(self.hours_hand_line)
        self.calculate_hand(self.hours, hand_radius = 80)
        self.target = (self.pos_x+self.hand_x,self.pos_y+self.hand_y)
        self.hours_hand_line = self.canvas.create_line(self.pos_x, self.pos_y, self.target[0] , self.target[1], width=25, fill=color, arrow=LAST)     
        
        tk.after(10, self.draw_hours_hand)        

def main():     
    
    c = Clock()
    
    c.draw_circle()
    c.draw_numbers()
    c.cover_middle()
    c.get_time()
    
    c.draw_seconds_hand()
    
    
    c.draw_minutes_hand()
    
    c.draw_hours_hand()
    
    tk.after(10, c.draw_seconds_hand)
    tk.after(10, c.draw_minutes_hand)
    tk.after(10, c.draw_hours_hand)
    
    
    
    tk.after(1000, c.get_time)
    mainloop()
    

main()

    
    