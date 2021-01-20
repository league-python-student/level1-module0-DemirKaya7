from tkinter import messagebox, simpledialog, Tk
import tkinter as tk


# 4. Create an app like the one show in the pictures in this package, 'guest_book_add.png'
# and 'guest_book_print'
class GuestBook(tk.Tk):

    def __init__(self, parent):
        super().__init__(parent)

        self.guestNameList = list()
        self.newGuestName = ""
        self.finalString = str()

        addGuestButton = tk.Button(self, text='Add Guest', bg='White', fg='Black', command=lambda: self.addGuestButton_pressed())
        addGuestButton.place(x=0, y=150)
        viewGuestsButton = tk.Button(self, text='View Guests', bg='White', fg='Black', command=lambda: self.viewGuestsButton_pressed())
        viewGuestsButton.place(x=100, y=150)

    def addGuestButton_pressed(self):
        self.newGuestName = simpledialog.askstring(title="New Guest", prompt="Enter Guest Name")
        if self.newGuestName is not None:
            self.guestNameList.append(self.newGuestName)

    def viewGuestsButton_pressed(self):
        self.finalString = ""
        for i in range(len(self.guestNameList)):
            self.finalString = self.finalString + "\n" + str(i+1) + " " + self.guestNameList[i]
        messagebox.showinfo(title="Guest List", message=self.finalString)


if __name__ == '__main__':
    # 1. Make a new GuestBook
    gb = GuestBook(None)

    # 2. Set the title
    gb.title('Guest Book')

    # 3. Run your game's mainloop
    gb.mainloop()
