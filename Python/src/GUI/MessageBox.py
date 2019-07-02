from tkinter import messagebox
from tkinter.messagebox import QUESTION

class MessageBox:
    title   = "Title"
    message = "Message"
    
    def __init__(self, title = "Title", message = "Message"):
        self.title   = title
        self.message = message
        
        
    def showInfoBox(self):
        messagebox.showinfo(self.title, self.message)
        
    
    def showAskOrCancel(self):        
        messagebox.askokcancel(self.title, self.message)