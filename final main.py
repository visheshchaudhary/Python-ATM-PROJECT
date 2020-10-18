import sqlite3
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("MAIN")
root.geometry("1300x720+0+0")
root.config(bg="dark slate grey")
root.overrideredirect(1)
l0=Label(root,text="WELCOME TO MY BANK",font=("STENCIL", 28, "bold"),bg="dark slate gray", fg="white")
l0.pack()
l01=Label(root,text="",bg="dark slate gray")
l01.pack()
l03=Label(root,text="",bg="dark slate gray")
l03.pack()
l04=Label(root,text="",bg="dark slate gray")
l04.pack()
l02=Label(root,text="",bg="dark slate gray")
l02.pack()
l05=Label(root,text="",bg="dark slate gray")
l05.pack()
l06=Label(root,text="",bg="dark slate gray")
l06.pack()
l07=Label(root,text="",bg="dark slate gray")
l07.pack()
l1=Label(root,text=("ENTER PIN"),font=("STENCIL", 28, "bold"),bg="dark slate gray",fg="white")
l1.pack()
e1=Entry(root,show='*',bg="dark slate gray",fg="white",bd='30')
e1.pack()    
def pinchange():
    top1=Toplevel()
    top1.title("PIN CHANGE")
    top1.geometry("1300x720+0+0")
    top1.config(bg="dark slate grey")
    top1.overrideredirect(1)
    l=Label(top1,text="ENTER NEW PIN").pack()
    e2=Entry(top1,bg="aquamarine",show="*")
    e2.pack()
    l1=Label(top1,text="CONFIRM PIN").pack()
    e3=Entry(top1,bg="aquamarine",show="*")
    e3.pack()
    p1=int(e1.get())  
    def s1():
        x1=int(e2.get())
        x2=int(e3.get())
        if(x1!=x2):
            msg=messagebox.showinfo("ERROR","PINS NOT MATCHED.RETRY!!!!")
            pinchange()
        else:
            c11=sqlite3.connect("info.db")
            c11.execute("update userinfo set pin = ? where pin = ?",(x1,p1))
            c11.commit()
            messagebox.showinfo("INFO"," PIN SUCCESSFULLY CHANGED!!!!")
            root.destroy()
    def validate():
        if(len(e2.get())==0):
            messagebox.showinfo("ERROR","PLEASE ENTER THE PIN !!!")
            pinchange()
        if(len(e2.get()) not in (0,4)):
            messagebox.showinfo("ERROR","PIN MUST BE OF 4 DIGITS !!!")
            pinchange()
        if(len(e2.get())!=0 and len(e3.get())==0):
            messagebox.showinfo("ERROR","PLEASE CONFIRM THE PIN !!!")
            pinchange()
        if(len(e2.get())==4):
            x=str(e2.get())
            for i in range(0,4):
                if(ord(x[i])in range(48,58)):
                    if(i>=3):
                        s1()
                    else:
                        i=i+1   
                elif(ord(x[i]) not in range(48,58)):
                    messagebox.showinfo("ERROR","ALPHABETS AND SPECIAL CHARACTERS NOT ALLOWED !!!")
                    pinchange()
                    break
    def cancel1():
        msg=messagebox.askyesno('Login page',"DO YOU WANT TO EXIT !!!")
        if(msg):
            root.destroy()
        else:
            pinchange()
    b=Button(top1,text="UPDATE AND EXIT",bd=10,bg="dark slate grey",fg="white",command=validate).pack()
    b1=Button(top1,text="EXIT",bd=10,bg="red",command=cancel1)
    b1.pack(side='bottom')
    b2=Button(top1,text="MAIN MENU",bd=10,bg="dark slate gray",fg="white",command=options)
    b2.pack(side='bottom')   
