import tkinter


def helloCallBack():
    tkinter.messagebox.showinfo( "Hello Python", "Hello World")
    
   
def main():
    top = tkinter.Tk()


    top.mainloop()

if __name__ == '__main__':
    main()