from tkinter import *
import tkinter.ttk as ttk
from server import *
from tkcalendar import DateEntry,Calendar
from datetime import *
from viewrecordsearchpatient2 import *
class view:
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
        d1 = datetime.strptime(str(self.fromdate.get()), '%y/%m/%d').strftime('%d-%m-%y')
        d2 = datetime.strptime(str(self.todate.get()), '%y/%m/%d').strftime('%d-%m-%y')
        query = "select `number`,`n_patient`,`disease`,`ward`,`datetime`,`dischargedate` from patientdata where adddate between '" + str(d1) + "' and '" + str(d2) + "'"
        cr = dr.conn.cursor()
        cr.execute(query)
        self.p = cr.fetchall()
        for k in self.tree.get_children():
            self.tree.delete(k)
        for i in range(0, len(self.p)):
            self.tree.insert("", value=self.p[i], index=i)

    def __init__(self):
        self.root = Tk()
        self.root.configure(bg="light green")
        # -=================================
        top = Frame(self.root, bg="light green")
        top.pack()
        down = Frame(self.root, bg="light green")
        down.pack()
        mid = Frame(self.root, bg="light green")
        mid.pack()
        # -================================================
        lb = Label(top, text="Patient Records", font=("arial", 30, "bold"), bg="light green", fg="blue").pack()
        lb = Label(down, text="From ", font=("Arial", 12, "bold"), bg="light green", fg="brown").grid(row=1, column=1,
                                                                                                      sticky=(E))
        lb = Label(down, text="To ", font=("Arial", 12, "bold"), bg="light green", fg="brown").grid(row=1, column=3,sticky=(E))
        lb = Label(down, text="                                                                                                                                         ", font=("Arial", 12, "bold"), bg="light green", fg="brown").grid(row=0, column=3,columnspan=5,sticky=(E))


        self.fromdate = DateEntry(down)
        self.todate = DateEntry(down)
        self.fromdate.grid(row=1, column=2, sticky=(W))
        self.todate.grid(row=1, column=4, sticky=(W))
        Button(down, text="go", font=("arial", 8, "bold"), fg="brown", width=10, command=self.search).grid(row=1,column=5)
        self.tree = ttk.Treeview(self.root, selectmode='browse',column=("number", "name", "dis", "ward", "adtime", "distime"))
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
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
        self.root.mainloop()
    # -============================================================================


x = view()