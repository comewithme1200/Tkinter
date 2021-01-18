from tkinter import *
from tkinter import messagebox


def showcaesar():
    win = Toplevel()
    win.title("Mã Ceasar")
    C = Caesar()
    def myclick():
        if plaintext.get() == "":
            messagebox.showinfo("Warning", "Bạn chưa nhập plaintext")
        elif Key.get() == "":
            messagebox.showinfo("Warning", "Bạn chưa nhập key")
        else:
            Encryptlb = Label(win, text=C.encrypt(int(Key.get()), plaintext.get()))
            Encryptlb.grid(row=3, column=1)
        # Create things
    plaintext = Entry(win, width=30)
    Key = Entry(win, width=30)
    myButton = Button(win, text='Encrypt', command=myclick)
    textlb = Label(win, text="Mật khẩu")
    textkey = Label(win, text="Key")
    # Geomatry
    plaintext.grid(row=0, column=1)
    Key.grid(row=1, column=1)
    myButton.grid(row=2, column=1)
    textlb.grid(row=0, column=0)
    textkey.grid(row=1, column=0)
    win.mainloop()
class Caesar:
    key = "abcdefghijklmnopqrstuvwxyz"
    def encrypt(self, k, plaintext):
        result = ""
        for l in plaintext:
            i = (self.key.index(l) + k) % len(self.key)
            result += self.key[i]
        return result
    def decrypt(self,k,ciphertext):
        result = ""
        for l in ciphertext:
            i = (self.key.index(l) - k) % len(self.key)
            result += self.key[i]
        return result
if __name__ == '__main__':
    main = Tk()
    main.title('Mã hóa cổ điển')
    sel = Button(main, text='Chọn',command=showcaesar)
    sel.pack()
    main.mainloop()
    #Functions









