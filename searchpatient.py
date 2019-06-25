from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter import *
from openadmissionpdf import *
from opendischargepdf import *

from server import *

class search(Toplevel):

    def openadpdf(self,event):
        global admissiondate
        if self.tf_number.get()=='' or self.cb_patientname.get()=='' or admissiondate=='':
            showerror('Message','Invalid Data Input!!!!')
        else:
            openadmissionpdf.open(self,self.tf_number.get(),self.cb_patientname.get(),admissiondate)

    def opendispdf(self,event):
        global dischargedate
        if self.tf_number.get()=='' or self.cb_patientname.get()=='' or admissiondate=='':
            showerror('Message','Invalid Data Input!!!!')
        else:
            if dischargedate==None:
                showerror('Message','Patient has not been discharged yet!!!!')
            else:
                opendischargepdf.open(self,self.tf_number.get(),self.cb_patientname.get(),dischargedate)

    def exit(self):
        self.destroy()

    def final_search(self,event):
        global name
        global number
        date=self.cb_date.get()
        if date=='':
            showerror('Message','Please fill in a valid date!!!!')
        else:
            self.lb_officialnameview.configure(text='')
            self.lb_serviceview.configure(text='')
            self.lb_rankview.configure(text='')
            self.lb_mobileview.configure(text='')
            dr1=connection()
            query1="select rank,name,service,mobile from officialdata where number='"+number+"'"
            cr1=dr1.conn.cursor()
            cr1.execute(query1)
            result1=cr1.fetchone()
            for data in result1:
                rank=result1[0]
                officialname=result1[1]
                service=result1[2]
                mobile=result1[3]
            self.lb_officialnameview.configure(text=officialname)
            self.lb_serviceview.configure(text=service)
            self.lb_rankview.configure(text=rank)
            self.lb_mobileview.configure(text=mobile)

            self.lb_nameview.configure(text='')
            self.lb_relationshipview.configure(text='')
            self.lb_admissiondateview.configure(text='')
            self.lb_dischargedateview.configure(text='')
            self.lb_sexview.configure(text='')
            self.lb_ageview.configure(text='')
            self.lb_maritalview.configure(text='')
            self.lb_religionview.configure(text='')
            self.lb_typeofadview.configure(text='')
            self.lb_transferredfromview.configure(text='')
            self.lb_receivedasview.configure(text='')
            self.lb_diseaseview.configure(text='')
            self.lb_dietview.configure(text='')
            self.lb_diagnosisview.configure(text='')
            self.lb_seenbyview.configure(text='')
            self.lb_wardview.configure(text='')
            self.lb_remarksview.configure(text='')
            dr2=connection()
            query2="select * from patientdata where number='"+number+"' and n_patient='"+name+"' and adddate='"+date+"'"
            cr2=dr2.conn.cursor()
            cr2.execute(query2)
            result2=cr2.fetchone()
            for i in result2:
                global dischargedate
                global admissiondate
                admissiondate=result2[3]
                dischargedate=result2[4]
                self.lb_nameview.configure(text=result2[6])
                self.lb_relationshipview.configure(text=result2[7])
                self.lb_admissiondateview.configure(text=result2[3])
                self.lb_dischargedateview.configure(text=result2[4])
                self.lb_sexview.configure(text=result2[8])
                self.lb_ageview.configure(text=result2[9])
                self.lb_maritalview.configure(text=result2[10])
                self.lb_religionview.configure(text=result2[11])
                self.lb_typeofadview.configure(text=result2[12])
                self.lb_transferredfromview.configure(text=result2[13])
                self.lb_receivedasview.configure(text=result2[16])
                self.lb_diseaseview.configure(text=result2[14])
                self.lb_dietview.configure(text=result2[15])
                self.lb_diagnosisview.configure(text=result2[17])
                self.lb_seenbyview.configure(text=result2[18])
                self.lb_wardview.configure(text=result2[19])
                self.lb_remarksview.configure(text=result2[20])



    def date_search(self,event):
        global number
        global name
        name=self.cb_patientname.get()
        if name=='':
            showerror('Message','Please enter the name to search!!!!')
        else:
            dr = connection()
            query = "select adddate from patientdata where number='" + number + "' and n_patient='" + name + "'"
            cr=dr.conn.cursor()
            cr.execute(query)
            result=cr.fetchall()
            lst_date = []
            for i in range(0, len(result)):
                lst_date.append(result[i][0])

            self.cb_date.config(values=tuple(lst_date))
            self.cb_date.bind("<<ComboboxSelected>>", self.final_search)

    def name_search(self):
        global number
        number=self.tf_number.get()
        if number=='':
            showerror('Message','Please enter the number to search!!!!')
        else:
            dr=connection()
            query="select n_patient from patientdata where number='"+self.tf_number.get()+"'"
            cr=dr.conn.cursor()
            cr.execute(query)
            result=cr.fetchall()
            lst_pname = []
            for i in range(0, len(result)):
                lst_pname.append(result[i][0])

            self.cb_patientname.config(values=tuple(lst_pname))
            self.cb_patientname.bind("<<ComboboxSelected>>", self.date_search)

    def __init__(self,parent):
        global admissiondate
        global dischargedate
        admissiondate=''
        dischargedate=''
        # self.root = Tk()
        Toplevel.__init__(self, parent)
        self.transient(parent)
        self.parent = parent
        self.configure(background="snow")
        self.title("SEARCH DETAILS")
        self.iconbitmap(self, default="MH.ico")
        # self.state('zoomed')
        # self.resizable(0, 0)
        self.geometry("{0}x{0}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.f = Frame(self, bg="snow")
        self.f.pack()
        self.lb_header = Label(self.f, text="Please fill the patient details to Search:", bg="snow", fg="brown",font=("times new roman", 20, "bold", "underline"), pady=10)
        self.lb_number = Label(self.f, text="Number:", bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.tf_number = Entry(self.f, width=20, font=("times new roman", 14), relief="solid")
        self.bt_search1 = Button(self.f, text="Search", font=("times new roman", 9, "bold"), fg="white", bg="green",activebackground="snow", activeforeground="brown", height=1, width=10,command=self.name_search)
        self.lb_patientname = Label(self.f, text="Name:", bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.cb_patientname = Combobox(self.f, width=20, font=("times new roman", 14),state='readonly')
        self.lb_date = Label(self.f, text="Date:", bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.cb_date = Combobox(self.f, width=20, font=("times new roman", 14),state='readonly')
        self.lb_officialname = Label(self.f, text="Name of Official:",bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_officialnameview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_service = Label(self.f, text="Service:", bg="snow", font=("times new roman", 14), padx=10,pady=10)
        self.lb_serviceview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_rank = Label(self.f, text="Rank:", bg="snow", font=("times new roman", 14), padx=10,pady=10)
        self.lb_rankview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_mobile = Label(self.f, text="Mobile Number:", bg="snow", font=("times new roman", 14), padx=10,pady=10)
        self.lb_mobileview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_name = Label(self.f, text="Name of patient:", bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_nameview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_relationship = Label(self.f, text="Relationship with patient:", bg="snow", font=("times new roman", 14), padx=10,pady=10)
        self.lb_relationshipview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_admissiondate = Label(self.f,text="Admission Date:", bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_admissiondateview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_dischargedate = Label(self.f, text='Discharge Date:',bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_dischargedateview = Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_sex = Label(self.f,bg="snow", text='Sex:',font=("times new roman", 14), padx=10, pady=10)
        self.lb_sexview = Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_age = Label(self.f,bg="snow", text='Age:',font=("times new roman", 14), padx=10, pady=10)
        self.lb_ageview = Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_marital = Label(self.f,bg="snow",text='Marital Status:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_maritalview = Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_religion = Label(self.f,bg="snow", text='Religion:',font=("times new roman", 14), padx=10, pady=10)
        self.lb_religionview = Label(self.f,bg="snow",font=("times new roman", 14), padx=10, pady=10)
        self.lb_typeofad = Label(self.f,bg="snow",text='Type of Admission:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_typeofadview = Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_transferredfrom = Label(self.f,bg="snow", text='Transferred From:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_transferredfromview = Label(self.f,bg="snow",font=("times new roman", 14), padx=10, pady=10)
        self.lb_receivedas = Label(self.f,bg="snow",text='Received as:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_receivedasview = Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_disease = Label(self.f,bg="snow",text='Disease:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_diseaseview = Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_diet= Label(self.f,bg="snow",text='Diet:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_dietview= Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_diagnosis= Label(self.f,bg="snow",text='Diagnosis:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_diagnosisview= Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_seenby= Label(self.f,bg="snow",text='Seen By:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_seenbyview= Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_ward= Label(self.f,bg="snow",text='Sent to Ward:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_wardview= Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_remarks= Label(self.f,bg="snow",text='Remarks:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_remarksview= Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.bt_adpdf = Button(self.f, text="Open Admission Pdf", font=("times new roman", 11, "bold"), fg="white",bg="red", activebackground="snow", activeforeground="brown", height=1, width=20, command=lambda :self.openadpdf(""))
        self.bt_dispdf = Button(self.f, text="Open Discharge Pdf", font=("times new roman", 11, "bold"), fg="white",bg="red", activebackground="snow", activeforeground="brown", height=1, width=20,command=lambda :self.opendispdf(""))
        self.bt_exit = Button(self.f, text="EXIT", font=("times new roman", 11, "bold"), fg="white", bg="red",activebackground="snow", activeforeground="brown", height=1, width=20, command=self.exit)
        self.bind('<Alt-a>',self.openadpdf)
        self.bind('<Alt-d>',self.opendispdf)


        self.lb_header.grid(row=0,column=0,columnspan=9)
        self.lb_number.grid(row=1,column=1,sticky=(E))
        self.tf_number.grid(row=1,column=2,sticky=(W))
        self.bt_search1.grid(row=1,column=3,sticky=(W))
        self.lb_patientname.grid(row=1,column=4)
        self.cb_patientname.grid(row=1,column=5)
        self.lb_date.grid(row=1,column=7,sticky=(E))
        self.cb_date.grid(row=1,column=8,sticky=(W))
        self.lb_officialname.grid(row=2, column=1, sticky=(E))
        self.lb_officialnameview.grid(row=2, column=2, sticky=(W))
        self.lb_service.grid(row=2, column=7, sticky=(E))
        self.lb_serviceview.grid(row=2, column=8, sticky=(W))
        self.lb_rank.grid(row=3, column=1, sticky=(E))
        self.lb_rankview.grid(row=3, column=2, sticky=(W))
        self.lb_mobile.grid(row=3, column=7, sticky=(E))
        self.lb_mobileview.grid(row=3, column=8, sticky=(W))
        self.lb_name.grid(row=4,column=1,sticky=(E))
        self.lb_nameview.grid(row=4,column=2,sticky=(W))
        self.lb_relationship.grid(row=4, column=7, sticky=(E))
        self.lb_relationshipview.grid(row=4, column=8, sticky=(W))
        self.lb_admissiondate.grid(row=5,column=1,sticky=(E))
        self.lb_admissiondateview.grid(row=5,column=2,sticky=(W))
        self.lb_dischargedate.grid(row=5, column=7, sticky=(E))
        self.lb_dischargedateview.grid(row=5, column=8, sticky=(W))
        self.lb_sex.grid(row=6,column=1,sticky=(E))
        self.lb_sexview.grid(row=6,column=2,sticky=(W))
        self.lb_age.grid(row=6,column=7,sticky=(E))
        self.lb_ageview.grid(row=6,column=8,sticky=(W))
        self.lb_marital.grid(row=7, column=1, sticky=(E))
        self.lb_maritalview.grid(row=7, column=2, sticky=(W))
        self.lb_religion.grid(row=7, column=7, sticky=(E))
        self.lb_religionview.grid(row=7, column=8, sticky=(W))
        self.lb_typeofad.grid(row=8, column=1, sticky=(E))
        self.lb_typeofadview.grid(row=8, column=2, sticky=(W))
        self.lb_transferredfrom.grid(row=8, column=7, sticky=(E))
        self.lb_transferredfromview.grid(row=8, column=8, sticky=(W))
        self.lb_receivedas.grid(row=9, column=1, sticky=(E))
        self.lb_receivedasview.grid(row=9, column=2, sticky=(W))
        self.lb_disease.grid(row=9, column=7, sticky=(E))
        self.lb_diseaseview.grid(row=9, column=8, sticky=(W))
        self.lb_diet.grid(row=10, column=1, sticky=(E))
        self.lb_dietview.grid(row=10, column=2, sticky=(W))
        self.lb_diagnosis.grid(row=10, column=7, sticky=(E))
        self.lb_diagnosisview.grid(row=10, column=8, sticky=(W))
        self.lb_seenby.grid(row=11, column=1, sticky=(E))
        self.lb_seenbyview.grid(row=11, column=2, sticky=(W))
        self.lb_ward.grid(row=11, column=7, sticky=(E))
        self.lb_wardview.grid(row=11, column=8, sticky=(W))
        self.lb_remarks.grid(row=12,column=1,sticky=(E))
        self.lb_remarksview.grid(row=12,column=2,sticky=(W))
        self.bt_adpdf.grid(row=13,column=1,sticky=(W))
        self.bt_dispdf.grid(row=13,column=2,sticky=(E))
        self.bt_exit.grid(row=13,column=8,sticky=(W))

        # self.root.mainloop()
        self.result = None

# x = search()
