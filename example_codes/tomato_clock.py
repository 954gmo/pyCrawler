# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import time
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()


def clock(t):
    times = tk.Label(window, text=t)
    times.place(x=window.winfo_width() / 2, y=window.winfo_height() / 2)
    tmp = int(t) * 60
    while tmp > -1:
        mins, secs = divmod(tmp, 60)
        time.sleep(1)
        times.configure(text=f"{mins}:{secs}")
        if tmp == 0:
            messagebox.showinfo("Time's Up")
        tmp -= 1


def main():
    window.title("SIG Tomato Clock")
    window.geometry('350x200')

    default_work_time = tk.IntVar()
    default_work_time.set(30)
    work_spin = tk.Spinbox(window, from_=1, to=60, width=5, textvariable=default_work_time)
    work_btn = tk.Button(window, text="Work", command=lambda: clock(work_spin.get()))

    default_break_time = tk.IntVar()
    default_break_time.set(10)
    break_spin = tk.Spinbox(window, from_=1, to=60, width=5, textvariable=default_break_time)
    break_btn = tk.Button(window, text="Break", command=lambda: clock(break_spin.get()))

    work_btn.grid(column=1, row=0)
    work_spin.grid(column=2, row=0)

    break_btn.grid(column=1, row=1)
    break_spin.grid(column=2, row=1)

    window.mainloop()


if __name__ == "__main__":
    main()
