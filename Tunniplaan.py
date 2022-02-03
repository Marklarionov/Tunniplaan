from tkinter import * 
from tkinter.messagebox import *
def failist_sõnastikusse():
	tund_kirjeldus={}
	file=open("Tunnid_kirjeldused.txt","r")
	for line in file:
		tund,kirjeldus=line.strip().split(":")
		tund_kirjeldus[tund.strip()]=kirjeldus.strip()
	file.close()
	print(tund_kirjeldus)
	return tund_kirjeldus

tund_kirjeldus=failist_sõnastikusse()
def kirjeldus_akn(t:str):
	if (askyesno("Küsimus","Kas tahad kirjeldust näha?")):
		alam_aken=Toplevel()
		lbl_kirjeldus=Label(alam_aken,text=tund_kirjeldus[t]).pack()
		alam_aken.geometry("600x600")
		c=Canvas(alam_aken,height=500,width=500)
		file=PhotoImage(file=t)
		c.create_image(10,10,image=file,anchor=NW)
		c.pack()
		alam_aken.mainloop()
	else:
		showinfo("Vastus","Kui ei taha,siis ei taha!")

j=0
def veel():
	global j
	if j==0:
		aken.geometry(str(win.winfo_width())+"x"+str(aken.winfo_height()-350))
		btn_veel.config(text="+")
		j=1
	else:
		aken.geometry(str(win.winfo_width())+"x"+str(aken.winfo_height()+350))
		btn_veel.config(text="-")
		j=0
win=Tk()
win.geometry("1200x800")
win.title("Tunniplan")
p=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede"]
j=0
for i in range(2,11,2):
	Ep=Label(win,text=p[j],font="Arial 20",relief="groove").grid(row=i,column=0,rowspan=2,sticky=N+S+W+E)
	j+=1
keel=["7:40-8:25","8:30-9:15","9:20-10:05","10:10-10:55","11:00-11:45","11:50-12:35","12:40-13:25","13:30-14:15","14:20-15:05","15:10-15:55","16:00-16:45"]
k=0
for i in range(1,12,1):
	Ek=Label(win,text=keel[k],font="Arial 6",relief="flat").grid(row=1,column=i,rowspan=2,sticky=N)
	k+=1
Rp=Label(win,text="TARpv21",font="Arial 16",relief="flat").grid(row=0,column=0,sticky=N+S+W+E)
Ep=Label(win,text="",relief="flat").grid(row=1,column=0,rowspan=1,sticky=N+S+W+E)
for i in range(11):
	tn="t"+str(i)
	tn=Label(win,text=i,font="Arial 20",relief="groove").grid(row=0,column=i+1,sticky=N+S+W+E)

btn_veel=Button(win,text="+", font="Calibri 26",bg="green",command=veel)
btn_veel.place(x=1060,y=400)
    


#NADAL
Not=Label(win,text="",bg="White",relief="solid").grid(row=0,column=0,columnspan=2,sticky=N+S+W+E)
Ep=Label(win,text="Esmaspäev",font="Arial 15",width=10,height=5,bg="White",relief="solid").grid(row=1,column=0,rowspan=2,sticky=N+S+W+E)
Tp=Label(win,text="Tesipäev",font="Arial 15",width=10,height=5,bg="White",relief="solid").grid(row=3,column=0,rowspan=2,sticky=N+S+W+E)
Kp=Label(win,text="Kolmapäev",font="Arial 15",width=10,height=5,bg="White",relief="solid").grid(row=5,column=0,rowspan=2,sticky=N+S+W+E)
Np=Label(win,text="Neljapäev",font="Arial 15",width=10,height=5,bg="White",relief="solid").grid(row=7,column=0,rowspan=2,sticky=N+S+W+E)
Rp=Label(win,text="Reede",font="Arial 15",width=10,height=5,bg="White",relief="solid").grid(row=9,column=0,rowspan=2,sticky=N+S+W+E)

#EMPTY
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=1,rowspan=2,column=1,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=3,rowspan=2,column=1,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=5,rowspan=2,column=1,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=7,rowspan=2,column=1,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=9,rowspan=2,column=1,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=9,rowspan=2,column=2,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=1,column=4,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=2,column=7,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=3,rowspan=2,column=6,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=5,rowspan=2,column=5,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=9,rowspan=2,column=7,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=1,rowspan=2,column=9,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=1,rowspan=2,column=10,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=1,rowspan=2,column=11,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=3,rowspan=2,column=11,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=5,rowspan=2,column=11,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=7,rowspan=2,column=9,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=7,rowspan=2,column=10,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=7,rowspan=2,column=11,sticky=N+S+W+E)
O=Label(win,text="",font="Arial 15",bg="White",relief="sunken").grid(row=9,rowspan=2,column=11,sticky=N+S+W+E)

