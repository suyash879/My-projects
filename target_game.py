import tkinter as tk
import random
import time

class ClickTargetGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Click the Target Game")
        self.root.geometry("500x500")
        self.root.configure(bg="#222")

        self.score = 0
        self.time_left = 30  # seconds

        self.canvas = tk.Canvas(self.root, width=500, height=400, bg="white")
        self.canvas.pack(pady=20)

        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 14), fg="white", bg="#222")
        self.score_label.pack()

        self.time_label = tk.Label(root, text=f"Time: {self.time_left}", font=("Arial", 14), fg="white", bg="#222")
        self.time_label.pack()

        self.target = self.canvas.create_oval(0, 0, 50, 50, fill="red", outline="")
        self.move_target()

        self.canvas.tag_bind(self.target, "<Button-1>", self.hit_target)

        self.update_timer()

    def move_target(self):
        x = random.randint(0, 450)
        y = random.randint(0, 350)
        self.canvas.coords(self.target, x, y, x + 50, y + 50)

    def hit_target(self, event):
        if self.time_left > 0:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.move_target()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.config(text=f"Time: {self.time_left}")
            self.root.after(1000, self.update_timer)
        else:
            self.canvas.unbind("<Button-1>")
            self.canvas.create_text(250, 200, text="⏰ Time's Up!", fill="black", font=("Arial", 24))

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickTargetGame(root)
    root.mainloop()
