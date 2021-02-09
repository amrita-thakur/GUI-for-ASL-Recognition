# -------------------------------- Import Necessary Modules -----------------------------------------------

import tkinter as tk
from tkinter import ttk # To style the widgets
from PIL import ImageTk
from PIL import Image, ImageDraw, ImageFont
import cv2
import os
import numpy as np
import imageio
import time
import keras
from keras.utils.np_utils import to_categorical
from keras.models import model_from_json
import statistics
import skimage
from skimage.transform import resize
import random
import re

# fonts ---> "Courier New", "Segoe UI","Open Sans","Roboto"

LABEL_FONT = ("Courier New",15)
BUTTON_FONT = ("Roboto",12)
alphabet_list = list()
deep_sky_blue = "#00BFFF"
SPECIAL_FONT = ("Courier New",14)

# --------------------------------  Helper functions ---------------------------------

def popupmsg():
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text="This feature isn't available yet!!", font=("Roboto",12))
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    


# ---------------------------- App Class -------------------------------------------------------

# main class ---> app 
# Child class of tk.Tk class as it is an app.

class ASL_RecogSys(tk.Tk):
    # self ---> points towards the object so that an object can use variables and methods of a class 
    # Eg: object_name.variable_name or object_name.method(...)
    # *args --> as many arguments/parameters as you like
    # **kwargs --> keyword arguments (dictionaries)
    
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs) #Initializing tkinter

        container = tk.Frame(self) #Frame ---> Window
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0,weight = 1) 
        container.grid_columnconfigure(0,weight = 1)
        
        label_style = ttk.Style()
        label_style.configure("my.TLabel",background = deep_sky_blue, foreground = "Black",relief = "flat")

        button_style = ttk.Style()
        button_style.theme_use("vista")
        button_style.configure('my.TButton',foreground = "dark blue",padding= 10, relief="flat", font= BUTTON_FONT)
        
        
       
        
        # Store the pages in the application inside a dictionary called frames
        self.frames = dict() 
        
        #Format
        frame_names = (StartPage,
                       MainMenu,
                       Credits) #Will be the name of the windows that will be separate classes
        
        for Fclass in frame_names:
            frame = Fclass(container,self)
            self.frames[Fclass] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew") #"nsew" ---> Strech everything to window size

        self.show_frame(StartPage)
 
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise() # Show page with the help of page_name class as a key
        
        
# ---------------------------- Window 1 -------------------------------------------------------
# First window
# Child class of tk.Frame as it is a window
class StartPage(tk.Frame): 
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        image1 = tk.PhotoImage(file="images/BG_StartPage.png")
        panel1 = tk.Label(self, image=image1)
        panel1.pack(side='top', fill='both', expand=True)
        panel1.image = image1
        

       
        x_pos = 0.25
        y_pos = 0.75
        x_inc = 0.5
        y_inc = 0.15
        button_width = 250
        button_height = 50
        
        button1 = ttk.Button(self,text = "To Main Menu",style = 'my.TButton',
                            command = lambda: controller.show_frame(MainMenu) )
        
        button1.place(relx = x_pos,  #fraction of width for button x_position
                      rely = y_pos, #fraction of height for button y_position
                      width = button_width,
                      height = button_height,
                      anchor = tk.CENTER)#Button  position
        
        button2 = ttk.Button(self,text = "Help",style = 'my.TButton', command = popupmsg)
        button2.place(relx = x_pos + x_inc,  #fraction of width for button x_position
                      rely = y_pos, #fraction of height for button y_position
                      width =  button_width,
                      height = button_height,
                      anchor = tk.CENTER)#Button  position
        
        button3 = ttk.Button(self,text = "Credits",style = 'my.TButton',command = lambda: controller.show_frame(Credits))
        button3.place(relx = 0.5,  #fraction of width for button x_position
                      rely = y_pos + y_inc, #fraction of height for button y_position
                      width =  button_width,
                      height = button_height,
                      anchor = tk.CENTER)#Button  position
        
    
        
        
# ---------------------------- Window 1.1 -------------------------------------------------------
class MainMenu(tk.Frame): 
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        image1 = tk.PhotoImage(file="images/BG_MainMenu.png")
        panel1 = tk.Label(self, image=image1)
        panel1.pack(side='top', fill='both', expand=True)
        panel1.image = image1
    
        x_pos = 0.25
        y_pos = 0.70
        x_inc = 0.5
        y_inc = 0.15
        button_width = 300
        button_height = 50
   
      
        button1 = ttk.Button(self,text = "ASL Fingerspelling Mode",style = 'my.TButton',
                    command = popupmsg)
        
        button1.place(relx = x_pos,  #fraction of width for button x_position
                      rely = y_pos, #fraction of height for button y_position
                      width =  button_width,
                      height = button_height,
                      anchor = tk.CENTER)#Button  position
        
        button2 = ttk.Button(self,text = "Text to ASL Mode",style = 'my.TButton',
                    command = popupmsg )
        button2.place(relx = x_pos + x_inc,  #fraction of width for button x_position
                      rely = y_pos, #fraction of height for button y_position     
                      width =  button_width,
                      height = button_height,
                      anchor = tk.CENTER)#Button  position
        
        
        button3 = ttk.Button(self,text = "ASL words",style = 'my.TButton',command = popupmsg)
        
        button3.place(relx = x_pos,  #fraction of width for button x_position
                      rely = y_pos + y_inc, #fraction of height for button y_position
                      width =  button_width,
                      height = button_height,
                      anchor = tk.CENTER)#Button  position
        
    
        
        button6 = ttk.Button(self,text = "Back",style = 'my.TButton',
                            command = lambda: controller.show_frame(StartPage) )
        button6.place(relx = x_pos + x_inc,  #fraction of width for button x_position
                      rely = y_pos + y_inc, #fraction of height for button y_position
                      width =  button_width,
                      height = button_height,
                      anchor = tk.CENTER)#Button  position
        
# ---------------------------- Window 1.2-------------------------------------------------------
class Credits(tk.Frame): 
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        image1 = tk.PhotoImage(file="images/BG_Credits.png")
        panel1 = tk.Label(self, image=image1)
        panel1.pack(side='top', fill="both", expand='yes')
        panel1.image = image1    
        
    

        mytext=tk.Text(self,bg= "Black",foreground = "White",width=40,height=15,font = ("Courier New",18))
        mytext.place(relx = 0.5,
                     rely = 0.53,
                     anchor = tk.CENTER)
        mytext.insert('end', "\n\n    Amrita Thakur        (073BEX405)  \n\n")
        mytext.insert('end', "    Pujan Budhathoki     (073BEX428)  \n\n")      
        mytext.insert('end', "    Sarmila Upreti       (073BEX439)  \n\n")
        mytext.insert('end', "    Shirish Shrestha     (073BEX440)  \n\n\n")
        mytext.insert('end', "           Supervised by:  \n") 
        mytext.insert('end', "        Prof. Dr. Subarna Shakya  ") 
        mytext.insert('end',"\n\n Thanks for using this application!!\n\n")
        mytext.configure(state='disabled')
       
        button1 = ttk.Button(self,text = "Back",style = 'my.TButton',
                            command = lambda: controller.show_frame(StartPage) )
        button1.place(relx = 0.5,  
              rely = 0.92, 
              width =  200,
              height = 50,
              anchor = tk.CENTER)
        



# ---------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__": 
    app = ASL_RecogSys()
    app.wm_title("ASL RecogSys")
    app.wm_geometry("800x600")
    app.resizable(False, False)
    app.iconbitmap("images/asl_icon.ico")

    app.mainloop()