# from tkinter import *
import tkinter.ttk as ttk
# from server import *
# from tkcalendar import DateEntry,Calendar
# from datetime import *
from viewrecordsearchpatient2 import *
class view(Toplevel):
    def ondoubleclick(self,event):
        curItem = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)
        # print('cell_value1 = ', curItem['values'])
        number=curItem['values'][0]
        name=curItem['values'][1]
        date1=curItem['values'][4]
        date2=date1.split()
        search.viewdata(self,number,name,date2[0])
        x=search()



    def search(self):
        dr = connection()
        fromday=int(self.tf_fromday.get())
        today=int(self.tf_today.get())
        fromyearlength = len(str(self.tf_fromyear.get()))
        frommonthlength = len(str(self.tf_frommonth.get()))
        fromdaylength = len(str(self.tf_fromday.get()))
        toyearlength = len(str(self.tf_toyear.get()))
        tomonthlength = len(str(self.tf_tomonth.get()))
        todaylength = len(str(self.tf_today.get()))
        field_flag = True
        if fromyearlength != 4 or toyearlength != 4 or fromdaylength > 2 or todaylength > 2 or frommonthlength > 2 or tomonthlength > 2 or fromyearlength == 0 or toyearlength == 0 or fromdaylength == 0 or todaylength == 0 or frommonthlength == 0 or tomonthlength == 0 or fromday>31 or today>31:
            field_flag = False
        if field_flag == False:
            showerror("Message", "Invalid Date Input!!!!")
        else:
            fromdate=str(self.tf_fromyear.get())+"-"+str(self.tf_frommonth.get())+"-"+str(self.tf_fromday.get())
            todate=str(self.tf_toyear.get())+"-"+str(self.tf_tomonth.get())+"-"+str(self.tf_today.get())
            query = "select `number`,`n_patient`,`disease`,`ward`,`datetime`,`dischargedate` from patientdata where adddate between '" + str(fromdate) + "' and '" + str(todate) + "' order by `adddate` DESC"
            cr = dr.conn.cursor()
            cr.execute(query)
            self.p = cr.fetchall()
            for k in self.tree.get_children():
                self.tree.delete(k)
            for i in range(0, len(self.p)):
                self.tree.insert("", value=self.p[i], index=i)

    def __init__(self,parent):
        # self.root = Tk()
        Toplevel.__init__(self, parent)
        self.transient(parent)
        self.parent = parent
        self.title("View Record")
        self.configure(bg="light green")
        # self.geometry("1200x500")
        # self.geometry("{0}x{0}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        # -=================================
        top = Frame(self, bg="light green")
        top.pack()
        down = Frame(self, bg="light green")
        down.pack()
        mid = Frame(self, bg="light green")
        mid.pack()
        # -================================================
        lb = Label(top, text="Patient Records", font=("arial", 30, "bold"), bg="light green", fg="blue").pack()
        lb = Label(down, text="From :", font=("Arial", 15, "bold"), bg="light green", fg="brown").grid(row=1, column=0,sticky=(E),padx=10)
        lb = Label(down, text="To :", font=("Arial", 15, "bold"), bg="light green", fg="brown").grid(row=1, column=8,sticky=(E))
        day = Label(down, text="day ", font=("Arial", 8, "bold"), bg="light green", fg="brown").grid(row=1, column=1,sticky=(E))
        self.tf_fromday=Spinbox(down,from_=1,to=31,width=5,wrap=True)
        self.tf_fromday.grid(row=1,column=2)
        month = Label(down, text="month", font=("Arial", 8, "bold"), bg="light green", fg="brown").grid(row=1, column=3,sticky=(E))
        self.tf_frommonth = Spinbox(down,state="readonly",from_=1,to=12,width=5,wrap=True)
        self.tf_frommonth.grid(row=1, column=4)
        year = Label(down, text="year ", font=("Arial", 8, "bold"), bg="light green", fg="brown").grid(row=1, column=5,sticky=(E))
        self.tf_fromyear = Spinbox(down,state="readonly",from_=2018,to=2030,width=10,wrap=True)
        self.tf_fromyear.grid(row=1, column=6)
        year = Label(down, text="           ", font=("Arial", 50, "bold"), bg="light green", fg="brown").grid(row=1, column=7,sticky=(E))
        day = Label(down, text="day ", font=("Arial", 8, "bold"), bg="light green", fg="brown").grid(row=1, column=9,sticky=(E))
        self.tf_today = Spinbox(down,from_=1,to=31,width=5,wrap=True)
        self.tf_today.grid(row=1, column=10)
        month = Label(down, text="month", font=("Arial", 8, "bold"), bg="light green", fg="brown").grid(row=1, column=11,sticky=(E))
        self.tf_tomonth = Spinbox(down,state="readonly",from_=1,to=12,width=5,wrap=True)
        self.tf_tomonth.grid(row=1, column=12)
        year = Label(down, text="year ", font=("Arial", 8, "bold"), bg="light green", fg="brown").grid(row=1, column=13,sticky=(E))
        self.tf_toyear = Spinbox(down,state="readonly",from_=2018,to=2030,width=10,wrap=True)
        self.tf_toyear.grid(row=1, column=14)

        Button(down, text="GO", font=("arial", 8, "bold"), fg="white",bg="#2e2977",activeforeground="snow", width=10, command=self.search).grid(row=1,column=15,padx=10)
        self.tree = ttk.Treeview(self, selectmode='browse',column=("number", "name", "dis", "ward", "adtime", "distime"))
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        vsb.pack(side=RIGHT, fill=Y)
        self.tree.configure(yscrollcommand=vsb.set)

        self.tree.heading("number", text="Number")
        self.tree.heading("name", text="Name")
        self.tree.heading("dis", text="Disease")
        self.tree.heading("ward", text="Ward")
        self.tree.heading("adtime", text="Admission date time")
        self.tree.heading("distime", text="Discharge date time")
        self.tree.pack(side="top",fill="both",expand=1)
        self.tree.column("#0", width=0)
        self.tree.bind("<Double-1>", self.ondoubleclick)
        # self.root.mainloop()
        ttk.Sizegrip(self).pack(side = 'right')

        self.result = None

    # -============================================================================


