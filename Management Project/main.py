from tkinter import *
from PIL import ImageTk,Image
import Database as db
from tkinter import messagebox
import pandas as pd
from abc_analysis import abc_analysis
import numpy as np
from tkinter import ttk
import matplotlib.pyplot as plt
import minimal_login as ml
from math import *

# Database Function -------------------------------------------------------------------------------
def bd_AddProduct():
    """
    ADD a new Product to Database from this function, we demande to the user to input:
    Product Name, Product Id, Request for a year, Unite Price and Stock inital, and we put this
    in the database.
    """
    global error
    IDsProduct = str(db.IdProduct())
    ProNames = str(db.ProductNames())

    if Id_Label.get() == '' or Name_Label.get() == '' or  request_Label.get() == '' or  price_Label.get() == '' or  stock_Label.get() == '':
        error = Label(bg_Frame2,text="Please input your informations!",fg='red',bg='white',border=0,font=13)
        error.place(x=560,y=485)
    elif Id_Label.get() in IDsProduct:
        error = Label(bg_Frame2, text="Your input 'Id' is aleady used in our databse, Please input a new one!!", fg='red', bg='white', border=0, font=13)
        error.place(x=510, y=485)
    elif Name_Label.get() in ProNames:
        error = Label(bg_Frame2, text="Your input 'Product Name' is aleady used in our databse, Please input a new one!!",
                      fg='red', bg='white', border=0, font=13).place(x=510, y=485)
    else:
        error.place_forget()
        db.Add_Product(Id_Label.get(),Name_Label.get(),request_Label.get(),price_Label.get(),stock_Label.get(),'.')
        messagebox.showinfo("Successful", "     successfully added your product to the databse, you can sheck it!")

def db_ShowProduct():
    """
    we use this function to Show product information from database using input Id Product from the user.
    """
    # Detected product function --------------------------------
    IDsProduct = str(db.IdProduct())
    global error

    if ID_Entry.get() == '':
        error = Label(Bg_Frame, text="Please input your product id!",fg='red', bg='white', border=0, font=13)
        error.place(x=565, y=230)
    elif ID_Entry.get() not in IDsProduct:
        error = Label(Bg_Frame, text="Your product id is not in our database!, Please retry!", bg='white',fg='red', border=0, font=13)
        error.place(x=565, y=230)
    else:
        PI = db.ShowProductInfo(ID_Entry.get())
        text = ''
        for pi in PI:
            text += str(pi) + '\n\n'
        Show = Label(Bg_Frame, text=text, bg='white',font=13, border=0).place(x=700,y=380)
        L = ["IdProduit", "NomeProduit",'demande_annuelle',"prix_unitair","stock_valeur"]
        text2 = ''
        for l in L :
            text2 += l + '\n\n'
        Show2 = Label(Bg_Frame, text=text2, bg='white',font=13, border=0).place(x=550,y=380)
        error.place_forget()




##### Functions-----------------------------------------------------------------------------
def ShowProdInfo():
    """
    A fram Contains : Image and two buttons, showing and adding a product
    """
    bg_Frame2 = Frame(root, width=1000, height=650, bg='white')
    bg_Frame2.place(x=0, y=0)

    global SecondImage
    SecondImage = ImageTk.PhotoImage(Image.open("Product Image.png"))
    Label(bg_Frame2, image=SecondImage, border=0, bg='white').place(x=100, y=155)

    # Label -------------------------------
    fLabel = Label(bg_Frame2,text=('Product Info'),fg='#F25CAF',bg='white',font=('Microsoft YaHei UI Light',45,'bold'))
    fLabel.place(x=325,y=10)
    SLabel = Label(bg_Frame2,text=('Here you can see your product information, and also add a new one.'),fg='#F25CAF',bg='white',font=('Microsoft YaHei UI Light',12,'bold'))
    SLabel.place(x=220,y=90)

    # Buttons --------------------------
    InfoPbutton = Button(bg_Frame2,text='Product Info',width=39,height=2,pady=7,bg='#F25CAF',fg='white',border=0,command=ShowInfoProducts).place(x=630,y=240)
    AddPbutton = Button(bg_Frame2,text='Add Product',width=39,height=2,pady=7,bg='#F25CAF',fg='white',border=0,command=AddProduct).place(x=630,y=310)
    Exitbutton = Button(bg_Frame2,text='BACK',width=20,height=2,pady=7,bg='#F25CAF',fg='white',border=0,command=bg_Frame2.place_forget)
    Exitbutton.place(x=695,y=380)

def ShowInfoProducts():
    """
    This function show a product information from database using input id.
    """
    global ID_Entry, Bg_Frame
    Bg_Frame = Frame(root,width=1000, height=650, bg='white')
    Bg_Frame.place(x=0, y=0)

    # Label -------------------------------
    fLabel = Label(Bg_Frame,text=('Product Info'),fg='#F25CAF',bg='white',font=('Microsoft YaHei UI Light',45,'bold'))
    fLabel.place(x=325,y=10)
    SLabel = Label(Bg_Frame,text=('Here you can see your product information, and also add a new one.'),fg='#F25CAF',bg='white',font=('Microsoft YaHei UI Light',12,'bold'))
    SLabel.place(x=220,y=90)

    global SecondImage2
    SecondImage2 = ImageTk.PhotoImage(Image.open("Product Image.png"))
    Label(Bg_Frame, image=SecondImage2, border=0, bg='white').place(x=100, y=155)

    ID_Label = Label(Bg_Frame,text='ID Product: ',bg='white', font=('Consolas', 13)).place(x=560,y=190)
    ID_Entry = Entry(Bg_Frame, width=20, border=0, font=('Consolas', 13))
    ID_Entry.place(x=700,y=190)
    Frame(Bg_Frame, width=180, height=2, bg='#141414').place(x=700,y=210)


    # Buttons-------------------------
    ValidatB = Button(Bg_Frame,text='Validation',width=33,pady=7,bg='#F25CAF',fg='white',border=0,command=db_ShowProduct).place(x=610,y=270)
    Exitbutton = Button(Bg_Frame, text='BACK', width=20, pady=7, bg='#F25CAF', fg='white', border=0,
                        command=Bg_Frame.place_forget)
    Exitbutton.place(x=655, y=320)



