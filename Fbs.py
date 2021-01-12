#voting poll
#import packages

import sqlite3
from tkinter import *
import tkinter
from tkinter import messagebox
import re

window = Tk()
window.geometry("1366x768")

#title
tit = Label(window,text="*** FeedBack System ***",font=("Courier",20,"bold")).place(x=580,y=20)
hr = Frame(window,height=5,width=1315,bg="black")
hr.place(x=20,y=55)
def Signup():
        name_var = tkinter.StringVar()
        email_var = tkinter.StringVar()
        pass_var = tkinter.StringVar()
        repass_var = tkinter.StringVar()
        def verify():

            name = name_var.get()
            email = email_var.get()
            password = pass_var.get()
            repass = repass_var.get()
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if name == "":
               messagebox.showerror("showerror","kindly provide valid user name")
            if re.search(regex,email):
                if password != repass :
                    messagebox.showerror("showerror","Password does not matched")
                    pass_var.set("")
                    repass_var.set("")
                else :
                    messagebox.showinfo("showeinfo","registered successfully")
                    conn = sqlite3.connect('feedback.db')
                    #conn.execute('''CREATE TABLE VOTEBANK 
                                  # ( NAME TEXT NOT NULL,EMAIL TEXT NOT NULL,PASSWORD TEXT NOT NULL);''' )
                    #once the table is created no need to call Create cammand again
                    conn.execute("""INSERT INTO DETAILS (NAME,EMAIL,PASSWORD) VALUES (?,?,?)""",(name,email,password))
                    conn.commit()
                    conn.close()
                    name_var.set("")
                    email_var.set("")
                    pass_var.set("")
                    repass_var.set("")
                    
            else :
                print("Invalid mail")
                messagebox.showerror("showerror","Invalid Email")
                email_var.set("")   
            
            
        tit = Label(window,text="New user,Register to Signup!!!",font=("Courier",15,"bold")).place(x=580,y=200)
        hr = Frame(window,height=5,width=1315,bg="black")
        hr.place(x=20,y=240)
        user_name = Label(window,text = "Username",font=("Courier",10)).place(x=580,y=260)
        user_input = Entry(window,textvariable=name_var,width=30).place(x=660,y=260)
        email = Label(window,text = "Email",font=("Courier",10)).place(x=580,y=300)
        email_input = Entry(window,textvariable=email_var,width=30).place(x=660,y=300)
        password = Label(window,text = "Password",font=("Courier",10)).place(x=580,y=340)
        pass_input = Entry(window,textvariable=pass_var,show="*",width=30).place(x=660,y=340)
        repassword = Label(window,text = "Retype Password",font=("Courier",10)).place(x=520,y=380)
        repass_input = Entry(window,textvariable=repass_var,show="*",width=30).place(x=660,y=380)
        verify1 = Button(window,text="Register",command=verify,width=20).place(x=600,y=450)
       
#login
def login():
    name_var1 = tkinter.StringVar()
    pass_var1 = tkinter.StringVar()
   

    def pollPage():
        
        win = Tk()
        win.geometry("1300x700") 
        staff_name_var = tkinter.StringVar(win)
        staff_code_var = tkinter.StringVar(win)
        student_name_var = tkinter.StringVar(win)
        Q1 = tkinter.StringVar(win)
        Q2 = tkinter.StringVar(win)
        Q3 = tkinter.StringVar(win)
        def vote1(win):
            staff_name = staff_name_var.get()
            staff_code = staff_code_var.get()
            student = student_name_var.get()
            val1 = Q1.get()
            val2 = Q2.get()
            val3 = Q3.get()
            conn = sqlite3.connect('feedback.db')
            conn.execute("""INSERT INTO FEED (STAFFNAME,SUBJECTCODE,STUDENTNAME,Q1,Q2,Q3) VALUES (?,?,?,?,?,?) """,(staff_name,staff_code,student,val1,val2,val3))
            messagebox.showinfo("showeinfo","your vote has been recorded  successfully!!!")
            name_var1.set("")
            pass_var1.set("")
            conn.commit()
            conn.close()
        Label(win,text="STAFF NAME ",font=("Courier",10,"bold")).place(x=500,y=20)
        user_input = Entry(win,textvariable=staff_name_var,width=30).place(x=610,y=20)
        Label(win,text="SUBJECT CODE ",font=("Courier",10,"bold")).place(x=500,y=50)
        user_input = Entry(win,textvariable=staff_code_var,width=30).place(x=610,y=50)
        Label(win,text="STUDENT NAME ",font=("Courier",10,"bold")).place(x=500,y=90)
        user_input = Entry(win,textvariable=student_name_var,width=30).place(x=610,y=90)
        ques1 = Label(win,text="1.Given a chance,What is one change that you would like to see?",font=("Courier",10,"bold")).place(x=350,y=110)
        Ao1 = Radiobutton(win,text="Teaching Method",variable= Q1,value="Teaching Method").place(x=550,y=140)
        Ao2 = Radiobutton(win,text="Time taken to complete a chapter",variable= Q1,value="Time taken to complete a chapter").place(x=550,y=180)
        Ao3 = Radiobutton(win,text="Extracuricular activities",variable= Q1,value="Extracuricular activities").place(x=550,y=220)
        Ao4 = Radiobutton(win,text="Others",variable= Q1,value="Others").place(x=550,y=260)
        ques2 = Label(win,text="2.Do you think that the staff provides you adequate books and materials",font=("Courier",10,"bold")).place(x=350,y=300)
        Bo1 = Radiobutton(win,text="yes",variable= Q2,value="yes").place(x=550,y=340)
        Bo2 = Radiobutton(win,text="no",variable= Q2,value="no").place(x=550,y=380)
        ques3 = Label(win,text="3.My teacher has fair rules for the class and is extermely impartial",font=("Courier",10,"bold")).place(x=350,y=420)
        Co1 = Radiobutton(win,text="Agree",variable= Q3,value="Agree").place(x=550,y=500)
        Co2 = Radiobutton(win,text="Netural",variable= Q3,value="Netural").place(x=550,y=540)
        Co2 = Radiobutton(win,text="Disagree",variable= Q3,value="Disagree").place(x=550,y=580)
        Button(win,text="Vote",command=lambda :vote1(win),width=20).place(x=550,y=620)
        Button(win,text="logout",command=win.destroy,width=20).place(x=700,y=620)
        win.mainloop()
    
    def loginverify():

        nameval = name_var1.get()
        passval = pass_var1.get()
        conn = sqlite3.connect('feedback.db')
        ele = conn.execute("""SELECT password,email FROM DETAILS WHERE name = ?""",(nameval,))
        ele = ele.fetchall()

        for val in ele :
            if val[0] == passval :
                pollPage()
                break
            else:
                messagebox.showerror("showerror","invalid userid or password")
                break
        
        else:
            messagebox.showerror("showerror","invalid userid or password")
       
        conn.commit()
        conn.close()
    user_name = Label(window,text = "Username",font=("Courier",10)).place(x=580,y=70)
    user_input = Entry(window,textvariable=name_var1,width=30).place(x=660,y=70)
    password = Label(window,text = "Password",font=("Courier",10)).place(x=580,y=110)
    pass_input = Entry(window,textvariable=pass_var1,width=30,show="*").place(x=660,y=110)
   
    login = Button(window,text="login",command=loginverify, width=20).place(x=580,y=150)
    signup = Button(window,text="signup",width=20,command=Signup).place(x=740,y=150)
login()
window.mainloop()