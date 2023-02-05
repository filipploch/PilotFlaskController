from tkinter import *
from commands import start_timer, stop_timer, reset_timer, get_time, increment_seconds

window = Tk()

countdown_var = IntVar(value=1)


def get_countdown_flag():
    if countdown_var.get():
        return True
    return False
# add widgets here

btn_time_start = Button(window, text="Start", fg='blue', command=start_timer)
btn_time_start.place(x=50, y=100)
btn_time_stop = Button(window, text="Stop", fg='blue', command=stop_timer)
btn_time_stop.place(x=100, y=100)
btn_time_reset = Button(window, text="Reset", fg='blue', command=reset_timer)
btn_time_reset.place(x=150, y=100)
btn_time_add_second = Button(window, text="+", fg='blue', command=lambda: increment_seconds(1, get_countdown_flag()), height=1, width=1)
btn_time_add_second.place(x=130, y=0)
btn_time_reduce_second = Button(window, text="-", fg='blue', command=lambda: increment_seconds(-1, get_countdown_flag()), height=1, width=1)
btn_time_reduce_second.place(x=130, y=20)
btn_time_add_minute = Button(window, text="+", fg='blue', command=lambda: increment_seconds(60, get_countdown_flag()), height=1, width=1)
btn_time_add_minute.place(x=30, y=0)
btn_time_reduce_minute = Button(window, text="-", fg='blue', command=lambda: increment_seconds(-60, get_countdown_flag()), height=1, width=1)
btn_time_reduce_minute.place(x=30, y=20)
lbl = Label(window, fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)



check_time_countdown = Checkbutton(window, text='Countdown?'
                                   , variable=countdown_var
                                   , onvalue=1
                                   , offvalue=0
                                   )
check_time_countdown.place(x=100, y=130)


def check_time():
    lbl.config(text=get_time(get_countdown_flag()))
    lbl.after(200, check_time)


check_time()


window.title('Hello Python')
window.geometry("300x200+10+20")

