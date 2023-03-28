from tkinter import *
import psycopg2
from PIL import ImageTk, Image
import os
import time
import pyqrcode
from tkvideo import tkvideo
#import vlc
from escpos import printer
import serial
import keyboard



con = psycopg2.connect(
                        host = "localhost",
                        database = "my_database",
                        user = "postgres",
                        password = "1234")



barkod = serial.Serial(port='COM4', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)
#arduino = serial.Serial(port='COM3', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)
cur = con.cursor()


root = Tk()
root.title("RVMTR KULLANICI ARAYÜZÜ")
root.geometry("1024x600")
#root.attributes('-fullscreen',True)  /// mini pc ye gecince yapilacak
root.configure(background="white")
root.gcounter = 0
root.pcounter = 0
root.mcounter = 0
root.prize = 0

canvas = Canvas(root, width = 400, height =100)
canvas.place(x=0, y=0)
img = ImageTk.PhotoImage(file='rvmtr.png')
panel = Label(canvas, image = img)
panel.place(x = 0, y = 0)


plasticlabel = Label(root, text='PLASTİK', fg='black', font=("Bold",20), bg="white")
plasticlabel.pack()
plasticlabel.place(x = 20, y = 120)
img2 = ImageTk.PhotoImage(file='plastic.png')
panel2 = Label(root, image = img2)
panel2.place(x=40,y=160)
plasticnumber = Label(root, text='0', fg='black', font=("Bold",20), bg="white")
plasticnumber.pack()
plasticnumber.place(x=65, y=325)


metallabel = Label(root, text='METAL', fg='black', font=("Bold",20), bg="white")
metallabel.pack()
metallabel.place(x = 180, y = 120)
img3 = ImageTk.PhotoImage(file='metal.png')
panel3 = Label(root, image = img3)
panel3.place(x=180,y=162)
metalnumber=Label(root, text='0', fg='black', font=("Bold",20), bg="white")
metalnumber.pack()
metalnumber.place(x=215, y=325)


camlabel = Label(root, text='CAM', fg='black', font=("Bold",20), bg="white")
camlabel.pack()
camlabel.place(x = 315, y = 120)
img4 = ImageTk.PhotoImage(file='cam.png')
panel4 = Label(root, image = img4)
panel4.place(x=315,y=162)
glassnumber=Label(root, text='0', fg='black', font=("Bold",20), bg="white")
glassnumber.pack()
glassnumber.place(x=340, y=325)


okunan_urun = Label(root, text='............', fg='black', font=("Bold",20), bg="white")
okunan_urun.pack()
okunan_urun.place(x=500, y=160)

okunan_urun_baslik = Label(root, text='SON OKUNAN ÜRÜN', fg='red', font=("Bold",20), bg="white")
okunan_urun_baslik.pack()
okunan_urun_baslik.place(x=500, y=120)



odul_miktari_baslik = Label(root, text='ÖDÜL MİKTARI', fg='red', font=("Bold",20), bg="white")
odul_miktari_baslik.pack()
odul_miktari_baslik.place(x=500, y=220)

odul_miktari = Label(root, text='0', fg='black', font=("Bold",20), bg="white")
odul_miktari.pack()
odul_miktari.place(x=575, y=250)


toplam_odul_baslik = Label(root, text='TOPLAM ÖDÜL MİKTARI', fg='red', font=("Bold",20), bg="white")
toplam_odul_baslik.pack()
toplam_odul_baslik.place(x=500, y=300)

toplam_odul = Label(root, text='0', fg='black', font=("Bold",20), bg="white")
toplam_odul.pack()
toplam_odul.place(x=575, y=330)


def clock():
    hour=time.strftime("%H")
    minute=time.strftime("%M")
    second=time.strftime("%S")
    clock1.config(text="Saat:"+"   " + hour + ":" + minute + ":" + second)
    clock1.after(1000,clock)
clock1 = Label(root, text='', font=("Helvetica",20), fg="black", bg="white")
clock1.pack()
clock1.place(x=500 ,y=30)
clock()


def numincrease(tur):
    if tur == 'GLASS':
        root.gcounter += 1
        glassnumber.config(text=str(root.gcounter))
    if tur == 'PLASTIC':
        root.pcounter += 1
        plasticnumber.config(text=str(root.pcounter))
    if tur == 'METAL':
        root.mcounter += 1
        metalnumber.config(text=str(root.mcounter))
        
        
def odul_hesapla(odul):
    global toplam
    odul_miktari.config(text = str(round(float(odul),2)) + 'TL')
    root.prize += float(odul)
    toplam = round(root.prize,2)
    toplam_odul.config(text = str(toplam) + 'TL')
    
    

def erase():
    odul_miktari.config(text='0')
    toplam_odul.config(text='0')
    metalnumber.config(text='0')
    plasticnumber.config(text='0')
    glassnumber.config(text='0')
    okunan_urun.config(text='.........')
    img_lbl.config(image = "")
    #kullanici icin geri sayim yaptirilacak...
    root.mcounter = 0
    root.pcounter = 0
    root.gcounter = 0
    root.prize=0
    
    
    
img_lbl=Label(root, bg='white')
img_lbl.pack()
img_lbl.place(x=100,y=400)
    
def getqr():
    global qr,imgqr
    qr = pyqrcode.create(str(toplam))
    imgqr = BitmapImage(data = qr.xbm(scale=6))
    img_lbl.config(image = imgqr)
    root.after(5000, erase)
    
    
odul_al_buton = Button(root, text="İşlemi Bitir Ödül Al", fg='black', font=("Bold",16), bg='#3BF41E', command=getqr)  
odul_al_buton.pack()
odul_al_buton.place(x=500,y=400)



def getserialport():
    if barkod.in_waiting:
        global okunan_urun
        okunan_urun.config(text = '')
        barkod_veri = barkod.readline()
        barkod_veri = barkod_veri.decode('utf')
        cur.execute("select * from rvmtr where kod =" + str(barkod_veri))
        rows = cur.fetchall()
        
        try:
            veri_isim = rows[0][2]
            okunan_urun = Label(root, text = veri_isim, fg='black', font=("Bold",16), bg="white")
            okunan_urun.pack()
            okunan_urun.place(x=500, y=160)
            
            veri_tur = rows[0][4]
            c = veri_isim.replace(veri_isim,'str'+veri_tur)
            #arduino.write(c.encode('utf-8'))
            
            numincrease(veri_tur)
            veri_odul = rows[0][5]
            odul_hesapla(veri_odul)
            
        
        except Exception as e:
            hata = 'Ürün veritabaninda bulunmuyor...'
            c = 'yok'
            #arduino.write(c.encode('utf-8'))
            okunan_urun = Label(root, text = hata, fg='black', font=("Bold",16), bg="white")
            okunan_urun.pack()
            okunan_urun.place(x=500, y=160)
            
        





while True:
    root.update()
    getserialport()
    if keyboard.is_pressed("q"):
        #print("q pressed, ending loop")
        break

root.destroy()
barkod.close()