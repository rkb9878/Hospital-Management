from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter import *

from server import *

class search:
    def exit(self):
        self.root.destroy()

    def viewdata(self,number,name,date):
        global received_number
        global received_name
        received_number=str(number)
        received_name=name
        global rank
        global officialname
        global service
        global mobile
        global patientname
        global relationship
        global admissiondate
        global dischargedate
        global sex
        global age
        global marital
        global religion
        global typeofad
        global transferredfrom
        global receivedas
        global disease
        global diet
        global diagnosis
        global seenby
        global ward
        global remarks

        dr1=connection()
        query1="select rank,name,service,mobile from officialdata where number='"+str(number)+"'"
        cr1=dr1.conn.cursor()
        cr1.execute(query1)
        result1=cr1.fetchone()
        for data in result1:
            rank=result1[0]
            officialname=result1[1]
            service=result1[2]
            mobile=result1[3]

        dr2=connection()
        query2="select * from patientdata where number='"+str(number)+"' and n_patient='"+str(name)+"' and adddate='"+date+"'"
        cr2=dr2.conn.cursor()
        cr2.execute(query2)
        result2=cr2.fetchone()
        for i in result2:
            patientname=result2[6]
            relationship=result2[7]
            admissiondate=result2[3]
            dischargedate=result2[4]
            sex=result2[8]
            age=result2[9]
            marital=result2[10]
            religion=result2[11]
            typeofad=result2[12]
            transferredfrom=result2[13]
            receivedas=result2[16]
            disease=result2[14]
            diet=result2[15]
            diagnosis=result2[17]
            seenby=result2[18]
            ward=result2[19]
            remarks=result2[20]

    def __init__(self):

        global received_number
        global received_name
        global rank
        global officialname
        global service
        global mobile
        global patientname
        global relationship
        global admissiondate
        global dischargedate
        global sex
        global age
        global marital
        global religion
        global typeofad
        global transferredfrom
        global receivedas
        global disease
        global diet
        global diagnosis
        global seenby
        global ward
        global remarks

        self.root = Tk()
        self.root.configure(background="snow")
        self.root.title("SEARCH DETAILS")
        # self.root.iconbitmap(self, default="MH.ico")
        self.root.state('zoomed')
        self.root.resizable(0, 0)
        self.f = Frame(self.root, bg="snow")
        self.f.pack()
        self.lb_header = Label(self.f, text="PATIENT DETAILS", bg="snow", fg="brown",font=("times new roman", 20, "bold", "underline"), pady=10)
        self.lb_number = Label(self.f, text="Number:", bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_numberview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_numberview.configure(text=received_number)
        self.lb_patientname = Label(self.f, text="Name of patient:", bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_patientnameview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_patientnameview.configure(text=received_name)
        self.lb_admissiondate = Label(self.f, text="Admission Date:", bg="snow", font=("times new roman", 14), padx=10,pady=10)
        self.lb_admissiondateview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_admissiondateview.configure(text=admissiondate)
        self.lb_dischargedate = Label(self.f, text='Discharge Date:', bg="snow", font=("times new roman", 14), padx=10,pady=10)
        self.lb_dischargedateview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_dischargedateview.configure(text=dischargedate)
        self.lb_officialname = Label(self.f, text="Name of Official:",bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_officialnameview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_officialnameview.configure(text=officialname)
        self.lb_service = Label(self.f, text="Service:", bg="snow", font=("times new roman", 14), padx=10,pady=10)
        self.lb_serviceview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_serviceview.configure(text=service)
        self.lb_rank = Label(self.f, text="Rank:", bg="snow", font=("times new roman", 14), padx=10,pady=10)
        self.lb_rankview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_rankview.configure(text=rank)
        self.lb_mobile = Label(self.f, text="Mobile Number:", bg="snow", font=("times new roman", 14), padx=10,pady=10)
        self.lb_mobileview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_mobileview.configure(text=mobile)
        self.lb_relationship = Label(self.f, text="Relationship with patient:", bg="snow", font=("times new roman", 14), padx=10,pady=10)
        self.lb_relationshipview = Label(self.f, bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_relationshipview.configure(text=relationship)
        self.lb_sex = Label(self.f,bg="snow", text='Sex:',font=("times new roman", 14), padx=10, pady=10)
        self.lb_sexview = Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_sexview.configure(text=sex)
        self.lb_age = Label(self.f,bg="snow", text='Age:',font=("times new roman", 14), padx=10, pady=10)
        self.lb_ageview = Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_ageview.configure(text=age)
        self.lb_marital = Label(self.f,bg="snow",text='Marital Status:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_maritalview = Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_maritalview.configure(text=marital)
        self.lb_religion = Label(self.f,bg="snow", text='Religion:',font=("times new roman", 14), padx=10, pady=10)
        self.lb_religionview = Label(self.f,bg="snow",font=("times new roman", 14), padx=10, pady=10)
        self.lb_religionview.configure(text=religion)
        self.lb_typeofad = Label(self.f,bg="snow",text='Type of Admission:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_typeofadview = Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_typeofadview.configure(text=typeofad)
        self.lb_transferredfrom = Label(self.f,bg="snow", text='Transferred From:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_transferredfromview = Label(self.f,bg="snow",font=("times new roman", 14), padx=10, pady=10)
        self.lb_transferredfromview.configure(text=transferredfrom)
        self.lb_receivedas = Label(self.f,bg="snow",text='Received as:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_receivedasview = Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_receivedasview.configure(text=receivedas)
        self.lb_disease = Label(self.f,bg="snow",text='Disease:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_diseaseview = Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_diseaseview.configure(text=disease)
        self.lb_diet= Label(self.f,bg="snow",text='Diet:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_dietview= Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_dietview.configure(text=diet)
        self.lb_diagnosis= Label(self.f,bg="snow",text='Diagnosis:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_diagnosisview= Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_diagnosisview.configure(text=diagnosis)
        self.lb_seenby= Label(self.f,bg="snow",text='Seen By:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_seenbyview= Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_seenbyview.configure(text=seenby)
        self.lb_ward= Label(self.f,bg="snow",text='Sent to Ward:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_wardview= Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_wardview.configure(text=ward)
        self.lb_remarks= Label(self.f,bg="snow",text='Remarks:', font=("times new roman", 14), padx=10, pady=10)
        self.lb_remarksview= Label(self.f,bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.lb_remarksview.configure(text=remarks)
        self.bt_exit = Button(self.f, text="EXIT", font=("times new roman", 11, "bold"),  fg="white", bg="red",activebackground="snow", activeforeground="brown", height=1, width=20, command=self.exit)

        self.lb_header.grid(row=0,column=5,sticky=(W))
        self.lb_number.grid(row=1,column=1,sticky=(W))
        self.lb_numberview.grid(row=1,column=2,sticky=(W))
        self.lb_patientname.grid(row=1,column=7,sticky=(W))
        self.lb_patientnameview.grid(row=1,column=8,sticky=(W))
        self.lb_admissiondate.grid(row=2, column=1, sticky=(W))
        self.lb_admissiondateview.grid(row=2, column=2, sticky=(W))
        self.lb_dischargedate.grid(row=2, column=7, sticky=(W))
        self.lb_dischargedateview.grid(row=2, column=8, sticky=(W))
        self.lb_officialname.grid(row=3, column=1, sticky=(W))
        self.lb_officialnameview.grid(row=3, column=2, sticky=(W))
        self.lb_service.grid(row=3, column=7, sticky=(W))
        self.lb_serviceview.grid(row=3, column=8, sticky=(W))
        self.lb_rank.grid(row=4, column=1, sticky=(W))
        self.lb_rankview.grid(row=4, column=2, sticky=(W))
        self.lb_mobile.grid(row=4, column=7, sticky=(W))
        self.lb_mobileview.grid(row=4, column=8, sticky=(W))
        self.lb_relationship.grid(row=5, column=1, sticky=(W))
        self.lb_relationshipview.grid(row=5, column=2, sticky=(W))
        self.lb_sex.grid(row=5,column=7,sticky=(W))
        self.lb_sexview.grid(row=5,column=8,sticky=(W))
        self.lb_age.grid(row=6,column=1,sticky=(W))
        self.lb_ageview.grid(row=6,column=2,sticky=(W))
        self.lb_marital.grid(row=6, column=7, sticky=(W))
        self.lb_maritalview.grid(row=6, column=8, sticky=(W))
        self.lb_religion.grid(row=7, column=1, sticky=(W))
        self.lb_religionview.grid(row=7, column=2, sticky=(W))
        self.lb_typeofad.grid(row=7, column=7, sticky=(W))
        self.lb_typeofadview.grid(row=7, column=8, sticky=(W))
        self.lb_transferredfrom.grid(row=8, column=1, sticky=(W))
        self.lb_transferredfromview.grid(row=8, column=2, sticky=(W))
        self.lb_receivedas.grid(row=8, column=7, sticky=(W))
        self.lb_receivedasview.grid(row=8, column=8, sticky=(W))
        self.lb_disease.grid(row=9, column=1, sticky=(W))
        self.lb_diseaseview.grid(row=9, column=2, sticky=(W))
        self.lb_diet.grid(row=9, column=7, sticky=(W))
        self.lb_dietview.grid(row=9, column=8, sticky=(W))
        self.lb_diagnosis.grid(row=10, column=1, sticky=(W))
        self.lb_diagnosisview.grid(row=10, column=2, sticky=(W))
        self.lb_seenby.grid(row=10, column=7, sticky=(W))
        self.lb_seenbyview.grid(row=10, column=8, sticky=(W))
        self.lb_ward.grid(row=11, column=1, sticky=(W))
        self.lb_wardview.grid(row=11, column=2, sticky=(W))
        self.lb_remarks.grid(row=11,column=7,sticky=(W))
        self.lb_remarksview.grid(row=11,column=8,sticky=(W))
        self.bt_exit.grid(row=13,column=8,sticky=(W))

        self.root.mainloop()
