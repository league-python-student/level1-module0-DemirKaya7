import tkinter as tk

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.label = tk.Label(self, bg='grey', fg='white', text='first text')
        #self.label.place(x=0, y=0)
        self.label.place(relx=0.2, rely=0.2, relwidth=0.4, relheight=0.4)

        self.button = tk.Button(self, bg='pink', fg='black', command=lambda:button_clicked())
        self.button.place(x=0, y=0)

    def button_clicked(self):
        print('button clicked')

if __name__ == '__main__':
    app = App()

    app.title('my first python app')

    app.geometry('600x400')

    app.mainloop()