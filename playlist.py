from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Playlist')
root.geometry("400x400)")
#Playlist file


>>> class Playlist:
            def __init__(self):
                pass
            def __addtopl__():
                pass
            def __deletefrompl__(self)
                pass
            












#create database
conn = sqlite3.connect('playlist.db')
 
c = conn.cursor()

#create table
'''
c.execute("""CREATE TABLE playlist (

            title text;

)""")

'''
#commit changes
conn.commit()




#close
conn.close()
root.mainloop()




