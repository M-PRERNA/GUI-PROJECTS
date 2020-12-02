from tkinter import *

def find():
    try:
        org_price = int(original_entry.get())
        new_price = int(new_entry.get())

        ans = ((new_price-org_price)*100)/org_price
        display_feild.insert(10,str(ans)+"%")
    except:
        display_feild.insert(10,"not a valid input")



def clear():
    o_entry.set("")
    n_entry.set("")
    display.set("")
if __name__=="__main__":
    Gst_app = Tk()
    Gst_app.title('GST RATE FINDER')
    Gst_app.geometry('500x200')
    Gst_app.configure(background='black')

    # label 1: the heading
    gst_label=Label (Gst_app, text='GST RATE FINDER',bg='yellow',fg='black')
    gst_label.config(width=200,font=('Courier',30))
    gst_label.pack()

    o_entry = StringVar()
    n_entry = StringVar()
    display = StringVar()
    # to create an enter old price text box
    original = Label(Gst_app,text = 'ORIGINAL PRICE',bg='light blue')
    original.config(width=20,font=('Courier',12))
    original.pack()

    original_entry = Entry(Gst_app,bd=5,textvariable = o_entry)
    original_entry.pack()

    # to create an enter new price text box
    _new = Label(Gst_app,text = 'NEW PRICE',bg='light blue')
    _new.config(width=20,font=('Courier',12))
    _new.pack()

    new_entry = Entry(Gst_app,bd=5,textvariable=n_entry)
    new_entry.pack()
    # gst finder button
    finder = Button(Gst_app,text="FIND GST %",fg="black", bg="light green",command=find,width=10)
    finder.pack()
    # gst rate displayer  
    display_feild=Entry(Gst_app,bd=5,textvariable = display)  
    display_feild.pack()
    # to clear the feilds
    gst_clear = Button(Gst_app, text = "clear", fg = "black", bg = "grey", command = clear) 
    gst_clear.config(width=20,font=('Courier',12))
    gst_clear.pack()

    # cal_exit.grid(row = 6, column = 1) cant use with pack
    Gst_app.mainloop()