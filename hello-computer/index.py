import mysql.connector

# import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

import tkinter.messagebox
import tkinter.simpledialog


gui = tkinter.Tk()


# empty string for user's name
user = ''

# prompt user for their name
def hello_call_back():
   global user
   tkinter.messagebox.showinfo( 'Hello World!', 'Thanks for coming!')
   user = tkinter.simpledialog.askstring( 'Query:', "What's your name? Type Below:               " )
   name_call_back()

# disable hello method, prompt for entry, display in new frame
def name_call_back():
    # make available variable
    global user

    # disable initial "hello" button
    Begin['state'] = tkinter.DISABLED
    
    # create label for user entry
    enter_value=Label(greeting_frame, text= f"Hi {user}, I am Python. Please enter a value:")
    enter_value.place(x=20, y=50)

    # create user entry field
    D = tkinter.Entry(greeting_frame, width= 40 )
    D.place(x=20, y=70)

    # create text field
    display_input=Text(response_frame)

    # empty string for user input
    user_input = ''
   
    # gets user entered value and sends it to response frame
    def input_driver():
        user_input = D.get()
        make_new_frame(user_input)

    # builds response frame and inserts user entered value
    def make_new_frame(input):
        response_frame.place(x= 310, y= 20)   
        display_input.insert('1.0', f'{user}, you entered: {input}\n')
        display_input.pack()
    
    # displays entered string in response_frame
    E = tkinter.Button(greeting_frame, text ='Ok', command = input_driver)
    E.place(x=20, y=90)

# layout frames
hello_frame = ttk.Frame(gui, width= 640, height= 260)
hello_frame['relief'] = 'raised'
hello_frame.place(x= 65, y= 20)
hello_frame.pack_propagate(False)

greeting_frame = ttk.Frame(hello_frame, width= 270, height= 200)
greeting_frame['relief'] = 'sunken'
greeting_frame.place(x= 20, y= 20)
greeting_frame.pack_propagate(False)

response_frame = ttk.Frame(hello_frame, width= 300, height= 200)
response_frame['relief'] = 'groove'
response_frame.pack_propagate(False)

# Initial 'Hello" button and beginning of name input callback chain
Begin = tkinter.Button(greeting_frame, text ='Hello', command = hello_call_back)
Begin.place(x=20, y=10)


# main window styling options
gui.title('Hello, Meta... Python Desktop Application')
gui.geometry('800x1000')

# run program
gui.mainloop()

# END of document
