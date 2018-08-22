## THIS SCRIPT TESTS A SINGLE REQUEST AND CLASSIFIES IT WITH THE TRAINING SET ##

import sys
import csv
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.feature_extraction import text

def MachineLearning(ProblemDescription, Hardware, Software):

    #training file location
    trainingfilelocation = r"C:\Users\ktovson\Desktop\SR Classifier Project\Data\EqualData.csv"

    SRTypes = np.array([
        'CAN',
        'CM C Series',
        'Calibration',
        'CounterTimer',
        'DAQExpress',
        'DIAdem',
        'DMM',
        'DSA HW',
        'Digital_IO',
        'FIRST (NIC Only)',
        'FieldBus',
        'FieldPoint',
        'FlexLogger',
        'FunctionalSafety',
        'GATI',
        'GPIB',
        'HMI and Industrial PCs',
        'HiQ',
        'HighSpeedDigital_IO',
        'IMAQ',
        'IOTechVibration',
        'Industrial Communications',
        'InsightCM',
        'LV',
        'LV CD&Sim',
        'LV Comms',
        'LV Controls Add-Ons',
        'LV Embedded',
        'LV MathScript RT',
        'LV NXG',
        'LV NXT',
        'LVDSC',
        'LVFPGA',
        'LVPDA and LV Touch Panel',
        'LVRT',
        'LabWindows_CVI',
        'Lookout',
        'MATRIXx',
        'Measure (Legacy)',
        'MStudioDotNet',
        'MStudioVisualBasic',
        'MStudioVisualC',
        'Motion',
        'MultifunctionDAQ',
        'Multimedia Test HW/SW',
        'Multisim (EWB)',
        'NI Update Service',
        'OPC Servers',
        'Optical (OSI)',
        'PXI Controllers, Chassis, MXI',
        'PXI Timing and Sync',
        'Power Supplies and SMUs',
        'Powertrain Controls',
        'RAID',
        'RF',
        'RF Software',
        'RIO',
        'SC Express',
        'SCC',
        'SCXI',
        'SPEEDY33',
        'STS',
        'ScopesDigitizers',
        'Serial',
        'Signal Sources',
        'SignalCondOther',
        'SignalExpress',
        'SoftwareDefinedInstruments',
        'Sound and Vibration SW',
        'SwitchExecutive',
        'Switches',
        'SystemLink',
        'TestStand',
        'USRP',
        'Ultiboard (EWB)',
        'VBench',
        'VILogger',
        'VXI_MXI',
        'VeriStand',
        'VisionSW',
        'VolumeLicenseMgr',
        'WSN',
        'Web UI Builder',
        'myRIO'
        ])

    #get training data
    with open(trainingfilelocation, encoding='utf-8', errors='replace') as trainingfile:
        readCSV = csv.reader(trainingfile, delimiter=',')
        DataArray=[]
        SRTypeArray=[]
        for column in readCSV:
             SRData = column[0]
             SRType = column[1]
             SRTypeArray.append(SRType)
             DataArray.append(SRData)
    train_data = DataArray
    train_target = SRTypeArray

    #get test data
    test_data = np.array([ProblemDescription + " " + Hardware + " " + Software])

    #add stop words
    my_stop_words = text.ENGLISH_STOP_WORDS.union(["cost", "solution", "help", "question", "thanks", "please"])

    #create model
    model = make_pipeline(TfidfVectorizer(decode_error= 'ignore', stop_words='english'), MultinomialNB())
    classifier = model.fit(train_data, train_target)
    predicted = model.predict(test_data)

    #remove brackets and quotes and print predicted label
    print(str(predicted).replace("'", "").replace('.','').replace('[','').replace(']',''))

if __name__ == "__main__":
    ProblemDescription = str(sys.argv[1])
    Hardware = str(sys.argv[2])
    Software = str(sys.argv[3])
    MachineLearning(ProblemDescription, Hardware, Software)
