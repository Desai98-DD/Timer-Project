from tkinter import * #tkinter is for gui
import time
from playsound import playsound #playsound is for import music to application

# window
root = Tk()
root.geometry('400x300')
root.resizable(0, 0)
root.config(bg='purple')
root.title('Countdown Clock And Timer')
Label(root, text='Countdown Clock and Timer', font='arial 20 bold', bg='purple').pack()
# time (current)
Label(root, font='arial 15 bold', text='current time :', bg='purple').place(x=40, y=70)


def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text=clock_time)
    curr_time.after(1000, clock)


curr_time = Label(root, font='arial 15 bold', text='', fg='gray25', bg='purple')
curr_time.place(x=190, y=70)
clock()
# timer
sec = StringVar()
Entry(root, textvariable=sec, width=2, font='arial 12').place(x=250, y=155)
sec.set('00')
mins = StringVar()
Entry(root, textvariable=mins, width=2, font='arial 12').place(x=225, y=155)
mins.set('00')
hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font='arial 12').place(x=200, y=155)
hrs.set('00')


# countdown
def countdown():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    while times > -1:
        minute, second = (times // 60, times % 60)

        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if (times == 0):
            playsound('audio.mp3')
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1


Label(root, font='arial 15 bold', text='set the time', bg='purple').place(x=40, y=150)

Button(root, text='START', bd='5', command=countdown, bg='antique white', font='arial 10 bold').place(x=150, y=210)

root.mainloop()
