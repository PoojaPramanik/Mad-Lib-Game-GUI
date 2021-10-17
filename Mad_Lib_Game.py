from tkinter import *
window = Tk()
window.geometry("600x620")
window.config(bg="yellowgreen")
window.title("Mad Lib Game")

label = Label(window,text="MAD  LIB  GAME",font=("bold",15),bg="yellowgreen",fg="blue").place(x=190,y=2)

f = Frame(window,bg="salmon",borderwidth=5,relief=SUNKEN)
f.pack(side=BOTTOM,fill="y")

def submit():
    print("  ")
    label1=Label(f,text=f"Hi,I am  {object_value.get()}",bg="salmon" ).pack(ipadx=100,ipady=5)
    label2=Label(f,text=f"My Name is {foodname_value.get()}",bg="salmon" ).pack(ipadx=100,ipady=5)
    label3=Label(f,text=f"I studied in  {str(std_value.get()) } Class",bg="salmon").pack(ipadx=100,ipady=5)
    label4=Label(f,text=f"I lived in  {place_value.get()}",bg="salmon").pack(ipadx=100,ipady=5)
    label5=Label(f,text=f"I am a very {adjective_value.get()}  person.",bg="salmon").pack(ipadx=100,ipady=5)
    label6=Label(f,text=f"Nice to talk to you {object_1_value.get()}",bg="salmon").pack(ipadx=100,ipady=5)

def clear():
    object_value.set("") 
    foodname_value.set("")  
    std_value.set("") 
    place_value.set("")  
    adjective_value.set("")  
    object_1_value.set("")  
def exit_():
    window.destroy()

object = Label(text="Enter Object Name : ",bg="yellowgreen").place(x=100,y=30)
foodname = Label(text="Enter Food Name : ",bg="yellowgreen").place(x=100,y=50)
std = Label(text="Enter Your Favourite no.  : ",bg="yellowgreen").place(x=100,y=70)
place = Label(text="Enter Your favourite place Name : ",bg="yellowgreen").place(x=100,y=90)
adjective = Label(text="Enter any Adjective : ",bg="yellowgreen").place(x=100,y=110)
object_1 = Label(text="Enter Object Name : ",bg="yellowgreen").place(x=100,y=130)

object_value =  StringVar()
foodname_value =  StringVar()
std_value =  IntVar()
place_value =  StringVar()
adjective_value =  StringVar()
object_1_value =  StringVar()

object_entry = Entry(textvariable=object_value).place(x=350,y=30)
foodname_entry = Entry(textvariable=foodname_value).place(x=350,y=50)
std_entry = Entry(textvariable=std_value).place(x=350,y=70)
place_entry = Entry(textvariable=place_value).place(x=350,y=90)
adjective_entry = Entry(textvariable=adjective_value).place(x=350,y=110)
object_1_entry = Entry(textvariable=object_1_value).place(x=350,y=130)

f1 = Frame(window,bg="blue",borderwidth=5,relief=SUNKEN)
f1.pack(side=BOTTOM,fill="y",pady=100)

button1 = Button(f1,text="SUBMIT",command=submit,bg="grey").pack(side=LEFT,padx=20,ipadx=20,ipady=10)
button2 = Button(f1,text="CLEAR",command=clear,bg="grey").pack(side=LEFT,padx=20,ipadx=20,ipady=10)
button3 = Button(f1,text="EXIT",command=exit_,bg="grey").pack(side=LEFT,padx=20,ipadx=20,ipady=10)


window.mainloop()
