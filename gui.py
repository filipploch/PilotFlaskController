from tkinter import *
from commands import start_timer, stop_timer, reset_timer, get_time, increment_seconds
from frame_settings import create_frame_settings
from frame_timer import create_frame_timer

from setup import WINDOW_WIDTH

window = Tk()
countdown_var = IntVar(value=1)
create_frame_settings(window)
create_frame_timer(window, countdown_var)


window.title('Hello Python')
window.geometry(f'{WINDOW_WIDTH}x500')

