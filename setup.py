import cx_Freeze
import sys
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = None



executables = [cx_Freeze.Executable("MH.py", base=base, icon="MH.ico")]

shortcut_table = [
    ("DesktopShortcut")]

cx_Freeze.setup(
    name = "MH",
    version="1.0",
    options = {"build_exe": {"packages":["tkinter","pymysql","datetime","tkcalendar"], 'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            "MH.ico","indian.jpg"
         ],}},
    description = "MH Desktop Application",
    executables = executables
    )

msi_data = {"Shortcut": shortcut_table}