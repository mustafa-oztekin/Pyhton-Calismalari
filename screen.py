import tkinter as tk
from tkinter import *
import psycopg2
from PIL import ImageTk, Image
import os
import time
import pyqrcode
from tkvideo import tkvideo
from escpos import printer
from PIL import Image
import cv2

#conn=psycopg2.connect('dbname=test')
#cur=conn.cursor()

root= tk.Tk()
root.configure(background="white")
root.geometry("1080x720")
#root.attributes('-fullscreen',True)
root.tcounter = 0
root.pcounter = 0
root.ccounter = 0
root.prize=0


img = ImageTk.PhotoImage(file='rvmtryeni.png')
panel = tk.Label(root, image = img)
panel.place(x=0,y=0)


plasticlabel=Label(root, text='PLASTİK', fg='black', font=("Bold",20), bg="white")
plasticlabel.pack()
plasticlabel.place(x=30, y=120)

img2 = ImageTk.PhotoImage(file='plastic.png')
panel2 = tk.Label(root, image = img2)
panel2.place(x=40,y=150)

plasticnumber=Label(root, text='0', fg='black', font=("Bold",20), bg="white")
plasticnumber.pack()
plasticnumber.place(x=65, y=310)


canlabel=Label(root, text='METAL', fg='black', font=("Bold",20), bg="white")
canlabel.pack()
canlabel.place(x=180, y=120)
img3 = ImageTk.PhotoImage(file='metal.png')
panel3 = tk.Label(root, image = img3)
panel3.place(x=180,y=150)
cannumber=Label(root, text='0', fg='black', font=("Bold",20), bg="white")
cannumber.pack()
cannumber.place(x=215, y=310)

glasslabel=Label(root, text='CAM', fg='black', font=("Bold",20), bg="white")
glasslabel.pack()
glasslabel.place(x=330, y=120)
img4 = ImageTk.PhotoImage(file='cam.png')
panel4 = tk.Label(root, image = img4)
panel4.place(x=330,y=150)
glassnumber=Label(root, text='0', fg='black', font=("Bold",20), bg="white")
glassnumber.pack()
glassnumber.place(x=355, y=305)



textlabel=Label(root, text='', fg='black', font=("Bold",20), bg="white")
textlabel.pack()
textlabel.place(x=500, y=160)

textname=Label(root, text='SON OKUNAN ÜRÜN', fg='red', font=("Bold",20), bg="white")
textname.pack()
textname.place(x=500, y=120)

prizename=Label(root, text='ÖDÜL MİKTARI', fg='red', font=("Bold",20), bg="white")
prizename.pack()
prizename.place(x=500, y=220)

prizeval=Label(root, text='0', fg='black', font=("Bold",20), bg="white")
prizeval.pack()
prizeval.place(x=500, y=250)

totalprizename=Label(root, text='TOPLAM ÖDÜL MİKTARI', fg='red', font=("Bold",20), bg="white")
totalprizename.pack()
totalprizename.place(x=500, y=300)
totalprizeval=Label(root, text='0', fg='black', font=("Bold",20), bg="white")
totalprizeval.pack()
totalprizeval.place(x=500, y=330)

def show (event):
    textlabel.configure(text='')
    x1 = entry1.get()
    cur.execute('select company from rvmtest where id='+str(x1))
    result=cur.fetchone()
    cur.execute('select type from rvmtest where id='+str(x1))
    result2=cur.fetchone()
    textlabel.configure(text=result[0])
    getprize(x1)
    numincrease(result2[0])
    entry1.delete(0, END)
    

def clock():
    hour=time.strftime("%H")
    minute=time.strftime("%M")
    second=time.strftime("%S")
    clock1.config(text="Saat:"+"   " + hour + ":" + minute + ":" + second)
    clock1.after(1000,clock)
clock1=Label(root, text='', font=("Helvetica",20), fg="black", bg="white")
clock1.pack(pady=20)
clock1.place(x=500 ,y=30)
clock()

def numincrease(temp):
    if temp=='teneke':
        root.tcounter+=1
        cannumber.configure(text=str(root.tcounter))
    if temp=='plastik':
        root.pcounter+=1
        plasticnumber.configure(text=str(root.pcounter))
    if temp=='Cam':
        root.ccounter+=1
        glassnumber.configure(text=str(root.ccounter))
    
def getprize(temp):
    global temp2
    cur.execute('select coin from rvmcoin where id='+str(temp))
    result=cur.fetchone()
    prizeval.configure(text=str(result[0])+'TL')
    root.prize+=float(result[0])
    temp2=round(root.prize,2)
    totalprizeval.configure(text=str(temp2)+'TL')
    
def erase():
    prizeval.configure(text='0')
    totalprizeval.configure(text='0')
    cannumber.configure(text='0')
    plasticnumber.configure(text='0')
    glassnumber.configure(text='0')
    textlabel.configure(text='')
    root.tcounter = 0
    root.pcounter = 0
    root.ccounter = 0
    root.prize=0
    
    
img_lbl=Label(root, bg='white')
img_lbl.pack()
img_lbl.place(x=100,y=350)

def getqr():
    global qr,imgqr
    qr = pyqrcode.create(str(temp2))
    imgqr = BitmapImage(data = qr.xbm(scale=6))
    img_lbl.config(image = imgqr)   
    erase()
    
getprizebutton=Button(root, text="İşlemi Bitir Ödül Al",height=4, width=15, bg='blue', command=getqr)  
getprizebutton.pack()
getprizebutton.place(x=500,y=370)

def getprizee():
    p = printer.Usb(0x0519, 0x2013, in_ep=0x81, out_ep=0x03)
    p.set(align='CENTER')
    p.text("ELTAGRON ELEKTRONIK\n")
    p.text("RVMTR TEKNOLOJI\n")
    p.text("\n")
    p.image("rvmtr.png", True)
    p.text("\n")
    p.text("\n")
    p.barcode('1234567891012', 'EAN13', 64,3, '', '', align_ct=True)
    p.text("\n")
    p.qr("En Büyük Eses", size=8)
    p.text("TESEKKUR EDERIZ")
    p.cut()
    
printbutton=Button(root, text="Ödülü Çıktı Al",height=4, width=15, bg='green', command=getprizee)  
printbutton.pack()
printbutton.place(x=700,y=370)

  
root.bind('<Return>', show)

root.mainloop()
