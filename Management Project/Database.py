import sqlite3
import csv

connec = sqlite3.connect('database.db')
c = connec.cursor()

with connec:
    c.execute(""" CREATE TABLE IF NOT EXISTS [Produit]
            (idProduit TEXT,
            NomeProduit TEXT,
            demande_annuelle INTEGER,
            prix_unitair INTEGER,
            stock_valeur INTEGER,
            Class_type TEXT);
    """)
    c.execute(""" CREATE TABLE IF NOT EXISTS [ClassB]
               (Date TEXT,
               Output INTEGER,
               Available_stock INTEGER,
               Command INTEGER,
               Mul INTEGER,
               Jours INTEGER);
    """)
    c.execute(""" CREATE TABLE IF NOT EXISTS [ClassC]
                  (Date TEXT,
                  Output INTEGER,
                  Available_stock INTEGER,
                  Command INTEGER,
                  Mul INTEGER,
                  Jours INTEGER);
    """)
    c.execute(""" CREATE TABLE IF NOT EXISTS [ClassA]
                      (Date TEXT,
                      Output INTEGER,
                      Available_stock INTEGER,
                      Command INTEGER,
                      Jours INTEGER);
        """)
    c.execute(""" CREATE TABLE IF NOT EXISTS [Prevision]
                          (Mois TEXT,
                          t INTEGER,
                          Années INTEGER,
                          Demande INTEGER);
            """)
    c.execute(""" CREATE TABLE IF NOT EXISTS [PrevisionShow]
                              (Mois TEXT,
                              t INTEGER,
                              Années INTEGER,
                              Demande INTEGER);
                """)
    c.execute(""" CREATE TABLE IF NOT EXISTS [StockSecurite]
                                  (x INTEGER,
                                  n INTEGER);
                    """)

f=open("DATABASE.csv")
fichier=csv.reader(f)
l=[]
matrice=[]
for ligne in fichier:
    l=ligne[0].split(';')
    matrice.append(l)

g=open("ClassB.csv")
fille=csv.reader(g)
a=[]
matrice1=[]
for ligne in fille:
    a=ligne[0].split(';')
    matrice1.append(a)

d=open("ClassC.csv")
f=csv.reader(d)
b=[]
matrice2=[]
for ligne in f:
    b=ligne[0].split(';')
    matrice2.append(b)

E=open("ClassA.csv")
F=csv.reader(E)
D=[]
matrice3=[]
for ligne in F:
    D=ligne[0].split(';')
    matrice3.append(D)

a1 = open("PREVISION DB.csv")
A1 = csv.reader(a1)
b1 = []
matrice4 = []
for ligne in A1:
    b1 = ligne[0].split(';')
    matrice4.append(b1)

E1=open("Show Prevision.csv")
F1=csv.reader(E1)
D1=[]
matrice5=[]
for ligne in F1:
    D1=ligne[0].split(';')
    matrice5.append(D1)

SS=open("SS.csv")
SS1=csv.reader(SS)
SS2=[]
matrice6=[]
for ligne in SS1:
    SS2=ligne[0].split(';')
    matrice6.append(SS2)


with connec:
   for i in range(1, len(matrice)):
       c.execute('INSERT OR IGNORE INTO Produit VALUES (?,?,?,?,?,?)', (matrice[i][0], matrice[i][1], matrice[i][2],matrice[i][3],matrice[i][4],matrice[i][5]))

with connec:
   for i in range(1, len(matrice1)):
       c.execute('INSERT OR IGNORE INTO ClassB VALUES (?,?,?,?,?,?)', (matrice1[i][0], matrice1[i][1], matrice1[i][2],matrice1[i][3],matrice1[i][4],matrice1[i][5]))

with connec:
    for i in range(1,len(matrice2)):
        c.execute('INSERT OR IGNORE INTO ClassC VALUES (?,?,?,?,?,?)', (matrice2[i][0], matrice2[i][1], matrice2[i][2],matrice2[i][3],matrice2[i][4],matrice2[i][5]))

with connec:
    for i in range(1, len(matrice3)):
        c.execute('INSERT OR IGNORE INTO ClassA VALUES (?,?,?,?,?)', (matrice3[i][0], matrice3[i][1], matrice3[i][2],matrice3[i][3],matrice3[i][4]))

