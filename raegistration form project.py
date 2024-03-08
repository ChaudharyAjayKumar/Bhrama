from tkinter import *
from tkinter import ttk
root=Tk()
root.title("registration form")
root.geometry("580x670+100+50")

#fuction decelartion
def show_data():
    if check_var.get()=="on":
        get_data=f'Name:{name_var.get()}\nEmail:{email_var.get()}\nGender:{gender_var.get()}'
        my_data.config(text=get_data,font=("arial",15,"bold"))    
    else :
        my_data.config(text="Please Accept Our Terms")


title_name=Label(root,text="STUDENT ENTRY FORM",font=("arial",30,"bold"),bg="white",fg="blue")
title_name.pack(side=TOP)

main_frame=Frame(root,bd=3,relief=RIDGE)
main_frame.place(x=20,y=70,width=550,height=580)

#Labels
name=Label(main_frame,text="Student Name",font=("arial",15,"bold"))
name.grid(row=0,column=0,padx=10,pady=10)

email=Label(main_frame,text="Student Email",font=("arial",15,"bold"))
email.grid(row=1,column=0,padx=10,pady=10)

gender=Label(main_frame,text=" Select Gender",font=("arial",15,"bold"))
gender.grid(row=2,column=0,padx=10,pady=10)

#variable
name_var=StringVar()
email_var=StringVar()
gender_var=StringVar()
check_var=StringVar()


#Entry
name_entry=Entry(main_frame,textvariable=name_var,font=("arial",15,"bold"),width=20,highlightthickness=2)
name_entry.grid(row=0,column=1,padx=10,pady=10)

email_entry=Entry(main_frame,textvariable=email_var,font=("arial",15,"bold"),width=20,highlightthickness=2)
email_entry.grid(row=1,column=1,padx=10,pady=10)


#Radiobutton
male=Radiobutton(main_frame,variable=gender_var,text="Male",font=("arial",15,"bold"),value="male")
male.grid(row=2,column=1,pady=2,sticky="w")                                                     #sticky is used to place male left most side ,anchor show error
gender_var.set("male")

female=Radiobutton(main_frame,variable=gender_var,text="Female",font=("arial",15,"bold"),value="female")
female.grid(row=3,column=1,pady=2,sticky="w")

#Checkbutton
check_btn=Checkbutton(main_frame,variable=check_var,onvalue="on",offvalue="off",text="Agree Our Terms  & Condition",font=("arial",15,"bold"))
check_btn.grid(row=4,column=1,padx=10,pady=10,sticky="w")
check_var.set(0)


#Button
Btn=Button(main_frame,text="Show Data",font=("arial",15,"bold"),bg="blue",fg="white",command=show_data)
Btn.grid(row=5,column=1,pady=2,sticky="w")

my_data=Label(main_frame,text="",font=("arial",15,"bold"))
my_data.grid(row=6,column=1,padx=10,pady=10)

root.mainloop()