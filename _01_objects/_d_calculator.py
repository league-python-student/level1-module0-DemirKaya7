import tkinter as tk


class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()

        self.num1 = 2
        self.num2 = 4
        self.result = 0

        self.text_field1 = tk.Entry(self)
        self.text_field1.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.1)
        self.text_field2 = tk.Entry(self)
        self.text_field2.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.1)

        self.result_label = tk.Label(self, textvariable=self.result)
        self.result_label.place(relx=0.2, rely=0.7, relwidth=0.8, relheight=0.1)

        self.addbutton = tk.Button(self, text="+", command=lambda:self.addbutton_clicked())
        self.addbutton.place(relx=0.05, rely=0.3, relwidth=0.2, relheight=0.1)
        self.subtractbutton = tk.Button(self, text="-", command=lambda: self.subtractbutton_clicked())
        self.subtractbutton.place(relx=0.25, rely=0.3, relwidth=0.2, relheight=0.1)
        self.multiplybutton = tk.Button(self, text="x", command=lambda: self.multiplybutton_clicked())
        self.multiplybutton.place(relx=0.55, rely=0.3, relwidth=0.2, relheight=0.1)
        self.dividebutton = tk.Button(self, text="/", command=lambda: self.dividebutton_clicked())
        self.dividebutton.place(relx=0.75, rely=0.3, relwidth=0.2, relheight=0.1)

    def addbutton_clicked(self):
        self.result = self.num1 + self.num2
        print(self.result)

    def subtractbutton_clicked(self):
        self.result = self.num1 - self.num2
        print(self.result)

    def multiplybutton_clicked(self):
        self.result = self.num1 * self.num2
        print(self.result)

    def dividebutton_clicked(self):
        self.result = self.num1 / self.num2
        print(self.result)

if __name__ == '__main__':
    # Make a calculator app like the one shown in the calculator.png image
    # HINT: you'll need:
    # 1. a new class
    # 2. a StringVar variable
    # 3. Two tk.Entry widgets, four tk.Button widgets, and one tl.Label widget
    app = Calculator()
    app.geometry('800x300')

    app.mainloop()