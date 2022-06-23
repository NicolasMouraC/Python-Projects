import math
import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_init = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer_init)
    pomodoro_counter.config(text="")
    timer.config(text="Timer", fg="green")
    canvas.itemconfig(timer_count, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_set = WORK_MIN * 60
    short_break_set = SHORT_BREAK_MIN * 60
    long_break_set = LONG_BREAK_MIN * 60
    reps += 1
    if reps == 8:
        count_down(long_break_set)
        timer.config(text="Long Break!", fg=GREEN)
    elif reps % 2 != 0:
        count_down(work_set)
        timer.config(text="Work time!", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_set)
        timer.config(text="Break time!", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer_init


    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer_init = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            pomodoro_counter.config(text='?' * math.floor(reps / 2), fg=PINK)
        #pomodoro_counter.config(text=reps)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

timer = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN)
timer.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224)
tomato_png = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_count = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=3)
reset_button = tkinter.Button(text="Reset", command=reset_timer,highlightthickness=0)
reset_button.grid(column=3, row=3)

pomodoro_counter = tkinter.Label(font=(FONT_NAME, 35, "bold"), fg=GREEN)
pomodoro_counter.grid(column=1, row=4)

window.mainloop()