def AddProduct():
    global bg_Frame2
    bg_Frame2 = Frame(root, width=1000, height=650, bg='white')
    bg_Frame2.place(x=0, y=0)

    # Label -------------------------------
    fLabel = Label(bg_Frame2,text=('Product Info'),fg='#F25CAF',bg='white',font=('Microsoft YaHei UI Light',45,'bold'))
    fLabel.place(x=325,y=10)
    SLabel = Label(bg_Frame2,text=('Here you can see your product information, and also add a new one.'),fg='#F25CAF',bg='white',font=('Microsoft YaHei UI Light',12,'bold'))
    SLabel.place(x=220,y=90)

    global SecondImage3
    SecondImage3 = ImageTk.PhotoImage(Image.open("Product Image.png"))
    Label(bg_Frame2, image=SecondImage3, border=0, bg='white').place(x=100, y=155)

    # Labesls ---------------------------------------------------
    Id_label = Label(bg_Frame2,text="Id Product: ",bg='white', font=('Consolas', 13) ).place(x=560,y=175)
    Name_label = Label(bg_Frame2, text="Product Name: ", bg='white', font=('Consolas', 13)).place(x=560,y=240)
    request_label = Label(bg_Frame2, text="Annual Request: ", bg='white', font=('Consolas', 13)).place(x=560,y=305)
    price_label = Label(bg_Frame2, text="Unit Price: ", bg='white', font=('Consolas', 13)).place(x=560,y=370)
    stock_label = Label(bg_Frame2, text="Stock Value: ", bg='white', font=('Consolas', 13)).place(x=560,y=435)

    # Enrtys --------------------------------------------------
    global Id_Label, Name_Label, request_Label, price_Label, stock_Label
    Id_Label = Entry(bg_Frame2, width=20, border=0, font=('Consolas', 13))
    Name_Label = Entry(bg_Frame2, width=20, border=0, font=('Consolas', 13))
    request_Label = Entry(bg_Frame2, width=20, border=0, font=('Consolas', 13))
    price_Label = Entry(bg_Frame2, width=20, border=0, font=('Consolas', 13))
    stock_Label = Entry(bg_Frame2, width=20, border=0, font=('Consolas', 13))

    Id_Label.place(x=720,y=175)
    Name_Label.place(x=720, y=240)
    request_Label.place(x=720, y=305)
    price_Label.place(x=720, y=370)
    stock_Label.place(x=720, y=435)

    # Frames for Labels -------------------------------
    Frame(bg_Frame2, width=180, height=2, bg='#141414').place(x=720, y=195)
    Frame(bg_Frame2, width=180, height=2, bg='#141414').place(x=720, y=260)
    Frame(bg_Frame2, width=180, height=2, bg='#141414').place(x=720, y=325)
    Frame(bg_Frame2, width=180, height=2, bg='#141414').place(x=720, y=390)
    Frame(bg_Frame2, width=180, height=2, bg='#141414').place(x=720, y=455)

    # Buttons ---------------------------------------------------
    Validat_button = Button(bg_Frame2,text='Validation',width=30,pady=7,bg='#F25CAF',fg='white',border=0,command=bd_AddProduct).place(x=675,y=530)
    Exitbutton = Button(bg_Frame2, text='BACK', width=20, pady=7, bg='#F25CAF', fg='white', border=0,
                        command=bg_Frame2.place_forget)
    Exitbutton.place(x=713, y=580)