def deposit():
    top2=Toplevel()
    top2.title("DEPOSIT")
    top2.geometry("1300x720+0+0")
    top2.config(bg="dark slate grey")
    top2.overrideredirect(1)
    l=Label(top2,text="AMOUNT",bd=20,font=("STENCIL", 18, "bold"),bg="dark slate grey",fg="white").pack()
    e2=Entry(top2,bg="aquamarine")
    e2.pack()
    p1=int(e1.get())
    def validate1():
        if(len(e2.get())== 0):
            messagebox.showinfo("ERROR","PLEASE ENTER THE AMOUNT !!!")
            deposit()
        else:
             x=str(e2.get())
             l=len(e2.get())
             for i in range(0,l):
                 if(ord(x[i])in range(48,58)):
                     if(i>=l-1):
                         s1()
                     else:
                         i=i+1   
                 elif(ord(x[i]) not in range(48,58)):
                     messagebox.showinfo("ERROR"," INVALID ENTRY !!!")
                     deposit()
                     break
    def s1():
            x1=int(e2.get())
            with sqlite3.connect("info.db") as db:
                c=db.cursor()
            c11=sqlite3.connect("info.db")
            b=("select balance from userinfo where pin = ?")
            c.execute(b,[(p1)])
            r1=c.fetchall()
            y=list(r1[0])
            l=[]
            l.append(x1)
            c1=y[0]+l[0]
            c12=int(c1)
            c11.execute("update userinfo set balance = ? where pin = ?",(c1,p1) )
            c11.commit()
            messagebox.showinfo("DEPOSIT","MONEY SUCCESSFULLY DEPOSITED.CLICK OK TO CHECK BALANCE.")
            balance()
    def cancel2():
        msg=messagebox.askyesno('Login page',"DO YOU WANT TO EXIT !!!")
        if(msg):
            root.destroy()
        else:
            deposit()
    b8=Button(top2,text="PROCEED",bd=10,command=lambda:validate1())
    b8.pack()
    b1=Button(top2,text="EXIT",bd=10,bg="red",command=cancel2)
    b1.pack(side='bottom')
    b2=Button(top2,text="MAIN MENU",bd=10,bg="dark slate gray",fg="white",command=options)
    b2.pack(side='bottom')
def withdrawl():
        top3=Toplevel()
        top3.title("WITHDRAWL")
        top3.geometry("1300x720+0+0")
        top3.config(bg="dark slate grey")
        top3.overrideredirect(1)
        l=Label(top3,text="AMOUNT",bd=20,font=("STENCIL", 18, "bold"),bg="dark slate grey",fg="white").pack()
        e2=Entry(top3,bg="aquamarine")
        e2.pack()
        p1=int(e1.get())
        def s1():    
               x1=int(e2.get())
               with sqlite3.connect("info.db") as db:
                  c=db.cursor()
               c11=sqlite3.connect("info.db")
               b=("select balance from userinfo where pin = ?")
               c.execute(b,[(p1)])
               r1=c.fetchall()
               y=list(r1[0])
               l=[]
               l.append(x1)
               c1=y[0]-l[0]
               if(c1<0):
                   messagebox.showinfo("ERROR","INSUFFICIENT BALANCE !!!")
                   options()
               if(c1>=0):
                   c11.execute("update userinfo set balance = ? where pin = ?",(c1,p1) )
                   c11.commit()
                   msg=messagebox.showinfo("DEPOSIT","MONEY SUCCESSFULLY WITHDRAWN.CLICK TO CHECK BALANCE")
                   balance()
        def validate1():
            if(len(e2.get())== 0):
                messagebox.showinfo("ERROR","PLEASE ENTER THE AMOUNT !!!")
                withdrawl()
            else:
                x=str(e2.get())
                l=len(e2.get())
                for i in range(0,l):
                    if(ord(x[i])in range(48,58)):
                        if(i>=l-1):
                            s1()
                        else:
                            i=i+1   
                    elif(ord(x[i]) not in range(48,58)):
                       messagebox.showinfo("ERROR"," INVALID ENTRY !!!")
                       withdrawl()
                       break
        def cancel3():
            msg=messagebox.askyesno('Login page',"DO YOU WANT TO EXIT !!!")
            if(msg):
               root.destroy()
            else:
                withdrawl()
        b8=Button(top3,text="PROCEED",bd=10,command = lambda:validate1())
        b8.pack()
        b1=Button(top3,text="EXIT",bd=10,bg="red",command=cancel3)
        b1.pack(side='bottom')
        b2=Button(top3,text="MAIN MENU",bd=10,bg="dark slate gray",fg="white",command=options)
        b2.pack(side='bottom')      
def balance():
    top4=Toplevel()
    top4.title("BALANCE")
    top4.geometry("1300x720+0+0")
    top4.config(bg="dark slate grey")
    top4.overrideredirect(1)
    p1=int(e1.get())
    with sqlite3.connect("info.db") as db:
        c=db.cursor()
    b=("select balance from userinfo where pin = ?")
    c.execute(b,[(p1)])
    r1=c.fetchall()
    v1=StringVar()
    v1.set(r1[0])
    l21=Label(top4,text="AVAILABLE BALANCE ",bd=20,font=("STENCIL", 18, "bold"),bg="dark slate grey",fg="white").pack()
    l2=Label(top4,textvariable=v1,bd=20,font=("STENCIL", 18, "bold"),bg="dark slate grey",fg="white")
    l2.pack()
    l2.config(font=50)
    def cancel4():
        msg=messagebox.askyesno('Login page',"DO YOU WANT TO EXIT !!!")
        if(msg):
            root.destroy()
        else:
            balance()
    b1=Button(top4,text="EXIT",bd=10,bg="red",command=cancel4)
    b1.pack(side='bottom')
    b2=Button(top4,text="MAIN MENU",bd=10,bg="dark slate gray",fg="white",command=options)
    b2.pack(side='bottom')  
