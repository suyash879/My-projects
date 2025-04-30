import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter Calculator")
        self.configure(bg="#2e2e2e")
        self.geometry("300x400")
        self.resizable(True, True)

        self.expression = ""

        self.display = tk.Entry(self, font=("Arial", 20), bd=10, relief=tk.FLAT, justify="right", bg="#1c1c1c", fg="white")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.create_buttons()

        for i in range(5):  # 4 rows of buttons + 1 display
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def create_buttons(self):
        btn_texts = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', 'C', '+'),
            ('=',)
        ]

        for r, row in enumerate(btn_texts, start=1):
            for c, char in enumerate(row):
                btn = tk.Button(self, text=char, font=("Arial", 18), bg="#3e3e3e", fg="white",
                                activebackground="#5e5e5e", relief=tk.RAISED,
                                command=lambda ch=char: self.on_click(ch))
                btn.grid(row=r, column=c, sticky="nsew", padx=1, pady=1)

    def on_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        elif char == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
