import tkinter
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodor")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(window, text="Timer", font=(FONT_NAME, 35,"bold"),foreground=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
start_button = Button(window, text="Start", font=(FONT_NAME, 15,"bold"), width="5")
start_button.grid(column=0, row=2)

reset_button = Button(window, text="Reset", font=(FONT_NAME, 15,"bold"), width="5")
reset_button.grid(column=3, row=2)

checked_label =Label(text=" ✓", font=(FONT_NAME, 30,"bold"), width="5",foreground=GREEN, bg=YELLOW)
checked_label.grid(column=1, row=3)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"), anchor=CENTER)
canvas.grid(column=1, row=1, columnspan=2)
















window.mainloop()