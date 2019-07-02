import tkinter as tk


class Button:
    mainWindow     = None
    
    callBackMethod = None
    callBackParams = None
    
    buttonText     = None

    
    def __init__(self, mainWindow, *callBackArgs, buttonText = "", callBack = lambda: passCallBack()):
        self.mainWindow     = mainWindow
        self.callBackMethod = callBack
        self.callBackParams = callBackArgs
        self.buttonText     = buttonText
        
    def passCallBack(self):
        pass
   
    def addSimpleButton(self):
        button = tk.Button(self.mainWindow, 
                           text = self.buttonText, 
                           width = 25, 
                           command = lambda: self.callBackMethod(*self.callBackParams))
        button.pack()