def ABC_Classification():
    global  df
    bg_Frame2 = Frame(root, width=1000, height=650, bg='white')
    bg_Frame2.place(x=0, y=0)

    # Label ------------------------------
    fLabel = Label(bg_Frame2, text=('ABC Classification'), fg='#F38704', bg='white',
                   font=('Microsoft YaHei UI Light', 45, 'bold'))
    fLabel.place(x=280, y=10)
    SLabel = Label(bg_Frame2, text=('Here you can see the ABC classification and his diagrame.'), fg='#F38704',
                   bg='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
    SLabel.place(x=280, y=90)

    global ABCImage
    ABCImage = ImageTk.PhotoImage(Image.open("ABC Frame Image.png"))
    Label(bg_Frame2, image=ABCImage, border=0, bg='white').place(x=100, y=180)

    df = pd.read_csv('DATABASE.csv',usecols=['NomeProduit','demande_annuelle'], sep=';')


    # ABC Buttons --------------------------------
    global ABC_D
    DiagramButton = Button(bg_Frame2,text='ABC Diagram',width=30,height=2,pady=7,bg='#F38704',fg='white',border=0,command=ABC_D)
    DiagramButton.place(x=630,y=240)
    ClassificationButton = Button(bg_Frame2,text='ABC Classifaction',height=2,width=30,pady=7,bg='#F38704',fg='white',border=0,command=ABCclass)
    ClassificationButton.place(x=630,y=310)
    Exitbutton = Button(bg_Frame2, text='BACK', width=20, pady=7,height=2, bg='#F38704', fg='white', border=0,
                        command=bg_Frame2.place_forget)
    Exitbutton.place(x=666, y=380)

def ABCclass():
    """
    This is the important ABC Classification function, because here we do the calculat work, we use the old databsa and
    we make our classification based on raquest of a year, and show the result in a Label, we use in this function
    ABC analysist package.
    """
    bg_Frame2 = Frame(root, width=1000, height=650, bg='white')
    bg_Frame2.place(x=0, y=0)
    abc = abc_analysis(df['demande_annuelle'])

    a_index = abc['Aind']
    b_index = abc['Bind']
    c_index = abc['Cind']

        # New Column indicating A, B, or C
    cond_list = [df.index.isin(a_index),
                df.index.isin(b_index),
                df.index.isin(c_index)]

    choice_list = ['A', 'B', 'C']

    df['abc'] = np.select(cond_list, choice_list)
    ABC_Variable = df.sort_values(by=['demande_annuelle'], ascending=False)

    ShowLable = Label(bg_Frame2,text= ABC_Variable,bg='white',font=('Licorice',11))
    ShowLable.place(x=210, y=40)
    Exitbutton = Button(bg_Frame2, text='BACK', width=20, pady=7, bg='#F38704', fg='white', border=0,
                        command=bg_Frame2.place_forget)
    Exitbutton.place(x=400, y=570)


def ABC_D():
    abc_analysis(df['demande_annuelle'],True)   # This function is for drawing ABC Diagrame using Matplotlipe


def BPMN():
    New_Frame = Frame(root, width=1000, height=650, bg='white')
    New_Frame.place(x=0, y=0)

    global BPMNImage
    BPMNImage = ImageTk.PhotoImage(Image.open("BPMN Frame Image.png"))
    Label(New_Frame, image=BPMNImage, border=0, bg='white').place(x=65, y=150)

    # Label -------------------------------
    fLabel = Label(New_Frame, text=('Busines Process Management and Notation'), fg='#360259', bg='white',
                   font=('Microsoft YaHei UI Light', 29, 'bold'))
    fLabel.place(x=100, y=30)
    SLabel = Label(New_Frame, text=('Here you can see the BPMN Scenario and diagrame.'), fg='#360259',
                   bg='white', font=('Microsoft YaHei UI Light', 13))
    SLabel.place(x=300, y=85)

    # Buttons -------------------------------
    BPMN1 = Button(New_Frame,text='BPMN Diagram',width=35,height=2,pady=7,bg='#360259',fg='white',border=0,command=BPMNShow)
    BPMN1.place(x=650,y=250)
    BPMN2 = Button(New_Frame,text='BPMN Scenario',width=35,height=2,pady=7,bg='#360259',fg='white',border=0,command=BPMNs1)
    BPMN2.place(x=650,y=320)
    Exitbutton = Button(New_Frame, text='BACK', width=20, pady=7, height=2, bg='#360259', fg='white', border=0,
                        command=New_Frame.place_forget)
    Exitbutton.place(x=706, y=390)

def BPMNShow():
    """
    here you can see the BPMN of our campany.
    """
    Show = Toplevel()
    Show.title("BPMN Diagram")
    Show.geometry("10000x100000")

    global BPMN_photo
    BPMN_photo = ImageTk.PhotoImage(Image.open("BPMN Diagram.png"))
    Label(Show, image=BPMN_photo,border=0,bg='white').place(x=0,y=0)

def BPMNs1():
    """
    Two function for discraibing our BPMN Scenario.
    """
    global New_Frame2, ScenarioLabel, BPMN2_Button
    New_Frame2 = Frame(root, width=1000, height=650, bg='white')
    New_Frame2.place(x=0, y=0)

    global BPMNImage1
    BPMNImage1 = ImageTk.PhotoImage(Image.open("BPMN Frame Image.png"))
    Label(New_Frame2, image=BPMNImage1, border=0, bg='white').place(x=60, y=150)

    # Label -------------------------------
    fLabel = Label(New_Frame2, text=('Busines Process Management and Notation'), fg='#360259', bg='white',
                   font=('Microsoft YaHei UI Light', 29, 'bold'))
    fLabel.place(x=100, y=30)
    SLabel = Label(New_Frame2, text=('Here you can see the BPMN Scenario and diagrame.'), fg='#360259',
                   bg='white', font=('Microsoft YaHei UI Light', 13))
    SLabel.place(x=300, y=85)

    # Scenario ------------------------------
    ScenarioLabel = Label(New_Frame2, text=("BMS's manufacturing operations begin after\nchecking the company's stock of"
                                           " raw materials\n and the arrival of the final material request\nfrom the customer,"
                                           " where this information is\nexploited, in addition to evaluating the supplier"
                                           "\nto choose the best among them and determine\nwhether the stock needs to be"
                                           " ordered from\n the supplier or not. If yes, it is sent and the\ncompany requests"
                                           " raw material to the supplier\n in the desired quantity and quality, then the "
                                           "\nsupplier either sends the raw material within \nthe specified deadline ")
                                           ,bg='white', font=('Microsoft YaHei UI Light', 15))
    ScenarioLabel.place(x=520, y=175)

    # Buttons -----------------------------
    BPMN2_Button = Button(New_Frame2, text='NEXT', width=20, pady=7, height=2, bg='#360259', fg='white', border=0,
                        command=BPMNs2)
    BPMN2_Button.place(x=790,y=530)
    Exitbutton = Button(New_Frame2, text='BACK', width=20, pady=7, height=2, bg='#360259', fg='white', border=0,
                        command=New_Frame2.place_forget)
    Exitbutton.place(x=520, y=530)

def BPMNs2():
    ScenarioLabel.place_forget()
    BPMN2_Button.place_forget()
    # Scenario ------------------------------
    ScenarioLabel1 = Label(New_Frame2, text="(within 5 days) or sends a protest to it and waits\n for it until another 5"
                                           "days have passed and gives\nit a bad rating in the feedback box To be taken,\n"
                                           "and the latter is taken into account when choosing\nthe supplier in the next "
                                           "application, then the raw\nmaterial enters the warehouse and then enters\nthe "
                                           "manufacturing stage. If the answer is no, the\nprocess goes directly to the "
                                           "manufacturing\nstage and from it produces the final material\nand in the end "
                                           "the company carries out a\ntransfer process The product is delivered to the\n"
                                           "buyer and the process is completed. "
                          , bg='white', font=('Microsoft YaHei UI Light', 15))
    ScenarioLabel1.place(x=500, y=175)

    # Buttons -----------------------------
    Exitbutton = Button(New_Frame2, text='BACK', width=20, pady=7, height=2, bg='#360259', fg='white', border=0,
                        command=New_Frame2.place_forget)
    Exitbutton.place(x=520, y=530)

def Methods():
    New_Frame = Frame(root, width=1000, height=650, bg='white')
    New_Frame.place(x=0, y=0)

    global MImage
    MImage = ImageTk.PhotoImage(Image.open("Methods Frame Image.png"))
    Label(New_Frame, image=MImage, border=0, bg='white').place(x=75, y=160)

    # Lables ----------------------------
    fLabel = Label(New_Frame, text=('Methods of supply and stock management'), fg='#635EF2', bg='white',
                   font=('Microsoft YaHei UI Light', 29, 'bold'))
    fLabel.place(x=100, y=30)
    SLabel = Label(New_Frame, text=('Here you can see methods of supply and stock management.'), fg='#635EF2',
                   bg='white', font=('Microsoft YaHei UI Light', 13))
    SLabel.place(x=275, y=85)

    # Buttons ------------------------------
    M1 = Button(New_Frame, text='Class A method', width=30, height=2, pady=7, bg='#635EF2', fg='white', border=0,
                   command=ClassA1)
    M1.place(x=650, y=240)
    M2 = Button(New_Frame, text='Class B method', width=30, height=2, pady=7, bg='#635EF2', fg='white', border=0,
                command=ClassB)
    M2.place(x=650, y=310)
    M3 = Button(New_Frame, text='Class C method', width=30, height=2, pady=7, bg='#635EF2', fg='white', border=0,
                command=ClassC)
    M3.place(x=650,y=380)
    PrevisionButton = Button(New_Frame, text='Prevision Methods', width=27, height=2, pady=7, bg='#635EF2', fg='white', border=0,
                command=P_Quantitave1)
    PrevisionButton.place(x=780,y=550)
    SS_Button = Button(New_Frame, text='Security Stock Calculat', width=28, height=2, pady=7, bg='#635EF2', fg='white', border=0,
                command=CalculSS)
    SS_Button.place(x=530,y=550)
    Exitbutton = Button(New_Frame, text='BACK', width=20, pady=7, height=2, bg='#635EF2', fg='white', border=0,
                        command=New_Frame.place_forget)
    Exitbutton.place(x=686, y=450)

def ClassA1():
    global D_entry
    messagebox.showinfo("Notification","Make sure that you input a correct database!")
    New_Frame = Frame(root, width=1000, height=650, bg='white')
    New_Frame.place(x=0, y=0)

    global MImage1
    MImage1 = ImageTk.PhotoImage(Image.open("Methods Frame Image.png"))
    Label(New_Frame, image=MImage1, border=0, bg='white').place(x=75, y=160)

    # Lables ----------------------------
    fLabel = Label(New_Frame, text=('Methods of supply and stock management'), fg='#635EF2', bg='white',
                   font=('Microsoft YaHei UI Light', 29, 'bold'))
    fLabel.place(x=100, y=30)
    SLabel = Label(New_Frame, text=('Here you can see methods of supply and stock management.'), fg='#635EF2',
                   bg='white', font=('Microsoft YaHei UI Light', 13))
    SLabel.place(x=275, y=85)

    # Entry label ---------------------------
    D_Label = Label(New_Frame, text=('Enter your prevision consomation for a year:'), fg='#6C63FF',
                      bg='white', font=('Microsoft YaHei UI Light', 13, 'bold'))
    D_Label1 = Label(New_Frame, text=('(You can use prevision part of this application!)'), fg='#6C63FF',
                    bg='white', font=('Microsoft YaHei UI Light', 13, 'bold'))
    D_Label.place(x=550,y=230)
    D_Label1.place(x=530,y=260)

    # Entry's ----------------------------
    D_entry = Entry(New_Frame, width=20, border=0, font=('Microsoft YaHei UI Light', 13))
    D_entry.place(x=650,y=315)
    Frame(New_Frame, width=180, height=2, bg='#141414').place(x=650, y=337)

    # Button's -------------------------------
    CalculB = Button(New_Frame, text='Calculate', width=25, pady=7, bg='#635EF2', fg='white', border=0
                     ,command=TestValus)
    CalculB.place(x=650, y=370)
    Exitbutton = Button(New_Frame, text='BACK', width=20, pady=7, bg='#635EF2', fg='white', border=0,
                        command=New_Frame.place_forget)
    Exitbutton.place(x=670, y=420)

def TestValus():
    try:
        I = int(float(D_entry.get()))
        ClassA()
    except:
        messagebox.showinfo('ERROR', 'You should input a numbre!!')

def ClassA():
    '''
    Method 'Point Comande' programing.
    :return: Table with period and command values.
    '''
    global a
    New_Frame = Frame(root, width=1000, height=650, bg='white')
    New_Frame.place(x=0, y=0)

    # Lables ----------------------------
    fLabel = Label(New_Frame, text=('Methods of supply and stock management'), fg='#635EF2', bg='white',
                   font=('Microsoft YaHei UI Light', 29, 'bold'))
    fLabel.place(x=100, y=30)
    SLabel = Label(New_Frame, text=('Here you can see methods of supply and stock management.'), fg='#635EF2',
                   bg='white', font=('Microsoft YaHei UI Light', 13))
    SLabel.place(x=275, y=85)

    # Table --------------------------------------------------
    table1 = ttk.Treeview(New_Frame, height=18)
    table1.place(x=200, y=120)
    table1['column'] = ('Date', 'Output', 'Available stock', 'Command')
    table1.column('#0', width=0)
    table1.column('Date', width=150)
    table1.column('Output', width=150)
    table1.column('Available stock', width=150)
    table1.column('Command', width=150)

    table1.heading('Date', text='Date')
    table1.heading('Output', text='Output')
    table1.heading('Available stock', text='Available stock')
    table1.heading('Command', text='Command')

    # Insert into the table -------------------------
    OutputA = db.OutputA()

    I = int(float(D_entry.get()))
    D = (I/48)
    a = [2000]
    for i in range(0,len(OutputA)):
        for j in OutputA[i]:
            if a[i]>D:
                b = a[i] - j
                a.append(b)
            elif a[i]<=D:
                b = 2000 - j
                a.append(b)
    db.AvailableA(a)
    db.UPDATE_CommandA(D)
    ClassA_items = db.ClassA()

    for i in ClassA_items:
        table1.insert('', 'end', values=i)

    PCommand = Label(New_Frame,text=f'Command Point is {D} Command/Week')
    PCommand.place(x=200,y=530)
    # button -----------------------------
    DiagramButton = Button(New_Frame, text='Diagram', width=20, pady=7, bg='#635EF2', fg='white', border=0,
                        command=ClassA_Diagram)
    DiagramButton.place(x=555,y=570)
    Exitbutton = Button(New_Frame, text='BACK', width=20, pady=7, bg='#635EF2', fg='white', border=0,
                        command=New_Frame.place_forget)
    Exitbutton.place(x=300, y=570)

def ClassA_Diagram():
    plt.style.use('ggplot')
    Y = a.pop()
    y= a
    x=["01","02","03","04","05","06","07","08","09","10","11","12"
       ,"13","14","15","16","17","18"]

    plt.plot(x,y)
    plt.xlabel('Période')
    plt.ylabel('Available stock')
    plt.show()

def ClassB():
    '''
    Method 'Recompletement periodique' programming.
    :return: Table with period and command values.
    '''
    global b
    messagebox.showinfo("Notification", "Make sure that you input a correct database!")
    New_Frame = Frame(root, width=1000, height=650, bg='white')
    New_Frame.place(x=0, y=0)

    # Lables ----------------------------
    fLabel = Label(New_Frame, text=('Methods of supply and stock management'), fg='#635EF2', bg='white',
                   font=('Microsoft YaHei UI Light', 29, 'bold'))
    fLabel.place(x=100, y=30)
    SLabel = Label(New_Frame, text=('Here you can see methods of supply and stock management.'), fg='#635EF2',
                   bg='white', font=('Microsoft YaHei UI Light', 13))
    SLabel.place(x=275, y=85)

    # Table --------------------------------------------------
    table1 = ttk.Treeview(New_Frame, height=20)
    table1.place(x=70, y=120)
    table1['column'] = ('Date', 'Output', 'Available stock', 'Command', 'Available stock + Command')
    table1.column('#0', width=0)
    table1.column('Date', width=150)
    table1.column('Output', width=150)
    table1.column('Available stock', width=150)
    table1.column('Command', width=150)
    table1.column('Available stock + Command', width=250)

    table1.heading('Date', text='Date')
    table1.heading('Output', text='Output')
    table1.heading('Available stock', text='Available stock')
    table1.heading('Command', text='Command')
    table1.heading('Available stock + Command', text='Available stock + Command')

    # Insert into the table -------------------------
    Output_B = db.OutputB()

    b = [600]
    for i in range(0,len(Output_B)):
        for j in Output_B[i]:
            if i == 9 or i == 16:
                c = b[i] - j + (600-b[i-2])
                b.append(c)
                db.UPDATE_CommandB(b[i-2],i-2)
            else:
                c = b[i] - j
                b.append(c)
    db.AvailableB(b)

    db.LessUPDATE(b)
    ClassB_items = db.ClassB()

    for i in ClassB_items:
        table1.insert('', 'end', values=i)

    # button -----------------------------
    DiagramButton = Button(New_Frame, text='Diagram', width=20, pady=7, bg='#635EF2', fg='white', border=0,
                           command=ClassB_Diagram)
    DiagramButton.place(x=600, y=570)
    Exitbutton = Button(New_Frame, text='BACK', width=20, pady=7, bg='#635EF2', fg='white', border=0,
                        command=New_Frame.place_forget)
    Exitbutton.place(x=270, y=570)

def ClassB_Diagram():
    plt.style.use('ggplot')

    Y = b.pop()

    y = b
    x=["01","02","03","04","05","06","07","08","09","10","11","12"
       ,"13","14","15","16","17","18"]

    plt.plot(x,y)
    plt.xlabel('Période')
    plt.ylabel('Available stock')
    plt.show()

def ClassC():
    '''
    Methode 'Min-Max' programming.
    :return: Table with period and command values.
    '''
    global c
    messagebox.showinfo("Notification", "Make sure that you input a correct database!")
    New_Frame = Frame(root, width=1000, height=650, bg='white')
    New_Frame.place(x=0, y=0)

    # Lables ----------------------------
    fLabel = Label(New_Frame, text=('Methods of supply and stock management'), fg='#635EF2', bg='white',
                   font=('Microsoft YaHei UI Light', 29, 'bold'))
    fLabel.place(x=100, y=30)
    SLabel = Label(New_Frame, text=('Here you can see methods of supply and stock management.'), fg='#635EF2',
                   bg='white', font=('Microsoft YaHei UI Light', 13))
    SLabel.place(x=275, y=85)

    # Table --------------------------------------------------
    table1 = ttk.Treeview(New_Frame, height=20)
    table1.place(x=70, y=120)
    table1['column'] = ('Date', 'Output', 'Available stock', 'Command', 'Available stock + Command')
    table1.column('#0', width=0)
    table1.column('Date', width=150)
    table1.column('Output', width=150)
    table1.column('Available stock', width=150)
    table1.column('Command', width=150)
    table1.column("Available stock + Command", width=250)

    table1.heading('Date', text='Date')
    table1.heading('Output', text='Output')
    table1.heading('Available stock', text='Available stock')
    table1.heading('Command', text='Command')
    table1.heading('Available stock + Command', text='Available stock + Command')

    # Insert into the table -------------------------
    OutputC = db.OutputC()

    c = [600]
    for i in range(0, len(OutputC)):
        for j in OutputC[i]:
            if c[i] > 300:
                b = c[i] - j
                c.append(b)
            elif c[i] <= 300:
                b = 600 - j
                c.append(b)
                db.UPDATE_CommandC(i+1)
    db.AvailableC(c)
    db.LessUPDATE2(c)

    ClassC_items = db.ClassC()
    for i in ClassC_items:
        table1.insert('', 'end', values=i)

    # button -----------------------------
    DiagramButton = Button(New_Frame, text='Diagram', width=20, pady=7, bg='#635EF2', fg='white', border=0,
                           command=ClassC_Diagram)
    DiagramButton.place(x=600, y=570)
    Exitbutton = Button(New_Frame, text='BACK', width=20, pady=7, bg='#635EF2', fg='white', border=0,
                        command=New_Frame.place_forget)
    Exitbutton.place(x=270, y=570)

def ClassC_Diagram():
    plt.style.use('ggplot')

    Y = db.MulC()
    y = []
    for i in Y:
        y.append(i[0])
    x=["01","02","03","04","05","06","07","08","09","10","11","12"
       ,"13","14","15","16","17","18"]

    plt.plot(x,y)
    plt.xlabel('Période')
    plt.ylabel('Available stock')
    plt.show()


def P_Quantitave1():
    global NPrevision_Calcul
    bg_Frame = Frame(root, width=1000, height=650, bg='white')
    bg_Frame.place(x=0, y=0)

    global PrevisionImage1
    PrevisionImage1 = ImageTk.PhotoImage(Image.open("Prevision Frame Image.png"))
    Label(bg_Frame, image=PrevisionImage1, border=0, bg='white').place(x=75, y=150)

    # Lables ----------------------------
    fLabel = Label(bg_Frame, text=('Prevision For Your Products'), fg='#6C63FF', bg='white',
                   font=('Microsoft YaHei UI Light', 29, 'bold'))
    fLabel.place(x=250, y=30)
    SLabel = Label(bg_Frame, text=('Here you can see prevision for your products.'), fg='#6C63FF',
                   bg='white', font=('Microsoft YaHei UI Light', 13))
    SLabel.place(x=330, y=85)

    # Labels -------------------------------
    def on_enter(e):
        NPrevision_Calcul.delete(0,'end')
    def on_leave(e):
        if NPrevision_Calcul.get()=='':
            NPrevision_Calcul.insert(0,'Maximum 24')

    NPC_lable = Label(bg_Frame, text=('Enter the number of months you are looking to consider:'), fg='#6C63FF',
                      bg='white', font=('Microsoft YaHei UI Light', 13, 'bold'))
    NPC_lable.place(x=500, y=240)

    # the numbre who wanted by the user --------------------------
    NPrevision_Calcul = Entry(bg_Frame, width=20, border=0, font=('Microsoft YaHei UI Light', 13))
    NPrevision_Calcul.place(x=650, y=300)
    NPC_Frame = Frame(bg_Frame, width=180, height=2, bg='#141414').place(x=650, y=322)
    NPrevision_Calcul.bind("<FocusIn>", on_enter)
    NPrevision_Calcul.bind("<FocusOut>", on_leave)
    NPrevision_Calcul.insert(0, 'Maximum 24')

    # Push Button ---------------------------
    CalculB = Button(bg_Frame, text='Calculate', width=25, pady=7, bg='#635EF2', fg='white', border=0,
                     command=ControlValues)
    CalculB.place(x=650, y=350)
    Exitbutton = Button(bg_Frame, text='BACK', width=20, pady=7, bg='#635EF2', fg='white', border=0,
                        command=bg_Frame.place_forget)
    Exitbutton.place(x=670, y=400)

def ControlValues():
    try:
        Nbr = int(float(NPrevision_Calcul.get()))
        P_Quantitave()
    except:
        messagebox.showinfo('ERROR', 'You should input a correct numbre!!')

def P_Quantitave():
    '''
    Methode 'Moyenne mobile avec tendance'.
    :return: y^ prevision.
    '''
    global b0, b1, b2, b3, a1, w, Y, t, y
    New_Frame = Frame(root, width=1000, height=650, bg='white')
    New_Frame.place(x=0, y=0)

    # Lables ----------------------------
    fLabel = Label(New_Frame, text=('Prevision For Your Products'), fg='#6C63FF', bg='white',
                   font=('Microsoft YaHei UI Light', 29, 'bold'))
    fLabel.place(x=250, y=30)
    SLabel = Label(New_Frame, text=('Here you can see prevision for your products.'), fg='#6C63FF',
                   bg='white', font=('Microsoft YaHei UI Light', 13))
    SLabel.place(x=330, y=85)

    # Calcule b^ ---------------------------
    t = db.tP()
    y = db.Demande()
    n = len(t)

    b0 = 0
    a1 = 0
    for i in range(0, len(t)):
        for j in t[i]:
            for z in y[i]:
                b0 = j * z
                a1 = a1 + b0


    b1 = 0
    for i in range(len(y)):
        for j in y[i]:
            b1 += j
    a2 = ((n + 1) / 2) * b1

    b2 = 0
    for i in range(len(t)):
        for j in t[i]:
            b2 = b2 + j ** 2

    b3 = 0
    for i in range(len(t)):
        for j in t[i]:
            b3 += j
    a3 = (b3 ** 2) / n


    B = (a1 - a2) / (b2 - a3)

    # CALCULE S -----------------------------------------------------
    S = (y[-1][0] + y[-2][0] + y[-3][0]) / 3

    # Calcule y^ --------------------------------
    Y = []
    Nbr = int(float(NPrevision_Calcul.get()))
    for i in range(1, Nbr+1):
        u = S + (1 + i) * B
        Y.append(u)
        db.DPrevision(Y)
    w = []
    for i in range(1,Nbr+1):
        w.append(i)

    # Tableau ----------------------------
    table = ttk.Treeview(New_Frame, height=20)
    table.place(x=150, y=120)
    table['column'] = ('Mois', 'Années', 't', 'Prevision')
    table.column('#0', width=0)
    table.column('Mois', width=150)
    table.column('Années', width=150)
    table.column('t', width=150)
    table.column("Prevision", width=250)

    table.heading('Mois', text='Mois')
    table.heading('Années', text='Années')
    table.heading('t', text='t')
    table.heading('Prevision', text='Prevision')

    # Insrtion ---------------------------
    Prevision_items = db.Prevision()
    for i in Prevision_items:
        table.insert('', 'end', values=i)

    # Buttons -------------------------------

    DiagramButton = Button(New_Frame, text='Diagram', width=20, pady=7, bg='#635EF2', fg='white', border=0
                           , command=P_Diagram)
    DiagramButton.place(x=600, y=570)
    Exitbutton = Button(New_Frame, text='BACK', width=20, pady=7, bg='#635EF2', fg='white', border=0,
                        command=New_Frame.place_forget)
    Exitbutton.place(x=270, y=570)

def P_Diagram():

    y1 = Y
    x = w

    plt.subplot(2, 1, 1)
    plt.plot(x, y1, 'o-')
    plt.title('Période')
    plt.ylabel('Prevision')

    plt.subplot(2, 1, 2)
    plt.plot(t, y, '.-')
    plt.xlabel('Période')
    plt.ylabel('Demande')

    plt.show()

def CalculSS():
    '''
    We use this function for calculing the Security Stock.
    :return: SS.
    '''
    global k_Calcul, DL_Calcul,New_Frame1
    New_Frame1 = Frame(root, width=1000, height=650, bg='white')
    New_Frame1.place(x=0, y=0)

    global MImage2
    MImage2 = ImageTk.PhotoImage(Image.open("Methods Frame Image.png"))
    Label(New_Frame1, image=MImage2, border=0, bg='white').place(x=75, y=160)

    # Lables ----------------------------
    fLabel = Label(New_Frame1, text=('Methods of supply and stock management'), fg='#635EF2', bg='white',
                   font=('Microsoft YaHei UI Light', 29, 'bold'))
    fLabel.place(x=100, y=30)
    SLabel = Label(New_Frame1, text=('Here you can see methods of supply and stock management.'), fg='#635EF2',
                   bg='white', font=('Microsoft YaHei UI Light', 13))
    SLabel.place(x=275, y=85)
    NPC_lable = Label(New_Frame1, text=("Enter the porsontage of le risque accepte par I'entreprise:"), fg='#6C63FF',
                      bg='white', font=('Microsoft YaHei UI Light', 13, 'bold'))
    NPC_lable.place(x=500, y=240)

    # the numbre who wanted by the user --------------------------
    k_Calcul = Entry(New_Frame1, width=20, border=0, font=('Microsoft YaHei UI Light', 13))
    k_Calcul.place(x=650, y=300)
    k_Frame = Frame(New_Frame1, width=180, height=2, bg='#141414').place(x=650, y=322)
    DL_Calcul = Entry(New_Frame1, width=20, border=0, font=('Microsoft YaHei UI Light', 13))
    DL_Calcul.place(x=650, y=350)
    DL_Frame = Frame(New_Frame1, width=180, height=2, bg='#141414').place(x=650, y=372)

    # Push Button ---------------------------
    Calculk = Button(New_Frame1, text='Calculate', width=25, pady=7, bg='#635EF2', fg='white', border=0,
                     command=ControlValues1)
    Calculk.place(x=650, y=400)
    Exitbutton = Button(New_Frame1, text='BACK', width=20, pady=7, bg='#635EF2', fg='white', border=0,
                        command=New_Frame1.place_forget)
    Exitbutton.place(x=670, y=450)

def AboutUs():
    '''
    A little fuction for representation the creators of this applications.
    '''
    New_Frame = Frame(root, width=1000, height=650, bg='white')
    New_Frame.place(x=0, y=0)

    # Images -------------------------------
    global SMImage, ABImage
    SMImage = ImageTk.PhotoImage(Image.open("SM.jpg"))
    Label(New_Frame, image=SMImage, border=0, bg='white').place(x=730, y=150)
    ABImage = ImageTk.PhotoImage(Image.open("ABD.jpg"))
    Label(New_Frame, image=ABImage, border=0, bg='white').place(x=730, y=380)

    # Labesl --------------------------------------------------
    FirstLabel = Label(New_Frame, text=('About Us '), fg='#33769C', bg='white',
                   font=('Microsoft YaHei UI Light', 55, 'bold'))
    FirstLabel.place(x=300, y=10)
    SecondLabel = Label(New_Frame, text=('Some information about application creators. '), fg='#33769C', bg='white',
                   font=('Microsoft YaHei UI Light', 13))
    SecondLabel.place(x=285, y=90)
    SMLabel = Label(New_Frame, text=('SAHRAOUI Mohamed-Amin a student in the national higher school of\ntechnology,speciality Industrial Engineering interested in programm'
                                     'ing,\ncomputer science, and Islamic science, have experience in Digital Marketing\nand UI/UX designing. We made this application to organize'
                                     ' and manage\nBMS company inventories of materials.'),
                   bg='white', font=('Microsoft YaHei UI Light', 14))
    SMLabel.place(x=60,y=170)
    ABLabel = Label(New_Frame,text=('MADJIDI ABDERRAOUF a student of the 2nd year in management and\nindustrial maintenance '
                                    'engineering  at Institute of Technology- Algiers.\nMy competences are: Bachelor of Science,which I took in 2017, '
                                    'CCNA 1\ncertificate from CISCO in Networking and OSI System,'
                                    'basics of\nprogramming in C, '
                                    'a certificate of success at higher schools contest.'),bg='white', font=('Microsoft YaHei UI Light', 14))
    ABLabel.place(x=60,y=380)

    # Button --------------------------------
    Exitbutton = Button(New_Frame, text='BACK', width=20, pady=7, bg='#33769C', fg='white', border=0,
                        command=New_Frame.place_forget)
    Exitbutton.place(x=400, y=570)

def ControlValues1():
    try :
        global SS_Label
        Poursantage_K = int(float(k_Calcul.get()))
        DL = int(float(DL_Calcul.get()))
        n = db.n()
        x = db.x()

        # Calcul -------------------------
        nT = 0
        for i in range(len(n)):
            for j in n[i]:
                nT += j


        x1 = 0
        for i in range(len(n)):
            for j in n[i]:
                for z in x[i]:
                    x1 = x1 + (z * j)

        xMoy = x1/nT


        x2 = 0
        for i in range(len(n)):
            for j in n[i]:
                for z in x[i]:
                    x2 += j * (z - xMoy)**2

        V = x2/nT

        G = sqrt(V)

        if Poursantage_K == 5:
            k = 1.65
        elif Poursantage_K == 2.5:
            k = 1.95
        elif Poursantage_K == 1:
            k = 2.35
        elif Poursantage_K == 0.5:
            k = 2.58
        elif Poursantage_K == 16:
            k = 1
        else:
            messagebox.showinfo('ERROR', 'You input incorrect k Poursontage!, Please retry!')

        SS = k * G * sqrt(DL)

        #SS_Label.place_forget()
        SS_Label = Label(New_Frame1, text=(f"Your Security Stock is: {SS}"),bg='white',
                         font=('Microsoft YaHei UI Light', 13, 'bold'))
        SS_Label.place(x=500,y=500)


    except:
        messagebox.showinfo('ERROR', 'You should input a correct numbre!!')


################# THE PRICIPALE WIDGET #######################
            ###############################
                   ##############

root = Tk()
root.title('UPGrade (Organize And Managment Application)')
root.geometry('1000x650')
root.resizable(0,0)

bg_Frame = Frame(root,width=1000,height=650,bg='white')
bg_Frame.place(x=0,y=0)

# Welcome Labels -----------------------------
WelcomLabel = Label(root,text=('Welcome '),fg='#0F0091',bg='white',font=('Microsoft YaHei UI Light',60,'bold'))
WelcomLabel.place(x=325,y=1)

WSecondLabel = Label(root,text=(f'welcom {ml.key} to UPGrade (Organize And Managment Application)'),fg='#0F0091',bg='white',font=('Microsoft YaHei UI Light',12))
WSecondLabel.place(x=260,y=95)


#First Image---------------------------
FirstImage = ImageTk.PhotoImage(Image.open("First Image.png"))
Label(bg_Frame,image=FirstImage,border=0,bg='white').place(x=90,y=145)

# Buttoms-----------------------------
ProductInfoB = Button(bg_Frame,text='Product Info',width=39,height=2,pady=7,bg='#0F0091',fg='white',border=0,command=ShowProdInfo).place(x=640,y=210)
ABC_button = Button(bg_Frame,text='ABC Classification',width=39,height=2,pady=7,bg='#0F0091',fg='white',border=0,command=ABC_Classification).place(x=640,y=280)
OtherMbutton = Button(bg_Frame,text='Stock Methods',width=39,height=2,pady=7,bg='#0F0091',fg='white',border=0,command=Methods).place(x=640,y=350)
BPMNbutton = Button(bg_Frame,text='BPMN',width=39,height=2,pady=7,bg='#0F0091',fg='white',border=0,command=BPMN).place(x=640,y=420)
AboutUsB = Button(bg_Frame,text='About Us',width=25,height=2,pady=7,bg='#0F0091',fg='white',border=0,command=AboutUs).place(x=790,y=580)
Exitbutton = Button(bg_Frame,text='EXIT',width=20,height=2,pady=7,bg='#0F0091',fg='white',border=0,command=exit)
Exitbutton.place(x=710,y=490)


root.mainloop()