#TUNDS
t0=Label(win,text="0",font="Arial 15",width=8,height=3,bg="White",relief="solid").grid(row=0,column=1,sticky=N+S+W+E)
t1=Label(win,text="1",font="Arial 15",width=8,height=3,bg="White",relief="solid").grid(row=0,column=2,sticky=N+S+W+E)
t2=Label(win,text="2",font="Arial 15",width=8,height=3,bg="White",relief="solid").grid(row=0,column=3,sticky=N+S+W+E)
t3=Label(win,text="3",font="Arial 15",width=8,height=3,bg="White",relief="solid").grid(row=0,column=4,sticky=N+S+W+E)
t4=Label(win,text="4",font="Arial 15",width=8,height=3,bg="White",relief="solid").grid(row=0,column=5,sticky=N+S+W+E)
t5=Label(win,text="5",font="Arial 15",width=8,height=3,bg="White",relief="solid").grid(row=0,column=6,sticky=N+S+W+E)
t6=Label(win,text="6",font="Arial 15",width=8,height=3,bg="White",relief="solid").grid(row=0,column=7,sticky=N+S+W+E)
t7=Label(win,text="7",font="Arial 15",width=8,height=3,bg="White",relief="solid").grid(row=0,column=8,sticky=N+S+W+E)
t8=Label(win,text="8",font="Arial 15",width=8,height=3,bg="White",relief="solid").grid(row=0,column=9,sticky=N+S+W+E)
t9=Label(win,text="9",font="Arial 15",width=8,height=3,bg="White",relief="solid").grid(row=0,column=10,sticky=N+S+W+E)
t10=Label(win,text="10",font="Arial 15",width=8,height=3,bg="White",relief="solid").grid(row=0,column=11,sticky=N+S+W+E)

#ESMAPSPÄEV
MultiBtn=Button(win,text="Multimeedia",command=lambda:kirjeldus_akn("sun.gif"),font="Arial 15",width=8,height=2,bg="#7297FF",relief="sunken").grid(row=1,column=2,columnspan=2,sticky=N+S+W+E)
MultiBtn=Button(win,text="Multimeedia",command=lambda:kirjeldus_akn("sun.gif"),font="Arial 15",width=8,height=2,bg="#7297FF",relief="sunken").grid(row=2,column=5,columnspan=2,sticky=N+S+W+E)
ProgBtn=Button(win,text="Programmerimise alused",command=lambda:kirjeldus_akn("prog.png"),font="Arial 15",width=8,height=2,bg="#4DD1FA",relief="sunken").grid(row=2,column=2,columnspan=3,sticky=N+S+W+E)
ProgBtn=Button(win,text="Programmerimise alused",command=lambda:kirjeldus_akn("prog.png"),font="Arial 15",width=8,height=2,bg="#4DD1FA",relief="sunken").grid(row=1,column=5,columnspan=3,sticky=N+S+W+E)
Ruhmbtn=Button(win,text="Rühma\njuhataja\n tund",command=lambda:kirjeldus_akn("Ruhmajuhataja tund"),font="Arial 15",width=8,height=2,bg="#4DD1FA",relief="sunken").grid(row=1,column=8,rowspan=2,sticky=N+S+W+E)

#TEISIPÄEV
IngBtn=Button(win,text="Inglise Keel",command=lambda:kirjeldus_akn("Inglise Keel"),font="Arial 15",width=8,height=2,bg="#F9F2E1",relief="sunken").grid(row=3,column=2,columnspan=2,sticky=N+S+W+E)
IngBtn=Button(win,text="Inglise Keel",command=lambda:kirjeldus_akn("Inglise Keel"),font="Arial 15",width=8,height=2,bg="#CB94E6",relief="sunken").grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
OPBtn=Button(win,text="Operats. alused",command=lambda:kirjeldus_akn("Operats. alused"),font="Arial 15",width=8,height=2,bg="#BB6DE6",relief="sunken").grid(row=3,rowspan=2,column=4,columnspan=2,sticky=N+S+W+E)
KehBtn=Button(win,text="Kehaline kasvatus",command=lambda:kirjeldus_akn("Kehaline kasvatus"),font="Arial 15",width=8,height=2,bg="#DE688E",relief="sunken").grid(row=3,rowspan=2,column=7,columnspan=2,sticky=N+S+W+E)
EstBtn=Button(win,text="Eesti keel",command=lambda:kirjeldus_akn("Eesti keel"),font="Arial 15",width=8,height=2,bg="#CB9DFF",relief="sunken").grid(row=3,column=9,sticky=N+S+W+E)
EstBtn=Button(win,text="Eesti keel",command=lambda:kirjeldus_akn("Eesti keel"),font="Arial 15",width=8,height=2,bg="#A2A0BD",relief="sunken").grid(row=4,column=9,sticky=N+S+W+E)
AjalBtn=Button(win,text="Ajalugu",command=lambda:kirjeldus_akn("Ajalugu"),font="Arial 15",width=8,height=2,bg="#F5D98F",relief="sunken").grid(row=3,rowspan=2,column=10,sticky=N+S+W+E)

