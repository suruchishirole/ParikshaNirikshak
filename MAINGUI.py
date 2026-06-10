from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
from datetime import date
from tkcalendar import Calendar
import cv2
from datetime import datetime
from ultralytics import *


def center_window(w,h):
    # get screen width and height
    ws = root.winfo_screenwidth() 
    
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    
def validateDate(entered_date):
    try:
        # Validate and parse the date
        valid_date = datetime.strptime(entered_date, "%m-%d-%Y")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter the date in mm-dd-yyyy format.")
    print(entered_date)
    return entered_date
    
    
    
    
def read_input():
    print("inside read_input")    
    
    HOD_name = textBox1.get()
    HOD_mob = textBox2.get()
    Block_Number = textBox3.get()
    print("HOD Name : ",HOD_name)
    print("HOD Number : ",HOD_mob)
    print("Block Number ",Block_Number)
    import anti_cheating_detection_engine
    anti_cheating_detection_engine.startDetection(HOD_name, HOD_mob, Block_Number)

    
root=Tk()
root.configure(background='#6495ED')
root.title("Anti Cheating System")
center_window(900, 600)
image = Image.open("MainGUI_img.jpg")

# Resize the image using resize() method
resize_image = image.resize((1200, 900))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()


username = Label(root,text = "Anti Cheating System", font=("Courier", 20,'bold'),fg='#f00').place(x = 210,y = 30)


# code to create label 
label1 = Label(root,text = "HOD Name: ",bg='#6495ED',font=("Ariel", 10)).place(x = 180,y = 205)
label2 = Label(root, text = "HOD Mobile No. : ",bg='#6495ED',font=("Ariel", 10)).place(x = 180,y = 265)  
label3 = Label(root, text = "Block Number : ",bg='#6495ED',font=("Ariel", 10)).place(x = 180,y = 325)     


textBox1 = tk.Entry(root, width = 25)
textBox1.place(x = 500,y = 205,height=30)
textBox2 = tk.Entry(root, width = 25)
textBox2.place(x = 500,y = 265,height=30)

textBox3 = tk.Entry(root, width = 25)
textBox3.place(x = 500,y = 325,height=30)



#command=lambda: retrieve_input() >>> just means do this when i press the button
button=Button(root, height=1, width=13, font=("Ariel", 10,'bold'),text="Start", command=lambda: read_input()).place(x=220,y=400)

# Button for closing
exit_button = Button(root, height=1, width=13, font=("Ariel", 10,'bold'),text="Exit", command=root.destroy).place(x=500,y=400)


mainloop()

