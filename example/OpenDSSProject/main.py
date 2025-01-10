from functions import *
import py_dss_interface



# Load the Excel file
excel_file = './InputData/OpenDSSInputSheet.xlsx'  # Replpace with your Excel file path

# Load Circuit Data from Excel fil to DSS file
#load_data_from_excel(excel_file)


'''
#Create Instance of the OpenDSS App
dss = py_dss_interface.DSS()

opendss_path = "C:/Program Files/OpenDSS"

#Get the DSS File
dss_file = "C:/Users/abhi/Dropbox/Python Scripts/OpenDSSProject/CircuitData/DSSproject.dss"
dss.text("compile {}".format(dss_file))

'''

import py_dss_interface
import os
import pathlib
import pandas as pd

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("CircuitData", "DSSproject.dss")

#dss = py_dss_interface.DSS()
#dss = py_dss_interface.DSS(opendss_path)
dss = py_dss_interface.DSS()



dss.text(f"compile [{dss_file}]")



#dss.text("solve")


#dss_file = "./CircuitData/DSSproject.dss"
#dss.text("compile {}".format(dss_file))




