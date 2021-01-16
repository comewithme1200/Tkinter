from tkinter import *
win = Tk()
def myclick():
    Encryptlb = Label(win,text='ket qua: ')
    Encryptlb.grid(row=3,column=1)
mylabel1 = Label(win, text='My name is Long')
myButton = Button(win, text='Encrypt' , command=myclick)
myButton.grid(row=2,column=1)
mylabel1.grid(row=1, column=1)
win.mainloop()




