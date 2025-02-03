from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN * 60

    '''
# What have done:
# If it's the 8th rep:
  count_down(long_break_sec)
# If it's the 1st/3rd/5th/7th rep:
  count_down(work_break_sec)
# If it's 2nd/4th/6th rep:
  count_down(short_break_sec)
'''
    if reps % 8==0:
        title_label.config(text = "BREAK", fg = RED)
        count_down(long_break_sec)
    elif reps % 2 ==0:
        title_label.config(text="BREAK",fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text = "WORK",fg = GREEN)
        count_down(work_sec)


    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text,text =f"{count_min}:{count_sec:02}") #The canvas.itemconfig() method is used to modify properties (like color, text, image, etc.) of an existing item on a Tkinter Canvas. #canvas.itemconfig(item_id, option=value)  [option=value → The new property value to set] 
    
    if count > 0:
       global timer
       timer =  window.after(1000,count_down,count - 1) #The after() method in Tkinter is used to schedule a function to run after a specified time delay (in milliseconds). It is commonly used for timers, animations, and periodic updates without freezing the GUI. #widget.after(delay, function, *args)
    else:
        start_timer() 
        #Adding a check mark after every work session.
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks +="✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=YELLOW)


title_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
title_label.grid(column=1,row=0)



canvas = Canvas(width = 200,height = 224,bg = YELLOW,highlightthickness=0)  #Canvas is a widget that allows drawing graphics, layering images, and creating custom shapes.
tomato_img = PhotoImage(file="pomodoro-start/tomato.png") #PhotoImage is a class used to handle and display images (in PNG, GIF, or PPM/PGM formats) in GUI applications.
canvas.create_image(100,112,image = tomato_img)
timer_text = canvas.create_text (100,130,text = "00:00",fill = "white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)



start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column = 2, row = 2)

check_marks = Label(fg = GREEN,bg = YELLOW)
check_marks.grid(column=1,row=3)





window.mainloop()
