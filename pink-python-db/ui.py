
# import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

import tkinter.messagebox
import tkinter.simpledialog

import logic
import data

gui = tkinter.Tk()


# frame and styling
s = Style()
s.configure('My.TFrame', background='pink')
db_frame = ttk.Frame(gui, width= 820, height= 620, style='My.TFrame')
db_frame['relief'] = 'raised'
db_frame.place(x= 40, y= 40)
db_frame.config()
db_frame.pack_propagate(False)

# text display area
db_display_frame = ttk.Frame(db_frame, width= 800, height= 450)
db_display_frame['relief'] = 'groove'
db_display_frame.place(x= 10, y= 160)
db_display_frame.pack_propagate(False)

# create text field
db_display_text=Text(db_display_frame)
db_display_text.pack(expand=True)
# db_display.place(x= 50, y= 100)

# title for section
section_title=Label(db_frame, text= "Create A Database")
section_title.place(x=10, y=10)

# label for user entry
enter_title=Label(db_frame, text= "Enter name below:")
enter_title.place(x=10, y=35)

# user entry field
F = tkinter.Entry(db_frame, width= 40 )
F.place(x=10, y=60)



# buttons
G = tkinter.Button(db_frame, text ='Create', command = data.create_db_driver)
G.place(x=260, y=56)

H = tkinter.Button(db_frame, text ='View All', command = data.view_all_db)
H.place(x=310, y=56)

I = tkinter.Button(db_frame, text ='Connect to:', command = data.connect_to_db)
I.place(x=380, y=56)

J = tkinter.Button(db_frame, text ='SQL Command:', command = data.sql_command)
J.place(x=400, y=26)

K = tkinter.Button(db_frame, text ='Show Tables', command = data.show_tables)
K.place(x=300, y=26)

# L = tkinter.Button(db_frame, text ='Cursor Contents', command = data.display_cursor)
# L.place(x=200, y=26)

M = tkinter.Button(db_frame, text ='Interface Call', command = logic.test)
M.place(x=100, y=126)

N = tkinter.Button(db_frame, text ='Interface Switch', command = lambda: logic.DependencyInjection.switch(1))
N.place(x=200, y=126)

O = tkinter.Button(db_frame, text ='Interface Switch', command = lambda: logic.DependencyInjection.switch(2))
O.place(x=300, y=126)

P = tkinter.Button(db_frame, text ='Interface Switch', command = lambda: logic.DependencyInjection.switch(3))
P.place(x=400, y=126)


# main window styling options
gui.title('PinkPython DB')
gui.geometry('900x700')