with connec:
    for i in range(1, len(matrice4)):
        c.execute('INSERT OR IGNORE INTO Prevision VALUES (?,?,?,?)', (matrice4[i][0], matrice4[i][1], matrice4[i][2],matrice4[i][3]))

with connec:
    for i in range(1, len(matrice5)):
        c.execute('INSERT OR IGNORE INTO PrevisionShow VALUES (?,?,?,?)', (matrice5[i][0], matrice5[i][1], matrice5[i][2],matrice5[i][3]))

with connec:
    for i in range(1, len(matrice6)):
        c.execute('INSERT OR IGNORE INTO StockSecurite VALUES (?,?)', (matrice6[i][0], matrice6[i][1]))


# Databse functions ----------
def IdProduct():
    ids_P = c.execute('SELECT idProduit FROM Produit;')
    return ids_P.fetchall()

def ProductNames():
    PNames =  c.execute('SELECT NomeProduit FROM Produit;')
    return PNames.fetchall()

def Add_Product(idp,PName,demande,prix,stock,Class):
    with connec:
        c.execute("INSERT OR IGNORE INTO Produit VALUES(?, ?, ?, ?, ?, ?)", (idp,PName,demande,prix,stock,Class))

def ShowProductInfo(idp):
    IPShow = c.execute("SELECT * FROM Produit WHERE idProduit = ?", (idp,))
    return IPShow.fetchone()

def ClassA():
    ClassAI = c.execute("SELECT * FROM ClassA;")
    return ClassAI.fetchall()

def ClassB():
    ClassBI = c.execute("SELECT * FROM ClassB;")
    return ClassBI.fetchall()

def ClassC():
    ClassCI = c.execute("SELECT * FROM ClassC;")
    return ClassCI.fetchall()

def OutputA():
    OA = c.execute("SELECT Output FROM ClassA;")
    return OA.fetchall()

def AvailableA(a):
    with connec:
        for i in range(0,len(a)):
            c.execute("UPDATE ClassA SET Available_stock = ? WHERE Jours = ?",(a[i],i+1))

def UPDATE_CommandA(z):
    with connec:
        c.execute("UPDATE ClassA SET Command  = 0 WHERE Available_stock != ?", (z,))
        c.execute("UPDATE ClassA SET Command  = 2000 WHERE Available_stock <= ?",(z,))



def OutputB():
    OB = c.execute("SELECT Output FROM ClassB;")
    return OB.fetchall()

def AvailableB(b):
    with connec:
        for i in range(0,len(b)):
            c.execute("UPDATE ClassB SET Available_stock = ? WHERE Jours = ?",(b[i],i+1))

def UPDATE_CommandB(x,h):
    with connec:
        c.execute("UPDATE ClassB SET Command = 600 - ? WHERE Jours = ?",(x,h))

def LessUPDATE(b):
    with connec:
        for i in range(0,len(b)):
            c.execute("UPDATE ClassB SET Mul = (Available_stock + Command) WHERE Jours = ?",(i+1,))

def OutputC():
    OC = c.execute("SELECT Output FROM ClassC;")
    return OC.fetchall()

def AvailableC(b):
    with connec:
        for i in range(0,len(b)):
            c.execute("UPDATE ClassC SET Available_stock = ? WHERE Jours = ?",(b[i],i+1))

def UPDATE_CommandC(h):
    with connec:
        c.execute("UPDATE ClassC SET Command = 300 WHERE Jours = ?",(h,))

def LessUPDATE2(b):
    with connec:
        for i in range(0,len(b)):
            c.execute("UPDATE ClassC SET Mul = (Available_stock + Command) WHERE Jours = ?",(i+1,))

def tP():
    tP = c.execute("SELECT t FROM Prevision;")
    return tP.fetchall()

def Demande():
    DP = c.execute("SELECT Demande FROM Prevision;")
    return DP.fetchall()

def DPrevision(b):
    with connec:
        for i in range(0,len(b)):
            c.execute("UPDATE PrevisionShow SET Demande = ? WHERE t = ?",(b[i],i+1))

def Prevision():
    Prevision = c.execute("SELECT * FROM PrevisionShow;")
    return Prevision.fetchall()

def MulC():
    MulC =  c.execute('SELECT Mul FROM ClassC;')
    return MulC.fetchall()

def x():
    x =  c.execute('SELECT x FROM StockSecurite;')
    return x.fetchall()

def n():
    n =  c.execute('SELECT n FROM StockSecurite;')
    return n.fetchall()