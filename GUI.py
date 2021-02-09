#!/usr/bin/env python
# coding: utf-8

# In[6]:


from tkinter import *
from PIL import ImageTk
from PIL import Image as PilImage

def main_menu():
    print("To main menu")
    main.create_window()

def ASL_Fingerspell():
    print("ASL fingerspelling and shit")
    windowASL.create_window()
    
def do_something():
    print("Did something")
    
def start():
    print('Just started')
    
def stop():
    print('stopped')

    
class Window:
    root = Tk()
    def __init__(self, window_title, window_size, bg_image,button_dict,exit_b,button_Ypos):
        self.title = window_title
        self.size = window_size
        self.background_image = bg_image
        self.buttons_and_func = button_dict
        self.exit = exit_b
        self.button_y = button_Ypos
        
        
    def create_buttons(self):
        button_names = list(self.buttons_and_func.keys())
        y_pos = self.button_y
        
        for i in range(len(button_names)):
            command_given = self.buttons_and_func[button_names[i]]
            y_pos = y_pos + 0.25
            button = Button(master = self.root,
                            activebackground = 'Blue',
                            text = button_names[i], 
                            font = 'Courier', 
                            height= 2, 
                            width=25, 
                            relief=RAISED,
                            bd='5',
                            command = command_given)
            button.place(relx = 0.5, rely = y_pos, anchor = CENTER) 
            
            
        #Exit Button
        if self.exit == True:
            button = Button(master = self.root,
                            activebackground = 'Red',
                            text = "Exit", 
                            font = 'Courier', 
                            height= 2, 
                            width=25, 
                            relief=RAISED,
                            bd='5',
                            command = self.root.destroy)
            button.place(relx = 0.5, rely = 0.25 * (len(button_names)+1), anchor = CENTER)   
           
            
        
    def create_window(self):
        self.root.geometry(self.size)  # For a fixed size of window
        self.root.title(self.title )

        #To set the background Image
        image = PilImage.open(self.background_image)
        background = ImageTk.PhotoImage(image)
        background_label = Label(image = background)
        background_label.place(x=0, y=0, relwidth=1, relheight=1) 
        
    
        self.create_buttons()
     
        self.root.mainloop()
        

# Window 1
title0 = 'American Sign Language Recognition'
size0 = "1280x868"
bg_image0 = "C:/Python/Python37/Scripts/Project/GUI images/back15.png"
button_dict0 = {"To Main Menu": main_menu}

start_page = Window(window_title = title0,
              window_size = size0,
              bg_image = bg_image0,
              button_dict = button_dict0,
              exit_b = False,
              button_Ypos = 0.60)

        
# Window 2
title1 = 'Main Menu'
size1 = "1280x868"
bg_image1 = "C:/Python/Python37/Scripts/Project/GUI images/back12.png"
button_dict1 = {"ASL Finger Spelling":ASL_Fingerspell, "Do Something": do_something}

main = Window(window_title = title1,
              window_size = size1,
              bg_image = bg_image1,
              button_dict = button_dict1,
              exit_b = True,
              button_Ypos = 0)




def go_back():
    main.create_window()
    try:
        windowASL.destroy()
    except:
        pass

# Window 3
title2 = 'ASL Finger Spelling'
size2 = "1280x868"
bg_image2 = "C:/Python/Python37/Scripts/Project/GUI images/back12.png"
button_dict2 = {"Start":start, "Stop": stop, "Back":go_back}

windowASL = Window(window_title = title2,
                   window_size = size2,
                   bg_image = bg_image2,
                   button_dict = button_dict2,
                   exit_b = False,
                   button_Ypos = 0)


start_page.create_window()

