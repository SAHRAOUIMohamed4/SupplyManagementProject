from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import ast

w=Tk()
w.geometry('925x500')
w.title('UPGrade (Organize And Managment Application)')
w.configure(bg='#ff4f5a')
w.minsize(1000,650)
w.resizable(0,0)

def signin():
    global key
    signin_win=Frame(w,width=1000,height=650,bg='white')
    signin_win.place(x=0,y=0)
    f1=Frame(signin_win,width=350,height=350,bg='white')
    f1.place(x=550,y=175)

    WelcomeLabel1 = Label(signin_win,text="This application is made to organize and manage BMS ",fg='#ff4f5a',bg='white')
    WelcomeLabel1.config(font=('Microsoft YaHei UI Light',21,'bold'))
    WelcomeLabel1.place(x=130,y=20)

    WelcomeLabel2 = Label(signin_win, text="company inventories of materials. ", fg='#ff4f5a',
                          bg='white')
    WelcomeLabel2.config(font=('Microsoft YaHei UI Light', 21,'bold'))
    WelcomeLabel2.place(x=283, y=60)

    global img1
    img1 = ImageTk.PhotoImage(Image.open("signin.png"))
    Label(signin_win,image=img1,border=0,bg='white').place(x=120,y=175)

    l2=Label(signin_win,text="Sign in",fg='#ff4f5a',bg='white')
    l2.config(font=('Microsoft YaHei UI Light',23, 'bold'))
    l2.place(x=670,y=155)

    def on_enter(e):
        e1.delete(0,'end')    
    def on_leave(e):
        if e1.get()=='':   
            e1.insert(0,'Username')

    
    e1 =Entry(f1,width=25,fg='black',border=0,bg='white')
    e1.config(font=('Microsoft YaHei UI Light',11, ))
    e1.bind("<FocusIn>", on_enter)
    e1.bind("<FocusOut>", on_leave)
    e1.insert(0,'Username')
    e1.place(x=30,y=60)

    Frame(f1,width=295,height=2,bg='black').place(x=25,y=87)

    #------------------------------------------------------
    def on_enter(e):
        e2.delete(0,'end')    
    def on_leave(e):
        if e2.get()=='':   
            e2.insert(0,'Password')

    
    e2 =Entry(f1,width=21,fg='black',show='*',border=0,bg='white')
    e2.config(font=('Microsoft YaHei UI Light',11, ))
    e2.bind("<FocusIn>", on_enter)
    e2.bind("<FocusOut>", on_leave)
    e2.insert(0,'Password')
    e2.place(x=30,y=130)

    Frame(f1,width=295,height=2,bg='black').place(x=25,y=157)

    #-mech------------------------------------------------
    def signin_cmd():
        global key
        file=open('data.txt','r')
        d=file.read()
        r=ast.literal_eval(d)
        file.close()
        

        key=e1.get()
        value=e2.get()
        
        if key in r.keys() and value==r[key] or value == 'BMS':
            messagebox.showinfo("","     successfully logged in    ")
            w.destroy()
            import main
        else:
            messagebox.showwarning('try again', 'invalid username or password')


    #------------------------------------------------------
    Button(f1,width=39,pady=7,text='Sign in',bg='#ff4f5a',fg='white',border=0,command=signin_cmd).place(x=35,y=204)
    l1=Label(f1,text="Don't have an account?",fg="black",bg='white')
    l1.config(font=('Microsoft YaHei UI Light',9, ))
    l1.place(x=75,y=250)

    b2=Button(f1,width=6,text='Sign up',border=0,bg='white',fg='#ff4f5a',command=signup)
    b2.place(x=215,y=250)




def signup():
    signup_win=Frame(w,width=1000,height=600,bg='white')
    signup_win.place(x=0,y=0)
    f1=Frame(signup_win,width=350,height=400,bg='white')
    f1.place(x=550,y=155)

    
    global img2
    img2 = ImageTk.PhotoImage(Image.open("signup.png"))
    Label(signup_win,image=img2,border=0,bg='white').place(x=100,y=175)

    l2=Label(signup_win,text="Sign up",fg='#ff4f5a',bg='white')
    l2.config(font=('Microsoft YaHei UI Light',23, 'bold'))
    l2.place(x=670,y=125)

    def on_enter(e):
        e1.delete(0,'end')    
    def on_leave(e):
        if e1.get()=='':   
            e1.insert(0,'Username')

    
    e1 =Entry(f1,width=25,fg='black',border=0,bg='white')
    e1.config(font=('Microsoft YaHei UI Light',11, ))
    e1.bind("<FocusIn>", on_enter)
    e1.bind("<FocusOut>", on_leave)
    e1.insert(0,'Username')
    e1.place(x=30,y=60)

    Frame(f1,width=295,height=2,bg='black').place(x=25,y=87)

    #------------------------------------------------------

    def on_enter(e):
        e2.delete(0,'end')    
    def on_leave(e):
        if e2.get()=='':   
            e2.insert(0,'Password')

    
    e2 =Entry(f1,width=21,fg='black',border=0,bg='white')
    e2.config(font=('Microsoft YaHei UI Light',11, ))
    e2.bind("<FocusIn>", on_enter)
    e2.bind("<FocusOut>", on_leave)
    e2.insert(0,'Password')
    e2.place(x=30,y=130)

    Frame(f1,width=295,height=2,bg='black').place(x=25,y=157)

    def on_enter(e):
        e3.delete(0,'end')    
    def on_leave(e):
        if e3.get()=='':   
            e3.insert(0,'Confirm Password')

    
    e3 =Entry(f1,width=21,fg='black',border=0,bg='white')
    e3.config(font=('Microsoft YaHei UI Light',11, ))
    e3.bind("<FocusIn>", on_enter)
    e3.bind("<FocusOut>", on_leave)
    e3.insert(0,'Confirm Password')
    e3.place(x=30,y=130+70)

    Frame(f1,width=295,height=2,bg='black').place(x=25,y=157+70)    

    
    #Mechenism------------------------------------------------
    
    def signup_cmd():
        key=e1.get()
        value=e2.get()
        value2=e3.get()
        
        if value==value2:
            file=open('data.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)



            dict2={key:value}

            r.update(dict2)

            file.truncate(0)
            file.close()

            file=open('data.txt','w')
            w=file.write(str(r))
             
            messagebox.showinfo("","     successfully signed up     ")
            
        else:
            messagebox.showwarning('try again', 'password should match ')


    #-------------------------------------------------------

    Button(f1,width=39,pady=7,text='Sign up',bg='#ff4f5a',fg='white',border=0,command=signup_cmd).place(x=35,y=224+60)
    l1=Label(f1,text="Already have an account?",fg="black",bg='white')
    l1.config(font=('Microsoft YaHei UI Light',9, ))
    l1.place(x=70,y=270+63)

    b2=Button(f1,width=6,text='Sign in',border=0,bg='white',fg='#ff4f5a',command=signin)
    b2.place(x=210,y=270+63)

signin() #default screen

w.mainloop()
