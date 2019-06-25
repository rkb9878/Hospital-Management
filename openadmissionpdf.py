
from server import *
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import subprocess
#-=================
class openadmissionpdf():
    def open(self,number,nameofpatient,admissiondate):
        file = str(number) + str(nameofpatient) + str(admissiondate)
        t = str("C:\pdf\Admission\\" + file + ".pdf")
        output=subprocess.Popen([t], shell=True)