def retry():
    top5=Toplevel()
    top5.title("RETRY")
    top5.geometry("1300x720+0+0")
    top5.config(bg="dark slate grey")
    top5.overrideredirect(1)
    l2=Label(top5,text="INCORRECT PIN",font=("STENCIL", 18, "bold"),bg="dark slate gray", fg="white")
    l2.pack()
    l3=Label(top5,text="",font=("STENCIL", 18, "bold"),bg="dark slate gray")
    l3.pack()
    l4=Label(top5,text="",font=("STENCIL", 18, "bold"),bg="dark slate gray",)
    l4.pack()
    b7=Button(top5,text="RETRY",bd=10,bg="dark slate grey",fg="white",command=root.deiconify)
    b7.pack()
    def cancel5():
        msg=messagebox.askyesno('RETRY',"DO YOU WANT TO EXIT !!!")
        if(msg):
            root.destroy()
        else:
            retry()
    b1=Button(top5,text="EXIT",bd=10,bg="red",command=cancel5)
    b1.pack(side='bottom')
def options():
    top=Toplevel()
    top.title("OPTIONS")
    top.geometry("1300x720+0+0")
    top.config(bg="dark slate grey")
    top.overrideredirect(1)
    p2=int(e1.get())
    with sqlite3.connect("info.db") as db:
        c=db.cursor()
    b=("select name from userinfo where pin = ?")
    c.execute(b,[(p2)])
    v1=StringVar()
    r1=c.fetchall()
    v1.set(r1[0])
    l3=Label(top,text="WELCOME",font=("STENCIL", 18, "bold"),bg="dark slate gray", fg="white")
    l3.pack()
    l2=Label(top,textvariable=v1,font=("STENCIL", 18, "bold"),bg="dark slate gray", fg="white")
    l2.pack()
    l30=Label(top,text="",bg="dark slate gray").pack()
    l31=Label(top,text="",bg="dark slate gray").pack()
    b2=Button(top,text="CHECK BALANCE ",bd=50,bg="dark slate grey",fg="white",command=balance )
    b2.pack()
    b3=Button(top,text="DEPOSIT  MONEY",bd=50,bg="dark slate grey",fg="white",command=deposit)
    b3.pack()
    b4=Button(top,text="    WITHDRAWL    ",bd=50,bg="dark slate grey",fg="white",command=withdrawl)
    b4.pack()
    b5=Button(top,text="    PIN CHANGE    ",bd=50,bg="dark slate grey",fg="white",command=pinchange)
    b5.pack()
    def cancel6():
        msg=messagebox.askyesno('Login page',"DO YOU WANT TO EXIT !!!")
        if(msg):
            root.destroy()
        else:
            options()
    b6=Button(top,text="EXIT",bd=5,bg="red",command=cancel6)
    b6.pack(side='bottom')   
def login():
    p=int(e1.get())
    with sqlite3.connect("info.db") as db:
        c=db.cursor()
    find_user=("select * from userinfo where pin = ?")
    c.execute(find_user,[(p)])
    results=c.fetchall()
    x=0
    if results:
        for i in results:
            options()
    if(p not in results):
        retry()         
def check_null():
    if(len(e1.get()) not in (0,4)):
        messagebox.showinfo("ERROR","PIN MUST BE OF 4 DIGITS !!!")
    elif(len(e1.get())==0):
        messagebox.showinfo("ERROR","PLEASE ENTER YOUR PIN !!!")   
    else:
        x=str(e1.get())
        for i in range(0,4):
            if(ord(x[i])in range(48,58)):
                if(i>=3):
                    login()
                else:
                    i=i+1   
            elif(ord(x[i]) not in range(48,58)):
                messagebox.showinfo("ERROR","ALPHABETS AND SPECIAL CHARACTERS NOT ALLOWED !!!")
                break
def cancel():
    msg=messagebox.askyesno('LOGIN',"DO YOU WANT TO EXIT !!!")
    if(msg):
        root.destroy()      
b1=Button(root,text="PROCEED",bd=30,bg="dark slate grey",fg="white",command=check_null)
b1.pack()
b2=Button(root,text="EXIT",bd=10,bg="red",command=cancel)
b2.pack(side='bottom')
root.mainloop()
