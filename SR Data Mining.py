import csv
import numpy as np
import urllib.request
from bs4 import BeautifulSoup
import time
from socket import timeout
import re

with open(r'C:\Users\ktovson\Desktop\SR Classifier Project\SRData\Data15to16.csv', encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    DataArray=[]
    SRTypeArray=[]
    for column in readCSV:
         SR_Number = column[0]
         SRType = column[1]
         Summary = column[2]
         try:
             # specify the URL
             SR_URL = "http://force.natinst.com:8000/pls/ebiz/niae_screenpop.main?p_incident_number=" + str(
                 SR_Number) + "&p_contact_number="

             # query website and return html to variable 'page'
             page = urllib.request.urlopen(SR_URL, timeout=10)

             # parse the html using beautiful soup and store in variable `soup`
             soup = BeautifulSoup(page, 'html.parser')

             ### PROBLEM DESCRIPTION ###

             # find the last Problem Description tag
             PD_label = soup.find_all("td", string="Problem Description")[-1]

             # locate the tag for problem description data
             PD_parent = PD_label.find_all_next("td")[2]

             # acquire text
             PD_raw = PD_parent.renderContents()

             # trim the space off text
             PD_strip = PD_raw.strip()

             # remove break line tags
             PD_break1 = PD_strip.replace(b'<br/>', b'')
             PD_break2 = PD_break1.replace(b'\r', b'')
             SRDescription_unformatted = PD_break2
             SRDescription = str(SRDescription_unformatted, 'utf-8')

             ### SOFTWARE ###

             # find the last SR Created on the Web tag
             Web_label = soup.find_all("td", string="SR Created on the Web")[-1]

             # locate the tag for web data
             Web_parent = Web_label.find_all_next("td")[2]

             # acquire text
             Web_raw = Web_parent.renderContents()

             # trim the space off text
             Web_strip = Web_raw.strip()

             # remove break line tags
             Web_break1 = Web_strip.replace(b'<br/>', b'')
             Web_break2 = Web_break1.replace(b'\r', b'')
             Web_unformatted = Web_break2
             Web_Data = str(Web_unformatted, 'utf-8')

             # initialize string and index variables
             HardwareString = "Hardware:"
             SoftwareString = "Software:"
             OSString = "OS:"

             # get listed software
             HardwareIndex = Web_Data.find(HardwareString)
             SoftwareIndex = Web_Data.find(SoftwareString)
             Software_raw = Web_Data[SoftwareIndex + 10:HardwareIndex]

             # remove free form entry str
             Software = Software_raw.replace("(Free form entry)", "")

             ### HARDWARE ###

             # get listed hardware
             HardwareIndex = Web_Data.find(HardwareString)
             OSIndex = Web_Data.find(OSString)
             Hardware_raw = Web_Data[HardwareIndex + 10:OSIndex]

             # remove free form entry str
             Hardware = Hardware_raw.replace("(Free form entry)", "")

             # concatenate strings into one variable 'data'
             Data = SRDescription + " " + Software + " " + Hardware

            # remove unwanted characters and make data uppercase
             Data = re.sub('[Â¿â€Ã™]', '', Data)
             Data = Data.upper()
             Data = Data.replace("PROBLEM DESCRIPTION:", "")

             # append data to arrays
             DataArray.append(Data)
             SRTypeArray.append(SRType)

             print(SR_Number)

             # wait 1 second before next loop
             time.sleep(1)

         except (IndexError, timeout):
             print(str(SR_Number) + " ERROR")


outputArray = []
for i in range(len(DataArray)):
    outputArray.append([DataArray[i], SRTypeArray[i]])

with open(r"C:\Users\ktovson\Desktop\SR Classifier Project\SRData\TrainingData5.csv", mode='w+', newline='', encoding='utf-8') as CSVtoWrite:
    csvWriter = csv.writer(CSVtoWrite, delimiter=',')
    csvWriter.writerows(outputArray)
