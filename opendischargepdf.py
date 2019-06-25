from server import *
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import subprocess
# -=================
class opendischargepdf():
    def open(self,number,nameofpatient,dischargedate):
        file = str(number) + str(nameofpatient) + str(dischargedate)
        t = str("C:\pdf\discharge\\" + file + ".pdf")
        output = subprocess.Popen([t], shell=True)
