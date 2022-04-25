from tkinter import *
window = Tk()

window.geometry("500x400+30+20")
window.title("Midterms in OOP")

def your_name():
    fullname = fullname_yn.get()

    txtfld.insert(0,f'{fullname}')

fullname_yn = Entry(window, bd = 3,fg="maroon",bg="lightgreen")
fullname_yn.place(x=300,y=100)

lbl = Label(window, text = "Enter your Fullname",  fg="maroon",bg="lightgreen")
lbl.place(x=60, y=100)

btn = Button(window,text = "Click to display your Fullname",fg="maroon",bg="lightgreen", command=your_name)
btn.place(x=60,y=150)
btn.pack

txtfld = Entry(window, bd = 3,fg="maroon",bg="lightgreen")
txtfld.place(x=300,y=150)
txtfld.pack

fullname_yn.pack

window.mainloop()








