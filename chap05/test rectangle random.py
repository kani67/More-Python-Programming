
from tkinter import *


tk = Tk()
counter = 0


class Rectangle():
    
    def __init__(self):    
        self.x0 = 0
        self.y0 = 0
        self.x1 = 100
        self.y1 = 100
        self.vel_x = 2
        self.vel_y = 1
       
        self.new_x0 = 0
        self.new_y0 = 0
        self.new_x1 = 0
        self.new_y1 = 0
        
        
        self.width = 100
        self.height = 100
        
        self.canvas = Canvas(tk, bg = "blue" ,width=600, height=500)

        self.canvas.pack(expand=YES, fill=BOTH)
        self.rxy_id = self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill = "white")
        
        
    def move_rectangle(self): 
        
        self.new_x0, self.new_y0, self.new_x1, self.new_y1 = self.canvas.coords(self.rxy_id)
        
          
        self.new_x0 += self.vel_x
        self.new_y0 += self.vel_y
        self.new_x1 += self.vel_x
        self.new_y1 += self.vel_y
    
        self.canvas.coords(self.rxy_id, self.new_x0, self.new_y0, self.new_x1, self.new_y1)      
        
        
        
        #if self.new_x1  > 600 or self.new_x0  < 0:     
    
        if self.new_x0 < 0  or self.new_x1  > 600:     
               
            self.vel_x = -self.vel_x
            self.canvas.itemconfig(self.rxy_id, fill = "black")
            
        #if self.new_y1  > 500 or self.new_y0 < 0:
        if self.new_y0 < 0 or self.new_y1  > 500:
            self.vel_y = -self.vel_y        
            self.canvas.itemconfig(self.rxy_id, fill = "red")
        
        
        
        
        
        #self.canvas.move(self.rectangle,self.new_x0, self.new_y0, self.new_x1, self.new_y1)
        
        
        self.canvas.after(5, self.move_rectangle)
         
        
def main():     
    
    r = Rectangle()
    
    tk.after(5,r.move_rectangle)
    
    
    mainloop()
    

main()


    #x1,y1,x2,y2=w.coords(id1)
    #if x1+Dx<=0 or x1+Dx>=190:
     #   Dx=-Dx
    #if y1+Dy<=0 or y1+Dy>=190:
    #    Dy=-Dy
    #w.coords(id1,x1+Dx,y1+Dy,x2+Dx,y2+Dy)