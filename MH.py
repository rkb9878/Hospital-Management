from viewrecord import *
from dischargeslip import *
from admission_slip import *
from searchpatient import *
from viewrecordswithoutself import *
from tkinter import *
import tkinter.ttk as ttk
from tkinter import font
from PIL import ImageTk,Image

def ondoubleclickadmission(event):
    curItem = admissiontree.item(admissiontree.focus())
    col = admissiontree.identify_column(event.x)
    number = curItem['values'][0]
    name = curItem['values'][1]
    date1 = curItem['values'][4]
    date2 = date1.split()
    searchcompletedata.viewdata(number, name, date2[0])
    x = searchcompletedata()

def ondoubleclickdischarge(event):
    curItem = dischargetree.item(dischargetree.focus())
    col = dischargetree.identify_column(event.x)
    number = curItem['values'][0]
    name = curItem['values'][1]
    date1 = curItem['values'][4]
    date2 = date1.split()
    searchcompletedata.viewdata(number, name, date2[0])
    x = searchcompletedata()

def admission_slip1(event):
    x = admission(root)
def searchpatient1(event):
    x = search(root)
def viewrecord1(event):
    x = view(root)
def dischargeslip(event):
    x = discharge(root)
root = Tk()
root.state('zoomed')
root.title('Military Hospital')
root.iconbitmap(default="MH.ico")
#-=====------------------Notebook----------------------------
f = font.Font(family='helvetica', size=18)
s = ttk.Style()
s.configure('.', font=f)
#---------------Notebook------------------------------------
note = ttk.Notebook(root, width=1845, height=670)
tab1 = Frame(note)
tab2 = Frame(note, bg="#DC143C")
tab3 = Frame(note,bg="light green")
tab4 = Frame(note,bg="#F5DEB3")
note.add(tab1, text="Home")
note.add(tab2, text="Today-admission")
note.add(tab3, text="Today-Discharge")
note.add(tab4, text="Help")
note.pack()
#-----------------shirtcut_key--------------------------
root.bind('<F1>', admission_slip1)
root.bind('<F2>', dischargeslip)
root.bind('<F3>', searchpatient1)
root.bind('<F4>', viewrecord1)
#-------------------------frame for tab1----------------------
maintab1=Frame(tab1)
maintab1.pack(side="left")
#------------sub-frame------------
lefttop=Frame(maintab1,bg="snow",relief="solid",borderwidth=1)
lefttop.pack()
leftdown=Frame(maintab1,bg="snow",relief="solid",borderwidth=1)
leftdown.pack( padx=10, pady=10)
#-----------------------------
righttab1=Frame(tab1,bg='snow' , relief="solid",borderwidth=1)
righttab1.pack(side="right")
#----------home page code--------------------------------------
clock = Label(lefttop, font=('times', 20, 'bold'), bg='snow')
date1 = Label(lefttop, font=('times', 15, 'bold'), bg='snow')
clock.pack(fill=BOTH, expand=1)
date1.pack(fill=BOTH, expand=1)
def tick():
    now = datetime.datetime.now()
    time2 =  str(now.strftime("%I:%M:%S %p"))
    time3 = str(now.strftime("%A,%d-%b-%y"))
    clock.config(text=time2)
    date1.config(text=time3)
    clock.after(200, tick)
tick()
Button(leftdown, text="Admission Patient",borderwidth=1, font=("arial", 12, "bold"), fg="green", width=30,command=lambda :admission_slip1("")).grid(row=0,column=0,padx=20, pady=21)
Button(leftdown, text="Discharge Patient",borderwidth=1, font=("arial", 12, "bold"), fg="green", width=30,command=lambda :dischargeslip("")).grid(row=1,column=0,padx=20, pady=21)
Button(leftdown, text="Search Patient",borderwidth=1, font=("arial", 12, "bold"), fg="brown", width=30,command=lambda :searchpatient1("")).grid(row=2,column=0,padx=20, pady=21)
Button(leftdown, text="View Record",borderwidth=1, font=("arial", 12, "bold"), fg="brown", width=30,command=lambda :viewrecord1("")).grid(row=3,column=0,padx=20, pady=21)
Button(leftdown, text="Exit",borderwidth=1, font=("arial", 12, "bold"), fg="white",bg="red", width=30,command=lambda :root.destroy()).grid(row=4,column=0,padx=20, pady=21)
path = "indian.jpg"
img = ImageTk.PhotoImage(Image.open(path))
lb1 = Label(righttab1, image=img,bg='snow',height=500,width=700)
lb1.pack(padx=150,pady=20)
lb=Label(righttab1,text="MILITARY HOSPITAL",font=("Elephent",30,"bold"),bg="snow",fg="brown").pack()
# ------------------------treeview for tab2-----------------------
f = font.Font(family='helvetica', size=11)
s = ttk.Style()
s.configure('.', font=f)
lb = Label(tab2, text="Admission Records", font=("arial", 30, "bold"), bg="#DC143C", fg="#FFFFE0").pack()
admissiontree = ttk.Treeview(tab2, selectmode='browse',column=("number", "name", "dis", "ward", "adtime", "seenby"))
vsb = ttk.Scrollbar(tab2, orient="vertical", command=admissiontree.yview)
vsb.pack(side=RIGHT, fill=Y)
admissiontree.configure(yscrollcommand=vsb.set)
admissiontree.pack(side="top",fill="both",expand=1)
admissiontree.heading("number", text="Number")
admissiontree.heading("name", text="Name")
admissiontree.heading("dis", text="Disease")
admissiontree.heading("ward", text="Ward")
admissiontree.heading("adtime", text="Admission date time")
admissiontree.heading("seenby", text="Seen By")
admissiontree.column("#0", width=0)
admissiontree.bind("<Double-1>",ondoubleclickadmission)
#-----------------admission record function-------------
def admissiontree1():
    now = datetime.datetime.now()
    time3 = str(now.strftime("%y-%m-%d"))
    dr = connection()
    cr = dr.conn.cursor()
    query="SELECT `number`,`n_patient`,`disease`,`ward`,`datetime`,`seenby` FROM `patientdata` WHERE adddate='"+time3+"'and disdate is null order by `n_patient` ASC"
    cr.execute(query)
    p = cr.fetchall()
    for k in admissiontree.get_children():
        admissiontree.delete(k)
    for i in range(0, len(p)):
        admissiontree.insert("", value=p[i], index=i)
