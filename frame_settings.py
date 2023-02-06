from tkinter import *
from setup import WINDOW_WIDTH, WINDOW_HEIGHT


def create_frame_settings(window):
    frame_settings = Frame(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT/3, bg='blue')
    frame_settings.grid(row=0, column=0)

    btn_select_competition = Button(frame_settings, text="C")
    btn_select_competition.grid(row=0, column=0)

    btn_select_teamA = Button(frame_settings, text="A")
    btn_select_teamA.grid(row=0, column=1)

    btn_select_teamB = Button(frame_settings, text="B")
    btn_select_teamB.grid(row=0, column=2)

    btn_select_timer_countdown = Button(frame_settings, text="t↓")
    btn_select_timer_countdown.grid(row=0, column=3)