#KOLMAPÄEV
ProgBtn=Button(win,text="Programmerimise alused",command=lambda:kirjeldus_akn("Programmerimise alused"),font="Arial 15",width=8,height=2,bg="#4DD1FA",relief="sunken").grid(row=5,column=2,columnspan=3,sticky=N+S+W+E)
MultiBtn=Button(win,text="Multimeedia",command=lambda:kirjeldus_akn("Multimeedia"),font="Arial 15",width=8,height=2,bg="#7297FF",relief="sunken").grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
MultiBtn=Button(win,text="Multimeedia",command=lambda:kirjeldus_akn("Multimeedia"),font="Arial 15",width=8,height=2,bg="#7297FF",relief="sunken").grid(row=5,column=6,columnspan=3,sticky=N+S+W+E)
ProgBtn=Button(win,text="Programmerimise alused",command=lambda:kirjeldus_akn("Programmerimise alused"),font="Arial 15",width=8,height=2,bg="#4DD1FA",relief="sunken").grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
KunstBtn=Button(win,text="Kunstiained",command=lambda:kirjeldus_akn("Kunstiained"),font="Arial 15",width=8,height=2,bg="#BD70C2",relief="sunken").grid(row=5,rowspan=2,column=9,columnspan=2,sticky=N+S+W+E)

#NELJAPÄEV
BasBtn=Button(win,text="Andmebaasisüsteemide",command=lambda:kirjeldus_akn("Andmebaasisüsteemide"),font="Arial 15",width=8,height=2,bg="#FF6075",relief="sunken").grid(row=7,rowspan=2,column=2,columnspan=2,sticky=N+S+W+E)
BasBtn=Button(win,text="Andmebaasisüsteemide",command=lambda:kirjeldus_akn("Andmebaasisüsteemide"),font="Arial 15",width=8,height=2,bg="#FF6075",relief="sunken").grid(row=7,rowspan=2,column=4,columnspan=3,sticky=N+S+W+E)
AjalBtn=Button(win,text="Ajalugu",command=lambda:kirjeldus_akn("Ajalugu"),font="Arial 15",width=8,height=2,bg="#F5D98F",relief="sunken").grid(row=7,rowspan=2,column=7,sticky=N+S+W+E)
EstBtn=Button(win,text="Eesti keel",command=lambda:kirjeldus_akn("Eesti keel"),font="Arial 15",width=8,height=2,bg="#CB9DFF",relief="sunken").grid(row=7,column=8,sticky=N+S+W+E)
EstBtn=Button(win,text="Eesti keel",command=lambda:kirjeldus_akn("Eesti keel"),font="Arial 15",width=8,height=2,bg="#A2A0BD",relief="sunken").grid(row=8,column=8,sticky=N+S+W+E)

#REEDE
KelBtn=Button(win,text="Keel ja Kirjandus",command=lambda:kirjeldus_akn("Keel ja Kirjandus"),font="Arial 15",width=8,height=2,bg="#D1FF59",relief="sunken").grid(row=9,rowspan=2,column=3,columnspan=2,sticky=N+S+W+E)
MathBtn=Button(win,text="Matemaatika",command=lambda:kirjeldus_akn("Matemaatika"),font="Arial 15",width=8,height=2,bg="#FDB9C4",relief="sunken").grid(row=9,rowspan=2,column=5,columnspan=2,sticky=N+S+W+E)
SuhtBtn=Button(win,text="Suhtl. ja Kliend.",command=lambda:kirjeldus_akn("Suhtl. ja Kliend."),font="Arial 15",width=8,height=2,bg="#A389FF",relief="sunken").grid(row=9,rowspan=2,column=8,columnspan=2,sticky=N+S+W+E)
AjalBtn=Button(win,text="Ajalugu",command=lambda:kirjeldus_akn("Ajalugu"),font="Arial 15",width=8,height=2,bg="#F5D98F",relief="sunken").grid(row=9,rowspan=2,column=10,sticky=N+S+W+E)

win.mainloop()