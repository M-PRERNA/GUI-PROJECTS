from tkinter import *
import calendar
def thecalendar():
    cal_window =Tk()
    cal_window.title('Your Calendar')
    cal_window.geometry('500x500')
    cal_window.configure(background='black')
    cal_label=Label(cal_window, text='CALENDAR',bg='pink',fg='black')
    cal_label.config(width=200,font=('Helvetica',30))
    cal_label.pack()

    year = int (cal_year_field.get())
    view_cal=calendar.calendar(year)

    view_cal_year = Label(cal_window,text = view_cal,font='Helvetica')
    view_cal_year.configure(height=100,width=100,font=('Helvetica',12))
    view_cal_year.pack(fill=BOTH)
    # view_cal_year.grid(row = 5, column = 1, padx = 20)
    cal_window.mainloop()




    # pass
if __name__=="__main__":
    Calendar_app = Tk()
    Calendar_app.title('CALENDAR')
    Calendar_app.geometry('500x200')
    Calendar_app.configure(background='black')
    # label 1: the heading
    cal_label=Label(Calendar_app, text='CALENDAR',bg='yellow',fg='black',bd=5)
    cal_label.config(width=200,font=('Helvetica',30))
    cal_label.pack()
    # to create an enter year text box
    cal_year = Label(Calendar_app, text = "Enter Year", bg = "yellow") 
    cal_year.config(width=50,font=('Helvetica',15))
    cal_year_field = Entry(Calendar_app)
    cal_year_field.pack()
    cal_year.pack()
   

    #to show the calendar-show button
    cal_show = Button(Calendar_app,text= "-Show calendar-",bg="gray",command=thecalendar)
    cal_show.configure(width = 20)
    cal_show.pack()

    # to exit the app
    cal_exit = Button(Calendar_app, text = "EXIT", fg = "white", bg = "red", command = exit) 
    cal_exit.configure(width=20)
    cal_exit.pack()

    # cal_exit.grid(row = 6, column = 1) cant use with pack
    Calendar_app.mainloop()