from tkinter import *
from tkinter import messagebox
import pyautogui
import time



def fun(str,n):

    messagebox.showinfo('info'," From now you have 10 seconds to place the pointer and click at \n"
      "the text box where you have to send the text")
    time.sleep(3)
    for i in range(n):
        for j in str:
            if j == ' ':
                pyautogui.press('space')
            else:
                pyautogui.press(j)
        pyautogui.press('enter')

class MainWindow(Tk):
    def __init__(self):
        self.window=Tk()
        self.frame1=Frame(self.window,height=300,width=800)
        self.frame1.pack(fill=X)
        self.frame2 = Frame(self.window, height=300, width=800)
        self.frame2.pack(fill=X)
        self.entry1=Entry(self.frame1,font=('Times New Roman',40))
        self.entry1.place(y=160,x=140)
        self.entry2 = Entry(self.frame2, font=('Times New Roman', 40))
        self.entry2.place(y=100, x=140)
        self.entry1.config(bg='#963656')
        self.entry2.config(bg='#963656')
        self.label=Label(self.frame2,bg='#551DB5',text='Submit',font=('Times New Roman',40))
        self.label.place(x=340,y=230)
        self.label.bind('<Button-1>',self.click)
        self.entry1.insert(0,'Enter text')
        self.entry2.insert(0,'Enter the number')
        self.entry1.bind('<Button-1>',lambda event:self.entry1.delete(0,END))
        self.entry2.bind('<Button-1>',lambda event:self.entry2.delete(0,END))

    def click(self,event):
        print("clicked")
        if self.entry2.get().isnumeric() is True:
            fun(self.entry1.get(),int(self.entry2.get()))
        else:
            messagebox.showerror('error','numbr is numeric not string')





obj=MainWindow()
obj.window.geometry('800x600')
obj.window.resizable(height=False,width=False)
obj.window.mainloop()