admissiontree1()
bt1=Button(tab2,text="Refresh",font=("times new roman", 9, "bold"), fg="brown", bg="#FAFAD2",activebackground="snow", activeforeground="brown", height=1, width=10,command=admissiontree1)
bt1.pack()
# -================================================
lb = Label(tab3, text="Discharge Records", font=("arial", 30, "bold"), bg="light green", fg="blue").pack()
dischargetree = ttk.Treeview(tab3, selectmode='browse',column=("number", "name", "disease","ward", "adtime","discharge","seenby"))
vsb = ttk.Scrollbar(tab3, orient="vertical", command=dischargetree.yview)
vsb.pack(side=RIGHT, fill=Y)

dischargetree.configure(yscrollcommand=vsb.set)
dischargetree.pack(side="top",fill="both",expand=1)
dischargetree.heading("number", text="Number")
dischargetree.heading("name", text="Name")
dischargetree.heading("disease", text="disease")
dischargetree.heading("ward", text="Ward")
dischargetree.heading("adtime", text="Admission date time")
dischargetree.heading("discharge", text="Discharge date time")
dischargetree.heading("seenby", text="seen By")

dischargetree.column("#0", width=0)
dischargetree.column("#1", width=80)
dischargetree.column("#4", width=60)
dischargetree.bind("<Double-1>",ondoubleclickdischarge)
def dischargetree1():
    now = datetime.datetime.now()
    time3 = str(now.strftime("%y-%m-%d"))
    dr = connection()
    cr = dr.conn.cursor()
    query1="SELECT `number`,`n_patient`,`disease`,`ward`,`datetime`,`dischargedate`,`seenby` FROM `patientdata` WHERE  disdate is NOT null and disdate='"+time3+"' order by n_patient ASC"
    cr.execute(query1)
    p = cr.fetchall()
    for k in dischargetree.get_children():
        dischargetree.delete(k)
    for i in range(0, len(p)):
        dischargetree.insert("", value=p[i], index=i)
dischargetree1()
bt=Button(tab3,text="Refresh",font=("times new roman",9,"bold"),fg="white", bg="brown",activebackground="snow", activeforeground="brown", height=1, width=10,command=dischargetree1)
bt.pack(side="bottom")

helptab=Frame(tab4,bg="#D2691E")
helptab.pack(pady=100)
Label(helptab,text="Welcome to MH v1.0 Help!!!!",font=("times new roman",18,"bold","underline"),fg="white",bg="#D2691E").pack(pady=10)
Label(helptab,text="For any help contact developers.",font=("times new roman",15,"bold"),fg="white",bg="#D2691E").pack()
Label(helptab,text="Email Address:'rkb6280@gmail.com'",font=("times new roman",15,"bold"),fg="white",bg="#D2691E").pack()
Label(helptab,text="Email Address:'akb9115@gmail.com'",font=("times new roman",15,"bold"),fg="white",bg="#D2691E").pack()
Label(helptab,text="Developed in Python and in other open source softwares.",font=("times new roman",15,"bold"),fg="white",bg="#D2691E").pack()
Label(helptab,text="DEVELOPED AND CONTRIBUTED TO OUR NATION",font=("times new roman",15,"bold"),fg="white",bg="#D2691E").pack()
Label(helptab,text="By 'Bharti Brothers'.",font=("times new roman",15,"bold","underline"),fg="white",bg="#D2691E").pack()
Label(helptab,text="Built on 5 Jan 2019.",font=("times new roman",15,"italic"),fg="white",bg="#D2691E").pack()
Label(helptab,text="Copyright 2019. All rights reserved.",font=("times new roman",15,"italic"),fg="white",bg="#D2691E").pack()
# -========================
root.mainloop()
