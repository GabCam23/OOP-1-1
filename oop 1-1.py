from tkinter import *
window = Tk()

window.geometry("500x400+30+20")
window.title("Welcome to Python Programming")

btn = Button(window,text="Click to add name",fg ="blue")
btn.place(x=80, y=100)

lbl = Label(window,text="Student Personal Information",fg="maroon",bg="lightgreen")
lbl.place(relx=.5, y=50,anchor='center')
lbl2 = Label(window, text="Gender",fg="navyblue")
lbl2.place(x=80, y=150)

txtfld = Entry(window, bd=3,font=("Verdana",16))
txtfld.place(x=150, y=100)

v1 = StringVar()
v2 = StringVar()
v1.set(1)
r1 = Radiobutton(window, text="Male",value=1)
r1.place(x=80, y=180)
r2 = Radiobutton(window, text="Female",value=2)
r2.place(x=150, y=180)

v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
chkbox = Checkbutton(window, text="Basketball",variable=v3,)
chkbox2 = Checkbutton(window, text="Volleyball",variable=v4)
chkbox3 = Checkbutton(window, text="Soccer",variable=v5)
chkbox4 = Checkbutton(window, text="Other",variable=v6)

lbl3 = Label(window, text="Sports",fg="darkblue")
lbl3.place(x=80, y=230)

chkbox.place(x=80, y=260)
chkbox2.place(x=80, y=285)
chkbox3.place(x=160, y=260)
chkbox4.place(x=160, y=285)

lbl4 = Label(window, text="Subjects",fg="darkblue")
lbl4.place(x=80, y=345)

var = StringVar()
var.set("Calculus")
data1 = "Calculus"
data2 = "Physics"
data3 = "Object-Oriented Programming"
lstbox = Listbox(window, height=5,width=28,selectmode='multiple')
lstbox.insert(END,data1,data2,data3)
lstbox.place(x=80,y=365)

window.mainloop()
