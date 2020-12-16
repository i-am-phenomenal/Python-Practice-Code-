import schedule 
import time 
import pyautogui as auto
import random
import tkinter as tk

# import tkinter as tk

# master = tk.Tk()
# master.geometry('200x200')
# tk.Label(master, text="First Name").grid(row=0)
# e1 = tk.Entry(master)
# e1.grid(row=0, column=1)
# button = tk.Button(master, text='Submit', width=25, command=master.destroy).grid(row=3, column=3)
# # button.pack()

# master.mainloop()

# window=tk.Tk()
# window.title("AUTO MOUSE MOVER VERSION 2.0 ")
# window.geometry('200x200')
# tk.Label(window, text="Enter the time after which you want the mouse to be moved").grid(row=0)
# button = tk.Button(window, text='Submit', width=25, command=window.destroy)
# button.pack()
# window.mainloop()

def move_mouse(): 
    random_x_coord = random.randint(0, 1366)
    random_y_coord = random.randint(0, 768)
    auto.moveTo(random_x_coord, random_y_coord, duration  = 1)

schedule.every(2).seconds.do(move_mouse)

while True: 
    schedule.run_pending()
    time.sleep(1)
