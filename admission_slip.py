from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *
import datetime
from server import *
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import subprocess
#-==================================global variable=========================================
nameofhospital=""
ad=""
number=""
rank=""
name=""
unit=""
nameofpatient=""
relationship=""
age=""
sex=""
martial=""
service=""
arms=""
totalservice=""
religion=""
station=""
formation=""
nextofkin=""
kinrelationship=""
mobile=""
cda=""
record=""
addrecord=""
area=""
post=""
city=""
state=""
pin=""
icd=""
ab64=""

#-=================================================================
class admission(Toplevel):
    #-==============================================slip2========================================
    def re(self):
        self.tf_pincode.delete(0, END)
        self.tf_state.delete(0, END)
        self.tf_area.delete(0, END)
        self.tf_city.delete(0, END)
        self.cb_typeofadmission.set("")
        self.tf_details.delete(0,END)
        self.tf_disease.delete(0,END)
        self.tf_icd.delete(0,END)
        self.tf_diet.delete(0,END)
        self.cb_receivedas.set("")
        self.tf_diagnosis.delete(0,END)
        self.tf_seenby.delete(0,END)
        self.tf_ward.delete(0,END)
        self.tf_remarks.delete(0,END)
        self.tf_post.delete(0,END)
        self.tf_ab64.delete(0,END)
    #--------------------------------Back------------------------------------------------------------
    def back(self):
        self.withdraw()
        self.win.deiconify()
    #----------------------------END back-------------------------------------------------------------
    def slip2(self,parent):
        global nameofhospital
        global ad
        global number
        global rank
        global name
        global unit
        global nameofpatient
        global relationship
        global age
        global sex
        global martial
        global service
        global arms
        global totalservice
        global religion
        global station
        global formation
        global nextofkin
        global kinrelationship
        global mobile
        global cda
        global record
        global addrecord

        nameofhospital=self.tf_nameofhospital.get()
        ad=self.tf_ADno.get()
        number=self.tf_number.get()
        rank=self.tf_rank.get()
        name=self.tf_name.get()
        unit=self.tf_unit.get()
        nameofpatient=self.tf_nameofpatient.get()
        relationship=self.tf_relationship.get()
        age=self.tf_age.get()
        sex=self.cb_sex.get()
        martial=self.cb_martialstatus.get()
        service=self.cb_service.get()
        arms=self.tf_type.get()
        totalservice=self.tf_totalservice.get()
        religion=self.tf_religion.get()
        station=self.tf_station.get()
        formation=self.tf_formation.get()
        nextofkin=self.tf_nextofkin.get()
        kinrelationship=self.tf_kinrelationship.get()
        mobile=self.tf_mobileno.get()
        cda=self.tf_cda.get()
        record=self.tf_recordoffice.get()
        addrecord=self.tf_recordofficeaddress.get()
        if nameofhospital=='' or ad=='' or number=='' or rank=='' or name=='' or unit=='' or nameofpatient=='' or relationship=='' or age=='' or sex=='' or martial=='' or service=='' or arms=='' or totalservice=='' or religion=='' or station=='' or formation=='' or nextofkin=='' or kinrelationship=='' or mobile=='' or cda=='' or record=='' or addrecord=='':
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
        elif field_flag==True and mobile_flag==False:
            showerror("Message","Mobile number is Invalid!!!!")
        elif field_flag==True and mobile_flag==True and age_flag==False:
            showerror("Message","Entered age is Invalid!!!!")
        else:
            # self.root2 = Toplevel(self.root)
            Toplevel.__init__(self, parent)
            self.transient(parent)
            self.parent = parent
            self.configure(background="snow")
            self.title("ADMISSION SLIP")
            self.geometry("{0}x{0}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
            now=datetime.datetime.now()
            current_date = "Current Date: " + str(now.strftime("%d-%m-%Y"))
            current_time = "Current Time:" + str(now.strftime("%H-%M-%S"))
            scrollbar=Scrollbar(self)
            scrollbar.pack(side=RIGHT,fill=Y)
            #------------------------------------------Frame-----------------------------------------------------------
            self.f = Frame(self, bg="snow")
            self.f.pack()
            #-------------------------------------------end Frame----------------------------------------------------

            self.lb_header = Label(self.f, text="HOSPITAL ADMISSION SLIP", bg="snow", fg="brown",font=("times new roman", 42, "bold", "underline"), pady=10)
            self.lb_header2 = Label(self.f, text="Admission Page 2-2", bg="snow", fg="brown",font=("times new roman", 8, "bold",), pady=10)
            self.lb_headeraddress = Label(self.f, text="Address:", bg="snow", font=("times new roman", 15,"underline"), pady=10)
            self.lb_area = Label(self.f, text="Street/Area/Locality", bg="snow", font=("times new roman", 14), pady=10,padx=10)
            self.tf_area = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
            self.tf_area.insert(0,area)
            self.lb_post=Label(self.f,text="Post Office",bg="snow",font=("times new roman",14),pady=10,padx=10)
            self.tf_post=Entry(self.f,width=50,font=("times new roman",14),relief="solid")
            self.tf_post.insert(0,post)
            self.lb_city = Label(self.f, text="City", bg="snow", font=("times new roman", 14), pady=10, padx=10)
            self.tf_city = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
            self.tf_city.insert(0, city)
            self.lb_state = Label(self.f, text="State", bg="snow", font=("times new roman", 14), pady=10, padx=10)
            self.tf_state = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
            self.tf_state.insert(0,state)
            self.lb_pincode = Label(self.f, text="Pin Code", bg="snow", font=("times new roman", 14), pady=10, padx=10)
            self.tf_pincode = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
            self.tf_pincode.insert(0,pin)
            self.lb_typeofadmission = Label(self.f, text="Type of Admission", bg="snow", font=("times new roman", 14),pady=10, padx=10)
            self.cb_typeofadmission = Combobox(self.f, width=48, font=("times new roman", 14),values=('Recat', 'Reassessment Medical Board', 'Direct', 'Transfer in from'),state='readonly')
            self.lb_details = Label(self.f, text="Transferred From", bg="snow", font=("times new roman", 14), pady=10, padx=10)
            self.tf_details = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
            self.tf_details.insert(0,'N/A')
            self.lb_ab64 = Label(self.f, text="AB 64 Available", bg="snow", font=("times new roman", 14), pady=10,padx=10)
            self.tf_ab64 = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
            if ab64!='':
                self.tf_ab64.insert(0,ab64)
            else:
                self.tf_ab64.insert(0,'N/A')
            self.lb_disease = Label(self.f, text="Disease Name", bg="snow", font=("times new roman", 14), pady=10, padx=10)
            self.tf_disease = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
            self.lb_icd = Label(self.f, text="ICD Code", bg="snow", font=("times new roman", 14), pady=10, padx=10)
            self.tf_icd = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
            if icd!='':
                self.tf_icd.insert(0,icd)
            else:
                self.tf_icd.insert(0, 'N/A')
            self.lb_diet = Label(self.f, text="Diet", bg="snow", font=("times new roman", 14), pady=10, padx=10)
            self.tf_diet = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
            self.lb_receivedas = Label(self.f, text="Received as", bg="snow", font=("times new roman", 14), pady=10,padx=10)
            self.cb_receivedas = Combobox(self.f, width=48, font=("times new roman", 14),values=('Walking', 'Sitting', 'Lying'), state='readonly')
            self.lb_diagnosis = Label(self.f, text="Provisional Diagnosis", bg="snow", font=("times new roman", 14),pady=10, padx=10)
            self.tf_diagnosis = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
            self.tf_diagnosis.insert(0, "N/A")
            self.lb_seenby = Label(self.f, text="Seen on arrival by", bg="snow", font=("times new roman", 14), pady=10,padx=10)
            self.tf_seenby = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
            self.lb_ward = Label(self.f, text="Sent to Ward", bg="snow", font=("times new roman", 14), pady=10, padx=10)
            self.tf_ward = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
            self.lb_remarks = Label(self.f, text="Remarks", bg="snow", font=("times new roman", 14), pady=10, padx=10)
            self.tf_remarks = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
            self.tf_remarks.insert(0, "N/A")
            self.bt_mainmenu = Button(self.f, text="<<BACK", font=("times new roman", 11, "bold"), fg="white",bg="red", activebackground="snow", activeforeground="brown", height=1, width=20,command=self.back)
            self.bt_proceed = Button(self.f, text="Print", font=("times new roman", 11, "bold"), fg="white", bg="green", activebackground="snow",activeforeground="brown", height=1, width=20,command=self.ins)
            self.bt_reset = Button(self.f, text="RESET", font=("times new roman", 11, "bold"), fg="white", bg="brown",activebackground="snow", activeforeground="brown", height=1, width=20,command=self.re)
            #------------------------------------------------------------------------------------
            self.lb_header.grid(row=0, column=1, columnspan=6)
            self.lb_header2.grid(row=0,column=6,columnspan=6,sticky=(E))
            self.lb_headeraddress.grid(row=2, column=1, sticky=(E))
            self.lb_area.grid(row=3, column=1, sticky=(E))
            self.tf_area.grid(row=3, column=2)
            self.lb_post.grid(row=3,column=5,sticky=(E))
            self.tf_post.grid(row=3,column=6)
            self.lb_city.grid(row=4, column=1, sticky=(E))
            self.tf_city.grid(row=4, column=2)
            self.lb_state.grid(row=4, column=5, sticky=(E))
            self.tf_state.grid(row=4, column=6)
            self.lb_pincode.grid(row=5, column=1, sticky=(E))
            self.tf_pincode.grid(row=5, column=2)
            self.lb_ab64.grid(row=6,column=1,sticky=(E))
            self.tf_ab64.grid(row=6,column=2)
            self.lb_typeofadmission.grid(row=6,column=5,sticky=(E))
            self.cb_typeofadmission.grid(row=6,column=6)
            self.lb_details.grid(row=7,column=1,sticky=(E))
            self.tf_details.grid(row=7,column=2)
            self.lb_disease.grid(row=7, column=5,sticky=(E))
            self.tf_disease.grid(row=7, column=6)
            self.lb_icd.grid(row=8,column=1,sticky=(E))
            self.tf_icd.grid(row=8,column=2)
            self.lb_diet.grid(row=8,column=5,sticky=(E))
            self.tf_diet.grid(row=8,column=6)
            self.lb_receivedas.grid(row=9, column=1,sticky=(E))
            self.cb_receivedas.grid(row=9, column=2)
            self.lb_diagnosis.grid(row=9, column=5,sticky=(E))
            self.tf_diagnosis.grid(row=9, column=6)
            self.lb_seenby.grid(row=10,column=1,sticky=(E))
            self.tf_seenby.grid(row=10, column=2)
            self.lb_ward.grid(row=10,column=5,sticky=(E))
            self.tf_ward.grid(row=10, column=6)
            self.lb_remarks.grid(row=11, column=1,sticky=(E))
            self.tf_remarks.grid(row=11, column=2)
            self.bt_mainmenu.grid(row=16, column=0, columnspan=6, pady=20, sticky=(W))
            self.bt_reset.grid(row=16, column=2, columnspan=6, sticky=(W), padx=30)
            self.bt_proceed.grid(row=16, column=1, columnspan=6, pady=20, sticky=(E))
            self.result = None

    #-===========================================slip2 end================================================

    #-==================================searching and fetching official data=============================
    def search(self):
        global area
        global post
        global city
        global state
        global pin
        global icd
        global ab64
        self.tf_ADno.delete(0,END)
        self.tf_rank.delete(0, END)
        self.tf_name.delete(0, END)
        self.tf_unit.delete(0, END)
        self.cb_service.set('')
        self.tf_station.delete(0, END)
        self.tf_formation.delete(0,END)
        self.tf_nextofkin.delete(0, END)
        self.tf_kinrelationship.delete(0, END)
        self.tf_mobileno.delete(0, END)
        self.tf_cda.delete(0,END)
        self.tf_recordoffice.delete(0, END)
        self.tf_recordofficeaddress.delete(0, END)
        self.tf_totalservice.delete(0, END)
        self.tf_type.delete(0,END)
        area = ''
        post = ''
        city = ''
        state = ''
        pin = ''
        icd = ''
        ab64 = ''
        dr=connection()
        query="select * from officialdata where number='"+self.tf_number.get()+"'"
        cr=dr.conn.cursor()
        cr.execute(query)
        result=cr.fetchone()
        if result:
            self.tf_ADno.insert(0,result[2])
            self.tf_rank.insert(0,result[3])
            self.tf_name.insert(0, result[4])
            self.tf_unit.insert(0,result[5])
            self.cb_service.set(result[6])
            self.tf_station.insert(0,result[7])
            self.tf_formation.insert(0,result[8])
            self.tf_nextofkin.insert(0,result[9])
            self.tf_kinrelationship.insert(0,result[10])
            self.tf_mobileno.insert(0,result[11])
            self.tf_cda.insert(0,result[12])
            self.tf_recordoffice.insert(0,result[13])
            self.tf_recordofficeaddress.insert(0,result[14])
            self.tf_totalservice.insert(0,result[15])
            self.tf_type.insert(0,result[16])
            area=result[17]
            post=result[18]
            city=result[19]
            state=result[20]
            pin=result[21]
            icd=result[22]
            ab64=result[23]
        else:
            showerror('Message','Record Not Found!!!!')
    #-=========================================START INSERTION QUERIES==========================================
    def ins(self):

        now = datetime.datetime.now()
        date2=str(datetime.datetime.now().date())
        td = now.strftime("%Y-%m-%d %H:%M")
        dr4=connection()
        query="select * from patientdata where number='"+number+"' and n_patient='"+nameofpatient+"' and adddate='"+date2+"'"
        cr4=dr4.conn.cursor()
        cr4.execute(query)
        result=cr4.fetchone()
        if result!=None:
            showerror("Message","Patient already admitted today!!!!")
        else:
            field_flag=False
            dr = connection()
            query1 = "INSERT INTO `patientdata`( `number`,`datetime`,`dischargedate`,`adddate`,`disdate`,`h_name`, `n_patient`, `r_patient`, `sex`, `age`, `martial`, `religion`,`typead`, `transfer`,`disease`,`diet`,`received`,`diagnosis`,`seenby`,`ward`,`remarks`) VALUES ('" + number + "','" + td + "',NULL,'"+date2+"',NULL,'" +nameofhospital + "','" + nameofpatient + "','" + relationship + "','" + sex + "','" + age + "','" + martial + "','" + religion + "','" + self.cb_typeofadmission.get() + "','" + self.tf_details.get() + "','" + self.tf_disease.get() + "','" + self.tf_diet.get() + "','" + self.cb_receivedas.get() + "','" + self.tf_diagnosis.get() + "','" + self.tf_seenby.get() + "','" + self.tf_ward.get() + "','" + self.tf_remarks.get() + "');"
            cr = dr.conn.cursor()
            cr.execute(query1)
            dr.conn.commit()
            showinfo("Message", "Data Uploaded Successfully")
            field_flag=True

        dr2=connection()
        query2="select * from officialdata where number='"+number+"'"
        cr2=dr2.conn.cursor()
        cr2.execute(query2)
        res=cr2.fetchone()
        if res==None:
            dr3=connection()
            query3= "INSERT INTO `officialdata`( `number`, `h_name`, `adno`, `rank`, `name`, `unitwaddress`,  `service`,  `station`, `command`, `nkin`, `relation`, `mobile`, `cdano`, `roffice`, `addroffice`, `totals`, `arms`, `area`,`post`, `city`, `state`, `pin`,`icd`, `ab64`) VALUES ('" + number + "','" + nameofhospital + "','" + self.tf_ADno.get() + "','" + rank + "','" + name+ "','" + unit+ "','"  + service+ "','" +station + "','" + formation + "','" + nextofkin + "','" + kinrelationship + "','" + mobile + "','" + cda + "','" + record + "','" + addrecord + "','" +totalservice + "','" + arms+"','"+self.tf_area.get()+"','"+self.tf_post.get()+"','"+self.tf_city.get()+"','"+self.tf_state.get()+"','"+self.tf_pincode.get()+"','"+self.tf_icd.get()+"','"+self.tf_ab64.get()+"');"
            ccr = dr3.conn.cursor()
            ccr.execute(query3)
            dr3.conn.commit()

            #---------------------printing slip------------------------------------------------------------
        if field_flag==True:
            file=str(number)+str(nameofpatient)+date2
            t = str("C:\pdf\Admission\\"+file+ ".pdf")
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
            my_canvas.drawString(245, 785, 'ADMISSION SLIP')
            my_canvas.line(50, 784, 580, 784)
                # -===================================DATA===========================
            my_canvas.setFont('Helvetica', 9)
            my_canvas.drawString(50, 765, 'Number')
            my_canvas.drawString(135, 765, '> '+str(number))
            my_canvas.drawString(300, 765, 'Date of Admission')
            my_canvas.drawString(390, 765, '> '+str(td))

            my_canvas.drawString(50, 755, 'A & D No')
            my_canvas.drawString(135, 755, '> '+str(ad))
            my_canvas.drawString(300, 755, 'Admission Ward')
            my_canvas.drawString(390, 755, '> '+str(self.tf_ward.get()))
            my_canvas.line(50, 753, 580, 753)
            # -=====================Patient==================================
            my_canvas.drawString(48, 745, '01. Patient Name')
            my_canvas.drawString(135, 745, '> '+str(nameofpatient))
            my_canvas.drawString(300, 745, '02. Relation')
            my_canvas.drawString(390, 745, '> '+str(religion))

            my_canvas.drawString(48, 735, '03. Age')
            my_canvas.drawString(135, 735, '> '+str(age))
            my_canvas.drawString(300, 735, '04. Marital Status')
            my_canvas.drawString(390, 735, '> '+str(martial))

            my_canvas.drawString(48, 725, '05. Service')
            my_canvas.drawString(135, 725, '> '+str(service))
            my_canvas.drawString(300, 725, '06. Rank')
            my_canvas.drawString(390, 725, '> '+str(rank))

            # my_canvas.drawString(48, 715, '07. Category')
            # my_canvas.drawString(135, 715, '> ')
            # my_canvas.drawString(300, 715, '07. Rank')
            # my_canvas.drawString(390, 715, '> '+str(rank))

            my_canvas.drawString(48, 705, '07. Sex')
            my_canvas.drawString(135, 705, '> '+str(sex))

            my_canvas.drawString(48, 695, '08. Total Service')
            my_canvas.drawString(135, 695, '> '+str(totalservice))
            my_canvas.drawString(300, 695, '09. Trade')
            my_canvas.drawString(390, 695, '> '+str(arms))

            my_canvas.drawString(48, 685, '10. Unit/Ship')
            my_canvas.drawString(135, 685, '> '+str(unit))
            my_canvas.drawString(300, 685, '11. Formation')
            my_canvas.drawString(390, 685, '> '+str(formation))

            my_canvas.drawString(48, 675, '12. Arms/Corps')
            my_canvas.drawString(135, 675, '> '+str(arms))
            my_canvas.drawString(300, 675, '13. Record Office')
            my_canvas.drawString(390, 675, '> '+str(record))

            my_canvas.drawString(48, 665, '14. Religion')
            my_canvas.drawString(135, 665, '> '+str(religion))
            my_canvas.drawString(300, 665, '15. Station')
            my_canvas.drawString(390, 665, '> '+str(station))

            my_canvas.drawString(48, 655, '16. State')
            my_canvas.drawString(135, 655, '> '+str(self.tf_state.get()))
            my_canvas.drawString(300, 655, '17. CDA No')
            my_canvas.drawString(390, 655, '> '+str(cda))

            # my_canvas.drawString(48, 645, '20. District Origin')
            # my_canvas.drawString(135, 645, '> ')
            # my_canvas.drawString(300, 645, '21. State')
            # my_canvas.drawString(390, 645, "")

            my_canvas.drawString(48, 635, '18. Next of Kin')
            my_canvas.line(50, 633, 580, 633)
            my_canvas.drawString(50, 625, 'Name')
            my_canvas.drawString(135, 625, '> '+str(nextofkin))
            my_canvas.drawString(300, 625, 'Relation')
            my_canvas.drawString(390, 625, '> '+str(kinrelationship))
            my_canvas.drawString(50, 615, 'Post Office')
            my_canvas.drawString(390, 615, '> '+str(self.tf_post.get()))
            my_canvas.drawString(300, 615, 'Pin Code')
            my_canvas.drawString(135, 615, '> ' + str(self.tf_pincode.get()))
            my_canvas.drawString(50, 605, 'Ph Number')
            my_canvas.drawString(135, 605, '> '+str(mobile))
            my_canvas.drawString(50, 595, 'Address')
            my_canvas.drawString(135, 595, '> ' + str(self.tf_area.get()) + ',' + str(self.tf_city.get()))
            my_canvas.line(50, 593, 580, 593)

            my_canvas.drawString(48, 585, '19. Received As')
            my_canvas.drawString(135, 585, '> '+str(self.cb_receivedas.get()))
            my_canvas.drawString(300, 585, '20. Seen By')
            my_canvas.drawString(390, 585, '> '+self.tf_seenby.get())

            my_canvas.drawString(48, 575, '21. Admission Type')
            my_canvas.drawString(135, 575, '> '+str(self.cb_typeofadmission.get()))
            my_canvas.drawString(300, 575, '22. Transfer Form')
            my_canvas.drawString(390, 575, '> '+str(self.tf_details.get()))

            my_canvas.drawString(48, 565, '23. Diet')
            my_canvas.drawString(135, 565, '> '+str(self.tf_diet.get()))
            my_canvas.drawString(300, 565, '24. MLC')
            my_canvas.drawString(390, 565, '>')

            my_canvas.drawString(48, 555, '25. Injury Report')
            my_canvas.drawString(135, 555, '>')
            my_canvas.drawString(300, 555, '26. Placed On List')
            my_canvas.drawString(390, 555, '>')

            my_canvas.drawString(48, 545, '27. Provisional Diagnosis')

            my_canvas.setFont('Helvetica', 10)
            my_canvas.drawString(400, 360, ' Signature & Stamp')
            my_canvas.setFont('Helvetica', 7)
            my_canvas.drawString(388, 350, ' (Medical Officers admitting the Case)')
            my_canvas.line(50, 344, 580, 344)

            my_canvas.drawString(50, 322, ' Personal/Unit Data Checked  :-')
            my_canvas.drawString(388, 312, ' (Signature Personnel/Family)')
            my_canvas.line(50, 310, 580, 310)
        # -===========================================
            my_canvas.line(80, 300, 80, 158)
            my_canvas.line(80, 300, 300, 300)
            my_canvas.line(300, 300, 300, 158)
            my_canvas.line(80, 158, 300, 158)

            my_canvas.setFont('Helvetica', 8)
            my_canvas.drawString(150, 290, ' MILITARY HOSPITAL ')
            my_canvas.drawString(160, 280, ' AMRITSAR')
            my_canvas.setFont('Helvetica', 9)
            my_canvas.drawString(150, 270, ' VISITOR PASS')
            my_canvas.line(150, 269, 220, 269)
            my_canvas.setFont('Helvetica', 8)
            my_canvas.drawString(85, 260, 'Please permit one Relative of No.'+str(number))
            my_canvas.drawString(85, 250, 'Name:- '+str(name))
            my_canvas.drawString(85, 240, 'Unit:- '+str(unit))
            my_canvas.drawString(85, 230, 'Address:- '+str(self.tf_area.get()))
            my_canvas.drawString(85, 220, 'State:- '+str(self.tf_state.get()))
            my_canvas.drawString(85, 210, 'Pin :-'+str(self.tf_pincode.get()))
            my_canvas.drawString(85, 200, 'A/D No:- '+str(ad))
            my_canvas.drawString(85, 190, 'valid upto 1900 hr on')
            my_canvas.drawString(85, 180, 'Visiting hour 1600-1800 h on ALL DAYS')
            my_canvas.drawString(85, 170, '1000-1200 h on Sundays/Holidays')
        # ============================================
            my_canvas.line(350, 300, 350, 158)
            my_canvas.line(350, 300, 560, 300)
            my_canvas.line(560, 300, 560, 158)
            my_canvas.line(350, 158, 560, 158)
            my_canvas.setFont('Helvetica', 8)
            my_canvas.drawString(415, 290, ' MILITARY HOSPITAL ')
            my_canvas.drawString(430, 280, ' AMRITSAR')
            my_canvas.setFont('Helvetica', 9)
            my_canvas.drawString(420, 270, ' VISITOR PASS')
            my_canvas.line(420, 269, 490, 269)
            my_canvas.setFont('Helvetica', 8)
            my_canvas.drawString(355, 260, 'Please permit one Relative of No.'+str(number))
            my_canvas.drawString(355, 250, 'Name:- '+str(name))
            my_canvas.drawString(355, 240, 'Unit:- '+str(unit))
            my_canvas.drawString(355, 230, 'Address:- '+str(self.tf_area.get()))
            my_canvas.drawString(355, 220, 'State:- '+str(self.tf_state.get()))
            my_canvas.drawString(355, 210, 'Pin:- '+str(self.tf_pincode.get()))
            my_canvas.drawString(355, 200, 'A/D No:- '+str(ad))
            my_canvas.drawString(355, 190, 'valid upto 1900 hr on')
            my_canvas.drawString(355, 180, 'Visiting hour 1600-1800 h on ALL DAYS')
            my_canvas.drawString(355, 170, '1000-1200 h on Sundays/Holidays')
         # -=======================================================
            my_canvas.save()
            subprocess.Popen([t], shell=True)
            self.win.destroy()

    #---------------------------------end----------------------------------------------------------

    #-===========================================END INSERT Query=================================================
#-=======================================================slip1=====================================================
    def reset(self):
        self.tf_station.delete(0, END)
        self.tf_cda.delete(0, END)
        self.tf_recordofficeaddress.delete(0, END)
        self.tf_recordoffice.delete(0, END)
        self.tf_mobileno.delete(0, END)
        self.tf_kinrelationship.delete(0, END)
        self.tf_nextofkin.delete(0, END)
        self.tf_formation.delete(0, END)
        self.tf_religion.delete(0, END)
        self.tf_totalservice.delete(0,END)
        self.tf_relationship.delete(0, END)
        self.tf_type.delete(0,END)
        self.tf_nameofpatient.delete(0, END)
        self.tf_ADno.delete(0, END)
        self.tf_age.delete(0, END)
        self.tf_unit.delete(0, END)
        self.tf_number.delete(0, END)
        self.tf_rank.delete(0,END)
        self.tf_name.delete(0,END)
        self.cb_martialstatus.set("")
        self.cb_service.set("")
        self.cb_sex.set("")

    def __init__(self,parent):
        # self.root = Tk()
        self.win=Toplevel(parent)
        self.win.transient(parent)
        self.win.parent = parent
        self.win.configure(background="snow")
        self.win.title("ADMISSION SLIP")
        self.win.iconbitmap(self,default="MH.ico")
        self.win.geometry("{0}x{0}+0+0".format(self.win.winfo_screenwidth(), self.win.winfo_screenheight()))
        now = datetime.datetime.now()
        current_date ="Current Date: "+str(now.strftime("%d-%m-%Y"))
        current_time= "Current Time:"+str(now.strftime("%H-%M-%S"))
        #-----------------------------------Frame--------------------------------------
        self.f = Frame(self.win, bg="snow")
        self.f.pack()
        #-----------------------------------end Frame---------------------------------
        self.lb_header = Label(self.f, text="HOSPITAL ADMISSION SLIP", bg="snow", fg="brown",font=("times new roman", 42, "bold", "underline"), pady=10)
        self.lb_header2=Label(self.f,text="Admission Page 1-2",bg="snow",fg="brown",font=("times new roman",8), pady=10)
        self.lb_showdate=Label(self.f,text=current_date,bg="snow",fg="brown",font=("times new roman",14, "bold"), pady=10)
        self.lb_showtime=Label(self.f,text=current_time,bg="snow",fg="brown",font=("times new roman",14,"bold"), pady=10)
        now=datetime.datetime.now()
        current_time = "Current Time: " + str(now.strftime("%H-%M-%S"))
        self.lb_showtime.config(text=current_time)
        self.lb_nameofhospital = Label(self.f, text="Name of Hospital", bg="snow", font=("times new roman", 14),padx=10)
        self.tf_nameofhospital = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.tf_nameofhospital.insert(0,"Military Hospital,Amritsar")
        self.lb_number = Label(self.f, text="Number", bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.tf_number = Entry(self.f, width=30, font=("times new roman", 14), relief="solid")
        self.bt_search=Button(self.f, text="Search", font=("times new roman", 11, "bold"), fg="brown", bg="#89d0ce",activebackground="snow", activeforeground="brown", height=1, width=15,command=self.search)
        self.lb_ADno = Label(self.f, text="A & D Nos.", bg="snow", font=("times new roman", 14), padx=10, pady=10)
        self.tf_ADno = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_rank = Label(self.f, text="Rank", bg="snow", font=("times new roman", 14), padx=20,pady=10)
        self.tf_rank = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_name = Label(self.f, text="Name", bg="snow", font=("times new roman", 14), padx=20, pady=10)
        self.tf_name = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_unit = Label(self.f, text="Unit/Ship with address", bg="snow", font=("times new roman", 14),padx=10,pady=10)
        self.tf_unit = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_nameofpatient = Label(self.f, text="Name of Patient", bg="snow", font=("times new roman", 14),padx=10,pady=10)
        self.tf_nameofpatient = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_relationship = Label(self.f, text="Relationship with Patient", bg="snow", font=("times new roman", 14),padx=10,pady=10)
        self.tf_relationship = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
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
        self.lb_religion = Label(self.f, text="Religion", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.tf_religion = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_station = Label(self.f, text="Station", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.tf_station = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_formation = Label(self.f, text="Formation/Command", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.tf_formation = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_nextofkin = Label(self.f, text="Next of Kin", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.tf_nextofkin = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_kinrelationship= Label(self.f, text="Relationship", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.tf_kinrelationship = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_mobileno = Label(self.f, text="Mobile Number", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.tf_mobileno = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_cda = Label(self.f, text="CDA Account No.", bg="snow", font=("times new roman", 14), pady=10,padx=10)
        self.tf_cda = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.tf_cda.insert(0,'N/A')
        self.lb_recordoffice = Label(self.f, text="Record Office", bg="snow", font=("times new roman", 14), pady=10, padx=10)
        self.tf_recordoffice = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        self.lb_recordofficeaddress = Label(self.f, text="Address of Record Office", bg="snow", font=("times new roman", 14), pady=10,padx=10)
        self.tf_recordofficeaddress = Entry(self.f, width=50, font=("times new roman", 14), relief="solid")
        #------------------------------------------------Button----------------------------------
        self.bt_mainmenu = Button(self.f, text="MAIN MENU", font=("times new roman", 11, "bold"), fg="white", bg="#f9d591",activebackground="snow", activeforeground="brown", height=1, width=20,command=lambda :self.win.destroy())
        self.bt_proceed = Button(self.f, text="PROCEED>>", font=("times new roman", 11, "bold"), fg="white", bg="green",activebackground="#F0E68C", activeforeground="white", height=1, width=20,command=lambda :self.slip2(self.win))
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
        self.lb_ADno.grid(row=3, column=1,sticky=(E))
        self.tf_ADno.grid(row=3, column=2)
        self.lb_rank.grid(row=3, column=5,sticky=(E))
        self.tf_rank.grid(row=3, column=6)
        self.lb_name.grid(row=4, column=1,sticky=(E))
        self.tf_name.grid(row=4, column=2)
        self.lb_unit.grid(row=4, column=5,sticky=(E))
        self.tf_unit.grid(row=4, column=6)
        self.lb_nameofpatient.grid(row=5, column=1,sticky=(E))
        self.tf_nameofpatient.grid(row=5, column=2)
        self.lb_relationship.grid(row=5,column=5,sticky=(E))
        self.tf_relationship.grid(row=5,column=6)
        self.lb_age.grid(row=6, column=1,sticky=(E))
        self.tf_age.grid(row=6, column=2,sticky=(W))
        self.cb_sex.grid(row=6,column=2,sticky=(E))
        self.lb_martialstatus.grid(row=6, column=5,sticky=(E))
        self.cb_martialstatus.grid(row=6, column=6)
        self.lb_service.grid(row=7, column=1,sticky=(E))
        self.cb_service.grid(row=7, column=2)
        self.lb_type.grid(row=7, column=5,sticky=(E))
        self.tf_type.grid(row=7, column=6)
        self.lb_totalservice.grid(row=8, column=1,sticky=(E))
        self.tf_totalservice.grid(row=8, column=2)
        self.lb_religion.grid(row=8, column=5,sticky=(E))
        self.tf_religion.grid(row=8, column=6)
        self.lb_station.grid(row=9, column=1,sticky=(E))
        self.tf_station.grid(row=9,column=2)
        self.lb_formation.grid(row=9, column=5,sticky=(E))
        self.tf_formation.grid(row=9, column=6)
        self.lb_nextofkin.grid(row=10, column=1,sticky=(E))
        self.tf_nextofkin.grid(row=10, column=2)
        self.lb_kinrelationship.grid(row=10, column=5,sticky=(E))
        self.tf_kinrelationship.grid(row=10, column=6)
        self.lb_mobileno.grid(row=11, column=1,sticky=(E))
        self.tf_mobileno.grid(row=11, column=2)
        self.lb_cda.grid(row=11, column=5,sticky=(E))
        self.tf_cda.grid(row=11, column=6)
        self.lb_recordoffice.grid(row=12, column=1,sticky=(E))
        self.tf_recordoffice.grid(row=12, column=2)
        self.lb_recordofficeaddress.grid(row=12, column=5,sticky=(E))
        self.tf_recordofficeaddress.grid(row=12, column=6)
        self.bt_mainmenu.grid(row=16,column=0,columnspan=6,pady=20,sticky=(W))
        self.bt_reset.grid(row=16,column=2,columnspan=6,sticky=(W),padx=50)
        self.bt_proceed.grid(row=16, column=1, columnspan=6, pady=20,sticky=(E))
        # self.root.mainloop()
        self.result = None

# x=admission