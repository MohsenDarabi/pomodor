import tkinter
from tkinter import *
import math
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
def start_timer():

    count_down(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        # count_sec = "0" + str(count_sec)
        count_sec =f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count -1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodor")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(window, text="Timer", font=(FONT_NAME, 35,"bold"),foreground=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
start_button = Button(window, text="Start", command=start_timer,font=(FONT_NAME, 15,"bold"), width="5" )
start_button.grid(column=0, row=2)

reset_button = Button(window, text="Reset", font=(FONT_NAME, 15,"bold"), width="5")
reset_button.grid(column=3, row=2)

checked_label =Label(text=" ✓", font=(FONT_NAME, 30,"bold"), width="5",foreground=GREEN, bg=YELLOW)
checked_label.grid(column=1, row=3)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"), anchor=CENTER)
canvas.grid(column=1, row=1)
















window.mainloop()