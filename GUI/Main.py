import GUI.Button as button
import GUI.MessageBox as msgBox
import tkinter as tk

    
def printCallBack(*parameters):
    print("Log: ", end='')
    
    for word in parameters:
        print(word + " ", end='')
        
    print()


def main():
    mainWindow = tk.Tk()
    
    mainWindow.title("Main Window")
    
    newMsg = msgBox.MessageBox("Tit", "Mess")
    
    newButton = button.Button(mainWindow, buttonText = "A button", callBack = newMsg.showAskOrCancel)
    
    newButton.addSimpleButton()

    mainWindow.mainloop()


if __name__ == '__main__':
    main()
