#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
from tkinter import messagebox
import pyqrcode
import png
from pyqrcode import QRCode

ws = Tk()
ws.geometry("500x600")
ws.resizable(False,False)
ws.title("QR CODE GENERATOR")
ws.config(bg = '#eb7965')

def generate():
    if len(user_input.get())!= 0:
        global qr, img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data = qr.xbm(scale = 10))
    else:
        messagebox.showwarning('All Fields are Required!')
    try:
        display_code()
    except:
        pass

def display_code():
    img_l.config(image = img)
    output.config(text = "SUCCESSFULLY GENERATED the QR code")
    
def save():
    qr.png(f'{user_input1.get()}.png', scale=25) 
    
l = Label(
    ws,
    text = "Enter Text/URL: ",
    bg = '#eb7965'
)
l.pack()

user_input = StringVar()
entry = Entry(
    ws,
    textvariable = user_input
)
entry.pack(padx=20)

button = Button(
    ws,
    text = "CLICK TO GENERATE",
    width = 25,
    command = generate
)
button.pack(pady = 30)

l1 = Label(
    ws,
    text = "Enter file name: ",
    bg = '#eb7965'
)
l1.pack()

user_input1 = StringVar()
entry1 = Entry(
    ws,
    textvariable = user_input1
)
entry1.pack(padx=20)

button1 = Button(
    ws,
    text = "CLICK TO SAVE",
    width = 25,
    command = save
)
button1.pack(pady = 30)

img_l = Label(
    ws,
    bg = '#eb7965')

img_l.pack()

output = Label(
    ws,
    text = "",
    bg = '#eb7965'
)
output.pack()

ws.mainloop()


# In[ ]:




