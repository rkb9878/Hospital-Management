from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *
import datetime
from server import *
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import subprocess
import random
#-==================================global variable=========================================
dischargedate=""
dischargetime=""
nameofhospital=""
number=""
nameofpatient=""
dateofadmission=""
timeofadmission=""
ad=""
ward=""
relationship=""
rank=""
unit=""
age=""
sex=""
martial=""
service=""
arms=""
totalservice=""
formation=""
mobile=""
record=""
typeofad=""
diseasename=""

#-=================================================================
class discharge(Toplevel):
    #-==============================================slip2========================================
    def re(self):
        self.tf_injuryreportinitiatedon.delete(0, END)
        self.tf_dischargecategory.delete(0, END)
        self.tf_disposal.delete(0, END)
        self.tf_disposedas.delete(0, END)
        self.tf_document.delete(0,END)
        self.tf_medicalboardheld.delete(0,END)
        self.tf_medicalboarddue.delete(0,END)
        self.tf_medicalboarddescription.delete('1.0',END)
        self.tf_diagnosis.delete('1.0',END)
        self.tf_briefcasesummanry.delete('1.0',END)
        self.tf_instructiontopatient.delete('1.0',END)
    #--------------------------------Back------------------------------------------------------------
    def back(self):
        self.withdraw()
        self.root.deiconify()
    #----------------------------END back-------------------------------------------------------------
    def slip2(self,parent):
        global dischargedate
        global dischargetime
        global nameofhospital
        global number
        global nameofpatient
        global dateofadmission
        global timeofadmission
        global ad
        global ward
        global relationship
        global rank
        global unit
        global age
        global sex
        global martial
        global service
        global arms
        global totalservice
        global formation
        global mobile
        global record
        global typeofad
        global diseasename

        now = datetime.datetime.now()
        dischargedate = str(now.strftime("%y-%m-%d"))
        dischargetime = str(now.strftime("%H:%M:%S"))
        nameofhospital=self.tf_nameofhospital.get()
        number=self.tf_number.get()
        nameofpatient = self.cb_nameofpatient.get()
        dateofadmission=self.tf_dateofadmission.get()
        timeofadmission=self.tf_timeofadmission.get()
        ad=self.tf_ADno.get()
        ward=self.tf_dischargeward.get()
        relationship = self.tf_relationship.get()
        rank=self.tf_rank.get()
        unit=self.tf_unit.get()
        age=self.tf_age.get()
        sex=self.cb_sex.get()
        martial=self.cb_martialstatus.get()
        service=self.cb_service.get()
        arms=self.tf_type.get()
        totalservice=self.tf_totalservice.get()
        formation=self.tf_formation.get()
        mobile=self.tf_mobileno.get()
        record=self.tf_recordoffice.get()
        typeofad=self.tf_typeofadmission.get()
        diseasename=self.tf_disease.get()

        if nameofhospital=='' or ad=='' or number=='' or rank=='' or unit=='' or nameofpatient=='' or relationship=='' or age=='' or sex=='' or martial=='' or service=='' or arms=='' or totalservice=='' or formation==''or mobile=='' or record=='' or typeofad=='' or diseasename=='':
            field_flag=False
        else:
            field_flag=True

        if mobile!='':
            l=mobile.__len__()
            mobile_flag=False
            if l==10 and mobile.isdigit()==True:
                mobile_flag=True

        if age!='':
            age_flag=False
            if age.isdigit()==True:
                age_flag=True
        #--------------------------------------------used-Toplevel----------------------------------------------
        if field_flag==False:
            showerror("Message","Some fields are mandatory!!!!")
        else:
            # self.root2 = Toplevel(self.root)
            Toplevel.__init__(self, parent)
            self.transient(parent)
            self.parent = parent
            self.configure(background="snow")
            self.title("DISCHARGE SLIP")
            # self.state('zoomed')
            # self.resizable(0, 0)
            self.geometry("{0}x{0}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

            now=datetime.datetime.now()
            current_date = "Current Date: " + str(now.strftime("%d-%m-%Y"))
            current_time = "Current Time:" + str(now.strftime("%H-%M-%S"))
            #------------------------------------------Frame-----------------------------------------------------------
            self.f = Frame(self, bg="snow")
            self.f.pack()
            #-------------------------------------------end Frame----------------------------------------------------
            self.lb_header = Label(self.f, text="HOSPITAL DISCHARGE SLIP", bg="snow", fg="brown",font=("times new roman", 42, "bold", "underline"), pady=10)
            self.lb_header2 = Label(self.f, text="Discharge Page 2-2", bg="snow", fg="brown",font=("times new roman", 8, "bold",), pady=10)
            self.lb_injuryreportinitiatedon = Label(self.f, text="Injury Report Initiated On", bg="snow",font=("times new roman", 14), pady=10, padx=10)
            self.tf_injuryreportinitiatedon = Entry(self.f, width=45, font=("times new roman", 14), relief="solid")
            self.lb_dischargecategory = Label(self.f, text="Discharge in Medical category", bg="snow",font=("times new roman", 14), pady=10, padx=10)
            self.tf_dischargecategory = Entry(self.f, width=45, font=("times new roman", 14), relief="solid")
            self.lb_disposal = Label(self.f, text="Disposal", bg="snow",font=("times new roman", 14), pady=10, padx=10)
            self.tf_disposal = Entry(self.f, width=45, font=("times new roman", 14), relief="solid")
            self.lb_disposedas = Label(self.f, text="Disposed As", bg="snow", font=("times new roman", 14), pady=10, padx=10)
            self.tf_disposedas = Entry(self.f, width=45, font=("times new roman", 14), relief="solid")
            self.lb_document = Label(self.f, text="Any Other Document Initiated", bg="snow",font=("times new roman", 14), pady=10, padx=10)
            self.tf_document = Entry(self.f, width=45, font=("times new roman", 14), relief="solid")
            self.lb_medicalboardheld = Label(self.f, text="Medical Board Held On", bg="snow",font=("times new roman", 14), pady=10, padx=10)
            self.tf_medicalboardheld = Entry(self.f, width=45, font=("times new roman", 14), relief="solid")
            self.lb_medicalboarddue = Label(self.f, text="Medical Board Due On", bg="snow",font=("times new roman", 14), pady=10, padx=10)
            self.tf_medicalboarddue = Entry(self.f, width=45, font=("times new roman", 14), relief="solid")
            self.lb_medicalboarddescription = Label(self.f, text="Medical Board Description", bg="snow",font=("times new roman", 14), pady=10, padx=10)
            self.tf_medicalboarddescription = Text(self.f,height=5,width=57, font=("times new roman", 11), relief="solid")
            self.lb_diagnosis = Label(self.f, text="Diagnosis", bg="snow",font=("times new roman", 14), pady=10, padx=10)
            self.tf_diagnosis = Text(self.f,height=5,width=57, font=("times new roman", 11), relief="solid")
            self.lb_briefcasesummary = Label(self.f, text="Summary", bg="snow",font=("times new roman", 14), pady=10, padx=10)
            self.tf_briefcasesummary = Text(self.f,height=5,width=57,  font=("times new roman", 11), relief="solid")
            self.lb_instructiontopatient = Label(self.f, text="Instruction to Patient", bg="snow",font=("times new roman", 14), pady=10, padx=10)
            self.tf_instructiontopatient = Text(self.f, height=5,width=57, font=("times new roman", 11), relief="solid")

            self.bt_mainmenu = Button(self.f, text="<<BACK", font=("times new roman", 11, "bold"), fg="white",bg="red", activebackground="snow", activeforeground="brown", height=1, width=20,command=self.back)
            self.bt_proceed = Button(self.f, text="Print", font=("times new roman", 11, "bold"), fg="white", bg="green", activebackground="snow",activeforeground="brown", height=1, width=20,command=self.ins)
            self.bt_reset = Button(self.f, text="RESET", font=("times new roman", 11, "bold"), fg="white", bg="brown",activebackground="snow", activeforeground="brown", height=1, width=20,command=self.re)
            #------------------------------------------------------------------------------------
            self.lb_header.grid(row=0, column=1, columnspan=6)
            self.lb_header2.grid(row=0,column=6,columnspan=6,sticky=(E))
            self.lb_injuryreportinitiatedon.grid(row=3, column=1, sticky=(E))
            self.tf_injuryreportinitiatedon.grid(row=3, column=2)
            self.lb_dischargecategory.grid(row=3,column=5,sticky=(E))
            self.tf_dischargecategory.grid(row=3,column=6)
            self.lb_disposal.grid(row=4, column=1, sticky=(E))
            self.tf_disposal.grid(row=4, column=2)
            self.lb_disposedas.grid(row=4, column=5, sticky=(E))
            self.tf_disposedas.grid(row=4, column=6)
            self.lb_document.grid(row=5, column=1, sticky=(E))
            self.tf_document.grid(row=5, column=2)
            self.lb_medicalboardheld.grid(row=5,column=5,sticky=(E))
            self.tf_medicalboardheld.grid(row=5,column=6)
            self.lb_medicalboarddue.grid(row=6,column=1,sticky=(E))
            self.tf_medicalboarddue.grid(row=6,column=2)
            self.lb_medicalboarddescription.grid(row=7,column=1,sticky=(E))
            self.tf_medicalboarddescription.grid(row=7,column=2)
            self.lb_diagnosis.grid(row=7, column=5,sticky=(E))
            self.tf_diagnosis.grid(row=7, column=6)
            self.lb_briefcasesummary.grid(row=10,column=1,sticky=(E))
            self.tf_briefcasesummary.grid(row=10,column=2)
            self.lb_instructiontopatient.grid(row=10,column=5,sticky=(E))
            self.tf_instructiontopatient.grid(row=10,column=6,pady=15)
            self.bt_mainmenu.grid(row=16, column=0, columnspan=6, pady=20, sticky=(W))
            self.bt_reset.grid(row=16, column=2, columnspan=6, sticky=(W), padx=30)
            self.bt_proceed.grid(row=16, column=1, columnspan=6, pady=20, sticky=(E))

    #-===========================================slip2 end================================================

    #-==================================searching and fetching official data=============================
    def search2(self,event):
        self.tf_dateofadmission.delete(0, END)
        self.tf_timeofadmission.delete(0, END)
        self.tf_mobileno.delete(0, END)
        self.tf_ADno.delete(0, END)
        self.tf_dischargeward.delete(0, END)
        self.tf_formation.delete(0, END)
        self.tf_relationship.delete(0, END)
        self.tf_totalservice.delete(0, END)
        self.tf_relationship.delete(0, END)
        self.tf_type.delete(0, END)
        self.tf_ADno.delete(0, END)
        self.tf_age.delete(0, END)
        self.tf_unit.delete(0, END)
        self.tf_rank.delete(0, END)
        self.cb_martialstatus.set("")
        self.cb_service.set("")
        self.cb_sex.set("")
        self.tf_typeofadmission.delete(0, END)
        self.tf_recordoffice.delete(0, END)
        self.tf_disease.delete(0, END)
        dr = connection()
        query = "select adno,rank,unitwaddress,service,command,mobile,roffice,totals,arms from officialdata where number='" + self.tf_number.get() + "'"
        cr = dr.conn.cursor()
        cr.execute(query)
        result = cr.fetchone()
        if result:
            self.tf_ADno.insert(0, result[0])
            self.tf_rank.insert(0, result[1])
            self.tf_unit.insert(0, result[2])
            self.cb_service.set(result[3])
            self.tf_formation.insert(0, result[4])
            self.tf_mobileno.insert(0, result[5])
            self.tf_recordoffice.insert(0, result[6])
            self.tf_totalservice.insert(0, result[7])
            self.tf_type.insert(0, result[8])
            dr2 = connection()
            query2 = "select datetime,adddate,r_patient,sex,age,martial,ward,typead,disease from patientdata where number='" + self.tf_number.get() + "' and n_patient='"+self.cb_nameofpatient.get()+"'"
            cr2 = dr2.conn.cursor()
            cr2.execute(query2)
            result2 = cr2.fetchone()
            time=str(result2[0])
            time2=time.split(" ")[1:][0]
            self.tf_timeofadmission.insert(0,time2)
            self.tf_dateofadmission.insert(0,result2[1])
            self.tf_relationship.insert(0,result2[2])
            self.cb_sex.set(result2[3])
            self.tf_age.insert(0,result2[4])
            self.cb_martialstatus.set(result2[5])
            self.tf_dischargeward.insert(0,result2[6])
            self.tf_typeofadmission.insert(0,result2[7])
            self.tf_disease.insert(0,result2[8])
        else:
            showerror('Message','Record Not Found!!!!')
    def search(self):
        self.cb_nameofpatient.set("")
        dr = connection()
        query = "select n_patient from patientdata where number='" + self.tf_number.get() +"'and dischargedate is null"
        cr = dr.conn.cursor()
        cr.execute(query)
        result= cr.fetchall()
        if result:
            lst_name = []
            for i in range(0, len(result)):
                lst_name.append(result[i][0])
            self.cb_nameofpatient.config(values=tuple(lst_name))
            self.cb_nameofpatient.bind("<<ComboboxSelected>>", self.search2)
        else:
            showerror('Message','Record Not Found!!!!')
    #-=========================================START INSERTION QUERIES==========================================
    def ins(self):

        now = datetime.datetime.now()
        date2=str(datetime.datetime.now().date())
        date3=str(datetime.datetime.now().date())
        td = now.strftime("%Y-%m-%d %H:%M:%S")
        dr=connection()
        query="select * from `dischargedata` where number='"+number+"' and n_patient='"+nameofpatient+"' and dateofdischarge='"+dischargedate+"'"
        cr=dr.conn.cursor()
        cr.execute(query)
        dr.conn.commit()
        result=cr.fetchone()
        if result:
            showerror('Message','Patient has been already discharged on discharge date '+dischargedate)
        else:
            dr2 = connection()
            query2="INSERT INTO `dischargedata`(`number`, `dateofadmission`, `timeofadmission`, `dateofdischarge`, `timeofdischarge`, `n_patient`, `ward`, `injuryreport`, `medicalcategory`, `disposal`, `disposedas`, `documentinitiated`, `medicalboardheldon`,`medicalboarddueon`, `medicalboarddesc`, `diagnosis`, `summary`, `instructiontopatient`) VALUES ('"+number+"','"+dateofadmission+"','"+timeofadmission+"','"+dischargedate+"','"+dischargetime+"','"+nameofpatient+"','"+ward+"','"+self.tf_injuryreportinitiatedon.get()+"','"+self.tf_dischargecategory.get()+"','"+self.tf_disposal.get()+"','"+self.tf_disposedas.get()+"','"+self.tf_document.get()+"','"+self.tf_medicalboardheld.get()+"','"+self.tf_medicalboarddue.get()+"','"+self.tf_medicalboarddescription.get('1.0',END)+"','"+self.tf_diagnosis.get('1.0',END)+"','"+self.tf_briefcasesummary.get('1.0',END)+"','"+self.tf_instructiontopatient.get('1.0',END)+"')"
            cr2=dr2.conn.cursor()
            cr2.execute(query2)
            dr2.conn.commit()
            dr3=connection()
            query3="Update `patientdata` set dischargedate='"+td+"',disdate='"+dischargedate+"' where number='"+number+"'and n_patient='"+nameofpatient+"'"
            cr3=dr3.conn.cursor()
            cr3.execute(query3)
            dr3.conn.commit()

            showinfo("Message","Data Uploaded Successfully")
            file = str(number) + str(nameofpatient) + date3
            t = str("C:\pdf\discharge\\" + file + ".pdf")
            my_canvas = canvas.Canvas(t, pagesize=A4)
            # -=========================================================
            my_canvas.setLineWidth(.5)
            my_canvas.setFont('Helvetica', 15)
            my_canvas.drawString(240, 820, 'CONFIDENTIAL')
            my_canvas.line(240, 819, 350, 819)
            my_canvas.setLineWidth(1)
            my_canvas.setFont('Helvetica', 20)
            my_canvas.drawString(180, 800, 'Military Hospital,AMRITSAR')
            my_canvas.line(180, 796, 435, 796)
            my_canvas.setFont('Helvetica', 12)
            my_canvas.setLineWidth(.7)
            my_canvas.drawString(245, 785, 'DISCHARGE SLIP')
            my_canvas.line(50, 784, 580, 784)
            # -===================================DATA===========================
            my_canvas.setFont('Helvetica', 10)
            my_canvas.drawString(50, 765, 'Date of Admission')
            my_canvas.drawString(135, 765, '> '+str(dateofadmission)+' '+str(timeofadmission))
            my_canvas.drawString(300, 765, 'Date of Discharge ')
            my_canvas.drawString(390, 765, '> '+str(dischargedate)+' '+str(dischargetime))

            my_canvas.drawString(50, 755, 'A & D No')
            my_canvas.drawString(135, 755, '> '+str(ad))
            my_canvas.drawString(300, 755, 'Admission Ward')
            my_canvas.drawString(390, 755, '> '+str(ward))
            my_canvas.line(50, 753, 580, 753)
            # -=====================Patient==================================
            my_canvas.drawString(48, 743, '01. Patient Name')
            my_canvas.drawString(135, 743, '> '+str(nameofpatient))
            my_canvas.drawString(300, 743, '02. Relation')
            my_canvas.drawString(390, 743, '> '+str(relationship))

            my_canvas.drawString(48, 733, '03. Age')
            my_canvas.drawString(135, 733, '> '+str(age))
            my_canvas.drawString(300, 733, '04. Marital Status')
            my_canvas.drawString(390, 733, '> '+str(martial))

            my_canvas.drawString(48, 723, '05. Service')
            my_canvas.drawString(135, 723, '> '+str(service))
            my_canvas.drawString(300, 723, '06. Rank')
            my_canvas.drawString(390, 723, '> '+str(rank))

            # my_canvas.drawString(48, 715, '07. Category')
            # my_canvas.drawString(135, 715, '> ')
            # my_canvas.drawString(300, 715, '08. Rank')
            # my_canvas.drawString(390, 715, '> '+str(rank))

            my_canvas.drawString(48, 703, '07. Sex')
            my_canvas.drawString(135, 703, '> '+str(sex))

            my_canvas.drawString(48, 693, '08. Total Service')
            my_canvas.drawString(135, 693, '> '+str(totalservice))
            my_canvas.drawString(300, 693, '09. Trade')
            my_canvas.drawString(390, 693, '> '+str(arms))

            my_canvas.drawString(48, 683, '10. Personnel Unit')
            my_canvas.drawString(135, 683, '> '+str(unit))
            my_canvas.drawString(300, 683, '11. Formation')
            my_canvas.drawString(390, 683, '> '+str(formation))

            my_canvas.drawString(48, 673, '12. Arms/Corps')
            my_canvas.drawString(135, 673, '> '+str(arms))
            my_canvas.drawString(300, 673, '13. Record Office')
            my_canvas.drawString(390, 673, '> '+str(record))
            my_canvas.line(50, 670, 580, 670)

            my_canvas.drawString(48, 660, '14. Injury Report')
            my_canvas.drawString(240, 660, '> '+str(self.tf_injuryreportinitiatedon.get()))

            my_canvas.drawString(48, 650, '15. Discharge in Med category(S.H.A.P.E)')
            my_canvas.drawString(240, 650, '> '+str(self.tf_dischargecategory.get()))

            my_canvas.drawString(48, 640, '16. Disposal')
            my_canvas.drawString(240, 640, '> '+str(self.tf_disposal.get()))

            my_canvas.drawString(48, 630, '17. Disposed As')
            my_canvas.drawString(240, 630, '> '+str(self.tf_disposedas.get()))

            my_canvas.drawString(48, 620, '18. Any other document initiated')
            my_canvas.drawString(240, 620, '> '+str(self.tf_document.get()))

            my_canvas.drawString(48, 610, '19. Medical board held on')
            my_canvas.drawString(240, 610, '> '+str(self.tf_medicalboardheld.get()))

            my_canvas.drawString(48, 600, '20. Medical board due on')
            my_canvas.drawString(240, 600, '>'+str(self.tf_medicalboarddue.get()))

            my_canvas.drawString(48, 590, '21. Medical board description')
            x = 240
            y = 590
            dis = self.tf_medicalboarddescription.get('1.0',END)
            tf = dis.split('\n')
            for i in range(0, len(tf) - 1):
                my_canvas.drawString(x, y, '> ')
                my_canvas.drawString(x + 20, y, tf[i])
                y = y - 10
            y=y-10
            my_canvas.drawString(48, y, '22. Diagnosis')
            dis=self.tf_diagnosis.get('1.0',END)
            tf_diagnosis = dis.split('\n')
            for i in range(0, len(tf_diagnosis) - 1):
                my_canvas.drawString(x, y, '> ')
                my_canvas.drawString(x + 20, y, tf_diagnosis[i])
                y = y - 10
            y=y-10
            my_canvas.drawString(48, y, '23. Brief Case Summary')
            b=self.tf_briefcasesummary.get('1.0',END)
            tf_briefcasesummary = b.split('\n')
            for i in range(0, len(tf_briefcasesummary) - 1):
                my_canvas.drawString(x, y, '> ')
                my_canvas.drawString(x + 20, y, tf_briefcasesummary[i])
                y = y - 10
            y=y-10
            my_canvas.drawString(48, y, '24. Instruction to Patient')
            inj=self.tf_instructiontopatient.get('1.0',END)
            tf_instructiontopatient = inj.split('\n')
            for i in range(0, len(tf_instructiontopatient) - 1):
                my_canvas.drawString(x, y, '>')
                my_canvas.drawString(x + 20, y, tf_instructiontopatient[i])
                y = y - 10
            y=y-10
            my_canvas.setFont('Helvetica', 11)
            my_canvas.drawString(48, 103, 'Date')
            my_canvas.drawString(480, 103, 'signature')
            my_canvas.line(50, 100, 580, 100)

            # -=======================================================
            my_canvas.save()
            subprocess.Popen([t], shell=True)
            self.root.destroy()
    #-===========================================END INSERT Query=================================================
#-=======================================================slip1=====================================================
    def reset(self):
        self.tf_number.delete(0, END)
        self.cb_nameofpatient.set("")
        self.tf_dateofadmission.delete(0, END)
        self.tf_timeofadmission.delete(0, END)
        self.tf_mobileno.delete(0, END)
        self.tf_ADno.delete(0, END)
        self.tf_dischargeward.delete(0, END)
        self.tf_formation.delete(0, END)
        self.tf_relationship.delete(0, END)
        self.tf_totalservice.delete(0,END)
        self.tf_relationship.delete(0, END)
        self.tf_type.delete(0,END)
        self.cb_nameofpatient.set("")
        self.tf_ADno.delete(0, END)
        self.tf_age.delete(0, END)
        self.tf_unit.delete(0, END)
        self.tf_number.delete(0, END)
        self.tf_rank.delete(0,END)
        self.cb_martialstatus.set("")
        self.cb_service.set("")
        self.cb_sex.set("")
        self.tf_typeofadmission.delete(0,END)
        self.tf_recordoffice.delete(0,END)
        self.tf_disease.delete(0,END)

    def __init__(self,parent):
        # self.root = Tk()
        self.root = Toplevel(parent)
        self.root.transient(parent)
        self.root.parent = parent
        self.root.configure(background="snow")
        self.root.title("DISCHARGE SLIP")
        self.root.iconbitmap(self,default="MH.ico")
        # self.root.state('zoomed')
        # self.root.resizable(0, 0)
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        now = datetime.datetime.now()
        current_date ="Discharge Date: "+str(now.strftime("%d-%m-%Y"))
        current_time= "Discharge Time:"+str(now.strftime("%H-%M-%S"))
        #-----------------------------------Frame--------------------------------------
        self.f = Frame(self.root, bg="snow")
        self.f.pack()
        #-----------------------------------end Frame---------------------------------
        self.lb_header = Label(self.f, text="HOSPITAL DISCHARGE SLIP", bg="snow", fg="brown",font=("times new roman", 42, "bold", "underline"), pady=10)
        self.lb_header2=Label(self.f,text="Discharge Page 1-2",bg="snow",fg="brown",font=("times new roman",8), pady=10)
        self.lb_showdate=Label(self.f,text=current_date,bg="snow",fg="brown",font=("times new roman",14, "bold"), pady=10)
        self.lb_showtime=Label(self.f,text=current_time,bg="snow",fg="brown",font=("times new roman",14,"bold"), pady=10)
        now=datetime.datetime.now()
        current_time = "Discharge Time: " + str(now.strftime("%H-%M-%S"))
        self.lb_showtime.config(text=current_time)
        self.lb_nameofhospital = Label(self.f, text="Name of Hospital", bg="snow", font=("times new roman", 14),padx=10)
        self.tf_nameofhospital = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.tf_nameofhospital.insert(0,"Military Hospital,Amritsar")
        self.lb_number = Label(self.f, text="Number", bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.tf_number = Entry(self.f, width=30, font=("times new roman", 14), relief="solid")
        self.bt_search=Button(self.f, text="Search", font=("times new roman", 11, "bold"), fg="white", bg="#89d0ce",activebackground="snow", activeforeground="brown", height=1, width=15,command=self.search)
        self.lb_nameofpatient = Label(self.f, text="Name of Patient", bg="snow", font=("times new roman", 14), padx=10,pady=10)
        self.cb_nameofpatient = Combobox(self.f, width=48, font=("times new roman", 14),state='readonly')
        self.lb_dateofadmission=Label(self.f, text="Date of Admission", bg="snow", font=("times new roman", 14), padx=10,pady=10)
        self.tf_dateofadmission=Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_timeofadmission=Label(self.f, text="Time of Admission", bg="snow", font=("times new roman", 14), padx=10,pady=10)
        self.tf_timeofadmission=Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_ADno = Label(self.f, text="A & D Nos.", bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.tf_ADno = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_dischargeward=Label(self.f, text="Discharge Ward", bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.tf_dischargeward=Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_relationship = Label(self.f, text="Relationship with Patient", bg="snow", font=("times new roman", 14),padx=10, pady=10)
        self.tf_relationship = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_rank = Label(self.f, text="Rank", bg="snow", font=("times new roman", 14), padx=20,pady=10)
        self.tf_rank = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_unit = Label(self.f, text="Unit/Ship with address", bg="snow", font=("times new roman", 14),padx=10,pady=10)
        self.tf_unit = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_age = Label(self.f, text="Age/Sex", bg="snow", font=("times new roman", 14), pady=10,padx=10)
        self.tf_age = Entry(self.f, width=25, font=("times new roman", 14), relief="solid")
        self.cb_sex=Combobox(self.f,width=20,values=('Male','Female','Others'),state="readonly",font=("times new roman",14))
        self.lb_martialstatus = Label(self.f, text="Marital Status", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.cb_martialstatus = Combobox(self.f, width=48, font=("times new roman", 14),values=('Single','Married'),state='readonly')
        self.lb_service = Label(self.f, text="Service", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.cb_service = Combobox(self.f, width=48, font=("times new roman", 14),values=('Army','Navy','Air Force'),state='readonly')
        self.lb_type = Label(self.f, text="Arms/Corps/Branch/Trade", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.tf_type = Entry(self.f, width=50, font=("times new roman", 14),relief="solid")
        self.lb_totalservice = Label(self.f, text="Total Service", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.tf_totalservice = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_formation = Label(self.f, text="Formation/Command", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.tf_formation = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_mobileno = Label(self.f, text="Mobile Number", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.tf_mobileno = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_recordoffice = Label(self.f, text="Record Office", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.tf_recordoffice = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_typeofadmission=Label(self.f,text="Type Of Admission",bg="snow",font=("times new roman", 14), pady=10, padx=10)
        self.tf_typeofadmission = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_disease = Label(self.f, text="Disease Name", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.tf_disease = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")

        #------------------------------------------------Button----------------------------------
        self.bt_mainmenu = Button(self.f, text="MAIN MENU", font=("times new roman", 11, "bold"), fg="white", bg="#f9d591",activebackground="snow", activeforeground="brown", height=1, width=20,command=lambda :self.root.destroy())
        self.bt_proceed = Button(self.f, text="PROCEED>>", font=("times new roman", 11, "bold"), fg="white", bg="green",activebackground="#F0E68C", activeforeground="white", height=1, width=20,command=lambda :self.slip2(self.root))
        self.bt_reset = Button(self.f, text="RESET", font=("times new roman", 11, "bold"), fg="white", bg="brown",activebackground="snow", activeforeground="brown", height=1, width=20,command=self.reset)
        #-----------------------------------------------end  Button---------------------------------------------------------------------
        self.lb_header.grid(row=0, column=1, columnspan=6)
        self.lb_header2.grid(row=0, column=6,sticky=(E))
        self.lb_showdate.grid(row=1,column=2,sticky=(W))
        self.lb_showtime.grid(row=1,column=6,sticky=(W))
        self.lb_nameofhospital.grid(row=2, column=1,sticky=(E))
        self.tf_nameofhospital.grid(row=2, column=2)
        self.lb_number.grid(row=2, column=5, sticky=(E))
        self.tf_number.grid(row=2, column=6,sticky=(W))
        self.bt_search.grid(row=2,column=6,sticky=(E))
        self.lb_nameofpatient.grid(row=3,column=1,sticky=(E))
        self.cb_nameofpatient.grid(row=3,column=2,sticky=(W))
        self.lb_dateofadmission.grid(row=3,column=5,sticky=(E))
        self.tf_dateofadmission.grid(row=3,column=6)
        self.lb_timeofadmission.grid(row=4, column=1, sticky=(E))
        self.tf_timeofadmission.grid(row=4, column=2)
        self.lb_ADno.grid(row=4, column=5,sticky=(E))
        self.tf_ADno.grid(row=4, column=6)
        self.lb_dischargeward.grid(row=5,column=1,sticky=(E))
        self.tf_dischargeward.grid(row=5,column=2)
        self.lb_relationship.grid(row=5, column=5, sticky=(E))
        self.tf_relationship.grid(row=5, column=6)
        self.lb_rank.grid(row=6, column=1,sticky=(E))
        self.tf_rank.grid(row=6, column=2)
        self.lb_unit.grid(row=6, column=5,sticky=(E))
        self.tf_unit.grid(row=6, column=6)
        self.lb_age.grid(row=7, column=1,sticky=(E))
        self.tf_age.grid(row=7, column=2,sticky=(W))
        self.cb_sex.grid(row=7,column=2,sticky=(E))
        self.lb_martialstatus.grid(row=7, column=5,sticky=(E))
        self.cb_martialstatus.grid(row=7, column=6)
        self.lb_service.grid(row=8, column=1,sticky=(E))
        self.cb_service.grid(row=8, column=2)
        self.lb_type.grid(row=8, column=5,sticky=(E))
        self.tf_type.grid(row=8, column=6)
        self.lb_totalservice.grid(row=9, column=1,sticky=(E))
        self.tf_totalservice.grid(row=9, column=2)
        self.lb_formation.grid(row=9, column=5,sticky=(E))
        self.tf_formation.grid(row=9, column=6)
        self.lb_mobileno.grid(row=10, column=1,sticky=(E))
        self.tf_mobileno.grid(row=10, column=2)
        self.lb_recordoffice.grid(row=10, column=5,sticky=(E))
        self.tf_recordoffice.grid(row=10, column=6)
        self.lb_typeofadmission.grid(row=11,column=1,sticky=(E))
        self.tf_typeofadmission.grid(row=11,column=2)
        self.lb_disease.grid(row=11,column=5,sticky=(E))
        self.tf_disease.grid(row=11,column=6)
        self.bt_mainmenu.grid(row=16,column=0,columnspan=6,pady=20,sticky=(W))
        self.bt_reset.grid(row=16,column=2,columnspan=6,sticky=(W),padx=50)
        self.bt_proceed.grid(row=16, column=1, columnspan=6, pady=20,sticky=(E))
        # self.root.mainloop()
        self.result = None

# discharge()