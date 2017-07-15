# https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard-on-windows-using-python/4203897#4203897
from tkinter import *
c = Tk()
c.withdraw()
c.clipboard_clear()
c.clipboard_append('i can has clipboardz?')
c.update() # now it stays on the clipboard after the window is closed
# c.destroy()