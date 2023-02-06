from tkinter import *
from setup import WINDOW_WIDTH, WINDOW_HEIGHT
from commands import start_timer, stop_timer, reset_timer, get_time, increment_seconds


def create_frame_timer(window, countdown_var):
    frame_timer = Frame(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT/3, bg='yellow')
    frame_timer.grid(column=0, row=1)
    btn_time_start = Button(frame_timer, text="Start", fg='blue', command=start_timer)
    btn_time_start.grid(row=2 ,column=0)
    btn_time_stop = Button(frame_timer, text="Stop", fg='blue', command=stop_timer)
    btn_time_stop.grid(row=2 ,column=1)
    btn_time_reset = Button(frame_timer, text="Reset", fg='blue', command=reset_timer)
    btn_time_reset.grid(row=2 ,column=2 )
    btn_time_add_second = Button(frame_timer, text="+", fg='blue', command=lambda: increment_seconds(1, get_countdown_flag()), height=1, width=1)
    btn_time_add_second.grid(row=0 ,column=2)
    btn_time_reduce_second = Button(frame_timer, text="-", fg='blue', command=lambda: increment_seconds(-1, get_countdown_flag()), height=1, width=1)
    btn_time_reduce_second.grid(row=1 ,column=2)
    btn_time_add_minute = Button(frame_timer, text="+", fg='blue', command=lambda: increment_seconds(60, get_countdown_flag()), height=1, width=1)
    btn_time_add_minute.grid(row=0 ,column=0)
    btn_time_reduce_minute = Button(frame_timer, text="-", fg='blue', command=lambda: increment_seconds(-60, get_countdown_flag()), height=1, width=1)
    btn_time_reduce_minute.grid(row=1 ,column=0)
    lbl = Label(frame_timer, fg='red', font=("Helvetica", 16))
    lbl.grid(row=0 ,column=1, rowspan=2)
    
    
    check_time_countdown = Checkbutton(window, text='Countdown?'
                                       , variable=countdown_var
                                       , onvalue=1
                                       , offvalue=0
                                       )
    check_time_countdown.place(x=100, y=130)

    def get_countdown_flag():
        if countdown_var.get():
            return True
        return False

    def check_time():
        lbl.config(text=get_time(get_countdown_flag()))
        lbl.after(200, check_time)

    check_time()



