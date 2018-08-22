## THIS SCRIPT EQUALIZES ALL SERVICE REQUEST TYPES TO GENERATE EQUALLY WEIGHTED TRAINING DATA FOR EACH TYPE. ##
## FOR HIGH VOLUME TYPES, IT TAKES A NUMBER OF SRs (THRESHOLD) AND THEN GENERATES ARTIFICIAL DATA FOR LOW ##
## VOLUME TYPES FROM HARDWARE AND SOFTWARE KEYWORDS. THEN IT RUNS THROUGH A MACHINE LEARNING CLASSIFIER AND ##
## GENERATES A RESULTS FILE. ##


import csv
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.feature_extraction import text

#file locations
keywordsfilelocation = r'C:\Users\ktovson\Desktop\SR Classifier Project\Keywords\Keywords.csv'
keywordstringsfilelocation = r"C:\Users\ktovson\Desktop\SR Classifier Project\Keywords\Keywordstrings.csv"
rawtrainingfilelocation = r'C:\Users\ktovson\Desktop\SR Classifier Project\Data\TrainingDataFINAL.csv'
trainingfilelocation = r"C:\Users\ktovson\Desktop\SR Classifier Project\Data\EqualData.csv"
testfilelocation = r'C:\Users\ktovson\Desktop\SR Classifier Project\Data\TestDataFINAL.csv'
predictionresultsfile = r"C:\Users\ktovson\Desktop\SR Classifier Project\Results\Results.csv"

#define number of SRs per type
threshold = 500

#initialize SRType keyword strings
CAN_str = ""
CMCSeries_str = ""
Calibration_str = ""
CounterTimer_str = ""
DAQExpress_str = ""
DIAdem_str = ""
DMM_str = ""
DSAHW_str = ""
Digital_IO_str = ""
FIRST_str = ""
FieldBus_str = ""
FieldPoint_str = ""
FlexLogger_str = ""
FunctionalSafety_str = ""
GATI_str = ""
GPIB_str = ""
HMI_str = ""
HiQ_str = ""
HighSpeedDigital_IO_str = ""
IMAQ_str = ""
IOTechVibration_str = ""
IndustrialCommunications_str = ""
InsightCM_str = ""
LV_str = ""
LVCDSim_str = ""
LVComms_str = ""
LVControls_str = ""
LVEmbedded_str = ""
LVMathScriptRT_str = ""
LVNXG_str = ""
LVNXT_str = ""
LVDSC_str = ""
LVFPGA_str = ""
LVPDA_str = ""
LVRT_str = ""
LabWindows_CVI_str = ""
Lookout_str = ""
MATRIXx_str = ""
MStudioDotNet_str = ""
MStudioVisualBasic_str = ""
MStudioVisualC_str = ""
Measure_str = ""
Motion_str = ""
MultifunctionDAQ_str = ""
MultimediaTest_str = ""
Multisim_str = ""
NIUpdateService_str = ""
OPCServers_str = ""
Optical_str = ""
PXIChassis_str = ""
PXITimingandSync_str = ""
PowerSuppliesandSMUs_str = ""
PowertrainControls_str = ""
RAID_str = ""
RF_str = ""
RFSoftware_str = ""
RIO_str = ""
SCExpress_str = ""
SCC_str = ""
SCXI_str = ""
SPEEDY33_str = ""
STS_str = ""
ScopesDigitizers_str = ""
Serial_str = ""
SignalSources_str = ""
SignalCondOther_str = ""
SignalExpress_str = ""
SoftwareDefinedInstruments_str = ""
SoundandVibrationSW_str = ""
SwitchExecutive_str = ""
Switches_str = ""
SystemLink_str = ""
TestStand_str = ""
USRP_str = ""
UltiboardEWB_str = ""
VBench_str = ""
VILogger_str = ""
VXI_MXI_str = ""
VeriStand_str = ""
VisionSW_str = ""
VolumeLicenseMgr_str = ""
WSN_str = ""
WebUIBuilder_str = ""
myRIO_str = ""

#grab keywords from file and concatenate into one string per SRType
with open(keywordsfilelocation, encoding='utf-8') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for column in readCSV:
        SRData = column[0]
        SRType = column[1]
        if SRType == "CAN":
            CAN_str = CAN_str + " " + SRData
        if SRType == "CM C Series":
            CMCSeries_str = CMCSeries_str + " " + SRData
        if SRType == "Calibration":
            Calibration_str = Calibration_str + " " + SRData
        if SRType == "CounterTimer":
            CounterTimer_str = CounterTimer_str + " " + SRData
        if SRType == "DAQExpress":
            DAQExpress_str = DAQExpress_str + " " + SRData
        if SRType == "DIAdem":
            DIAdem_str = DIAdem_str + " " + SRData
        if SRType == "DMM":
            DMM_str = DMM_str + " " + SRData
        if SRType == "DSA HW":
            DSAHW_str = DSAHW_str + " " + SRData
        if SRType == "Digital_IO":
            Digital_IO_str = Digital_IO_str + " " + SRData
        if SRType == "FIRST (NIC Only)":
            FIRST_str= FIRST_str + " " + SRData
        if SRType == "FieldBus":
            FieldBus_str = FieldBus_str + " " + SRData
        if SRType == "FieldPoint":
            FieldPoint_str = FieldPoint_str + " " + SRData
        if SRType == "FlexLogger":
            FlexLogger_str = FlexLogger_str + " " + SRData
        if SRType == "Functional Safety":
            FunctionalSafety_str = FunctionalSafety_str + " " + SRData
        if SRType == "GATI":
            GATI_str = GATI_str + " " + SRData
        if SRType == "GPIB":
            GPIB_str = GPIB_str + " " + SRData
        if SRType == "HMI and Industrial PCs":
            HMI_str = HMI_str + " " + SRData
        if SRType == "HiQ":
            HiQ_str = HiQ_str + " " + SRData
        if SRType == "HighSpeedDigital_IO":
            HighSpeedDigital_IO_str = HighSpeedDigital_IO_str + " " + SRData
        if SRType == "IMAQ":
            IMAQ_str = IMAQ_str + " " + SRData
        if SRType == "IOTech Vibration":
            IOTechVibration_str = IOTechVibration_str + " " + SRData
        if SRType == "Industrial Communications":
            IndustrialCommunications_str = IndustrialCommunications_str + " " + SRData
        if SRType == "InsightCM":
            InsightCM_str = InsightCM_str + " " + SRData
        if SRType == "LV":
            LV_str = LV_str + " " + SRData
        if SRType == "LV CD&SIM":
            LVCDSim_str = LVCDSim_str + " " + SRData
        if SRType == "LV Comms":
            LVComms_str = LVComms_str + " " + SRData
        if SRType == "LV Controls Add-Ons":
            LVControls_str = LVControls_str + " " + SRData
        if SRType == "LV Embedded":
            LVEmbedded_str = LVEmbedded_str + " " + SRData
        if SRType == "LV MathScript RT":
            LVMathScriptRT_str = LVMathScriptRT_str + " " + SRData
        if SRType == "LV NXG":
            LVNXG_str = LVNXG_str + " " + SRData
        if SRType == "LV NXT":
            LVNXT_str = LVNXT_str + " " + SRData
        if SRType == "LVDSC":
            LVDSC_str = LVDSC_str + " " + SRData
        if SRType == "LVFPGA":
            LVFPGA_str = LVFPGA_str + " " + SRData
        if SRType == "LVPDA and LV Touch Panel":
            LVPDA_str = LVPDA_str + " " + SRData
        if SRType == "LVRT":
            LVRT_str = LVRT_str + " " + SRData
        if SRType == "LabWindows_CVI":
            LabWindows_CVI_str = LabWindows_CVI_str + " " + SRData
        if SRType == "Lookout":
            Lookout_str = Lookout_str + " " + SRData
        if SRType == "MATRIXx":
            MATRIXx_str = MATRIXx_str + " " + SRData
        if SRType == "MStudioDotNet":
            MStudioDotNet_str = MStudioDotNet_str + " " + SRData
        if SRType == "MStudioVisualBasic":
            MStudioVisualBasic_str = MStudioVisualBasic_str + " " + SRData
        if SRType == "MStudioVisualC":
            MStudioVisualC_str = MStudioVisualC_str + " " + SRData
        if SRType == "Measure (Legacy)":
            Measure_str = Measure_str + " " + SRData
        if SRType == "Motion":
            Motion_str = Motion_str + " " + SRData
        if SRType == "MultifunctionDAQ":
            MultifunctionDAQ_str = MultifunctionDAQ_str + " " + SRData
        if SRType == "Multimedia Test HW/SW":
            MultimediaTest_str = MultimediaTest_str + " " + SRData
        if SRType == "Multisim (EWB)":
            Multisim_str = Multisim_str + " " + SRData
        if SRType == "NI Update Service":
            NIUpdateService_str = NIUpdateService_str + " " + SRData
        if SRType == "OPC Servers":
            OPCServers_str = OPCServers_str + " " + SRData
        if SRType == "Optical (OSI)":
            Optical_str = Optical_str + " " + SRData
        if SRType == "PXI Controllers, Chassis, MXI":
            PXIChassis_str = PXIChassis_str + " " + SRData
        if SRType == "PXI Timing and Sync":
            PXITimingandSync_str = PXITimingandSync_str + " " + SRData
        if SRType == "Power Supplies and SMUs":
            PowerSuppliesandSMUs_str = PowerSuppliesandSMUs_str + " " + SRData
        if SRType == "Powertrain Controls":
            PowertrainControls_str = PowertrainControls_str + " " + SRData
        if SRType == "RAID":
            RAID_str = RAID_str + " " + SRData
        if SRType == "RF":
            RF_str = RF_str + " " + SRData
        if SRType == "RF Software":
            RFSoftware_str = RFSoftware_str + " " + SRData
        if SRType == "RIO":
            RIO_str = RIO_str + " " + SRData
        if SRType == "SC Express":
            SCExpress_str = SCExpress_str + " " + SRData
        if SRType == "SCC":
            SCC_str = SCC_str + " " + SRData
        if SRType == "SCXI":
            SCXI_str = SCXI_str + " " + SRData
        if SRType == "SPEEDY-33 (Hyperception)":
            SPEEDY33_str = SPEEDY33_str + " " + SRData
        if SRType == "STS":
            STS_str = STS_str + " " + SRData
        if SRType == "ScopesDigitizers":
            ScopesDigitizers_str = ScopesDigitizers_str + " " + SRData
        if SRType == "Serial":
            Serial_str = Serial_str + " " + SRData
        if SRType == "Signal Sources":
            SignalExpress_str = SignalSources_str + " " + SRData
        if SRType == "SignalCondOther":
            SignalCondOther_str = SignalCondOther_str + " " + SRData
        if SRType == "SignalExpress":
            SignalExpress_str = SignalExpress_str + " " + SRData
        if SRType == "Software Defined Instruments":
            SoftwareDefinedInstruments_str = SoftwareDefinedInstruments_str + " " + SRData
        if SRType == "Sound and Vibration SW":
            SoundandVibrationSW_str = SoundandVibrationSW_str + " " + SRData
        if SRType == "SwitchExecutive":
            SwitchExecutive_str = SwitchExecutive_str + " " + SRData
        if SRType == "Switches":
            Switches_str = Switches_str + " " + SRData
        if SRType == "SystemLink":
            SystemLink_str = SystemLink_str + " " + SRData
        if SRType == "TestStand":
            TestStand_str = TestStand_str + " " + SRData
        if SRType == "USRP":
            USRP_str = USRP_str + " " + SRData
        if SRType == "Ultiboard (EWB)":
            UltiboardEWB_str = UltiboardEWB_str + " " + SRData
        if SRType == "VBench":
            VBench_str = VBench_str + " " + SRData
        if SRType == "VI Logger":
            VILogger_str = VILogger_str + " " + SRData
        if SRType == "VXI_MXI":
            VXI_MXI_str = VXI_MXI_str + " " + SRData
        if SRType == "VeriStand":
            VeriStand_str = VeriStand_str + " " + SRData
        if SRType == "VisionSW":
            VisionSW_str = VisionSW_str + " " + SRData
        if SRType == "VolumeLicenseMgr":
            VolumeLicenseMgr_str = VolumeLicenseMgr_str + " " + SRData
        if SRType == "WSN":
            WSN_str = WSN_str + " " + SRData
        if SRType == "Web UI Builder":
            WebUIBuilder_str = WebUIBuilder_str + " " + SRData
        if SRType == "myRIO":
            myRIO_str = myRIO_str + " " + SRData
        else:
            pass

#create array of keyword string and associated SRType
CAN_array = [CAN_str, "CAN"]
CMCSeries_array = [CMCSeries_str, "CM C Series"]
Calibration_array = [Calibration_str, "Calibration"]
CounterTimer_array = [CounterTimer_str, "CounterTimer"]
DAQExpress_array = [DAQExpress_str, "DAQExpress"]
DIAdem_array = [DIAdem_str, "DIAdem"]
DMM_array = [DMM_str, "DMM"]
DSAHW_array = [DSAHW_str, "DSA HW"]
Digital_IO_array = [Digital_IO_str, "Digital_IO"]
FIRST_array = [FIRST_str, "FIRST (NIC Only)"]
FieldBus_array = [FieldBus_str, "FieldBus"]
FieldPoint_array = [FieldPoint_str, "FieldPoint"]
FlexLogger_array = [FlexLogger_str, "FlexLogger"]
FunctionalSafety_array = [FunctionalSafety_str, "Functional Safety"]
GATI_array = [GATI_str, "GATI"]
GPIB_array = [GPIB_str, "GPIB"]
HMI_array = [HMI_str, "HMI and Industrial PCs"]
HiQ_array = [HiQ_str, "HiQ"]
HighSpeedDigital_IO_array = [HighSpeedDigital_IO_str, "HighSpeedDigital_IO"]
IMAQ_array = [IMAQ_str, "IMAQ"]
IOTechVibration_array = [IOTechVibration_str, "IOTech Vibration"]
IndustrialCommunications_array = [IndustrialCommunications_str, "Industrial Communications"]
InsightCM_array = [InsightCM_str, "InsightCM"]
LV_array = [LV_str, "LV"]
LVCDSim_array = [LVCDSim_str, "LV CD&SIM"]
LVComms_array = [LVComms_str, "LV Comms"]
LVControls_array = [LVControls_str, "LV Controls Add-Ons"]
LVEmbedded_array = [LVEmbedded_str, "LV Embedded"]
LVMathScriptRT_array = [LVMathScriptRT_str, "LV MathScript RT"]
LVNXG_array = [LVNXG_str, "LV NXG"]
LVNXT_array = [LVNXT_str, "LV NXT"]
LVDSC_array = [LVDSC_str, "LVDSC"]
LVFPGA_array = [LVFPGA_str, "LVFPGA"]
LVPDA_array = [LVPDA_str, "LVPDA and LV Touch Panel"]
LVRT_array = [LVRT_str, "LVRT"]
LabWindows_CVI_array = [LabWindows_CVI_str, "LabWindows_CVI"]
Lookout_array = [Lookout_str, "Lookout"]
MATRIXx_array = [MATRIXx_str, "MATRIXx"]
MStudioDotNet_array = [MStudioDotNet_str, "MStudioDotNet"]
MStudioVisualBasic_array = [MStudioVisualBasic_str, "MStudioVisualBasic"]
MStudioVisualC_array = [MStudioVisualC_str, "MStudioVisualC"]
Measure_array = [Measure_str, "Measure"]
Motion_array = [Motion_str, "Motion"]
MultifunctionDAQ_array = [MultifunctionDAQ_str, "MultifunctionDAQ"]
MultimediaTest_array = [MultimediaTest_str, "Multimedia Test HW/SW"]
Multisim_array = [Multisim_str, "Multisim (EWB)"]
NIUpdateService_array = [NIUpdateService_str, "NI Update Service"]
OPCServers_array = [OPCServers_str, "OPC Servers"]
Optical_array = [Optical_str, "Optical (OSI)"]
PXIChassis_array = [PXIChassis_str, "PXI Controllers, Chassis, MXI"]
PXITimingandSync_array = [PXITimingandSync_str, "PXI Timing and Sync"]
PowerSuppliesandSMUs_array = [PowerSuppliesandSMUs_str, "Power Supplies and SMUs"]
PowertrainControls_array = [PowertrainControls_str, "Powertrain Controls"]
RAID_array = [RAID_str, "RAID"]
RF_array = [RF_str, "RF"]
RFSoftware_array = [RFSoftware_str, "RF Software"]
RIO_array = [RIO_str, "RIO"]
SCExpress_array = [SCExpress_str, "SC Express"]
SCC_array = [SCC_str, "SCC"]
SCXI_array = [SCXI_str, "SCXI"]
SPEEDY33_array = [SPEEDY33_str, "SPEEDY-33 (Hyperception)"]
STS_array = [STS_str, "STS"]
ScopesDigitizers_array = [ScopesDigitizers_str, "ScopesDigitizers"]
Serial_array = [Serial_str, "Serial"]
SignalSources_array = [SignalSources_str, "Signal Sources"]
SignalCondOther_array = [SignalCondOther_str, "SignalCondOther"]
SignalExpress_array = [SignalExpress_str, "SignalExpress"]
SoftwareDefinedInstruments_array = [SoftwareDefinedInstruments_str, "Software Defined Instruments"]
SoundandVibrationSW_array = [SoundandVibrationSW_str, "Sound and Vibration SW"]
SwitchExecutive_array = [SwitchExecutive_str, "SwitchExecutive"]
Switches_array = [Switches_str, "Switches"]
SystemLink_array = [SystemLink_str, "SystemLink"]
TestStand_array = [TestStand_str, "TestStand"]
USRP_array = [USRP_str, "USRP"]
UltiboardEWB_array = [UltiboardEWB_str, "Ultiboard (EWB)"]
VBench_array = [VBench_str, "VBench"]
VILogger_array = [VILogger_str, "VI Logger"]
VXI_MXI_array = [VXI_MXI_str, "VXI_MXI"]
VeriStand_array = [VeriStand_str, "VeriStand"]
VisionSW_array = [VisionSW_str, "VisionSW"]
VolumeLicenseMgr_array = [VolumeLicenseMgr_str, "VolumeLicenseMgr"]
WSN_array = [WSN_str, "WSN"]
WebUIBuilder_array = [WebUIBuilder_str, "Web UI Builder"]
myRIO_array = [myRIO_str, "myRIO"]

#merge all keyword arrays
Output = np.array([
    CAN_array,
    CMCSeries_array,
    Calibration_array,
    CounterTimer_array,
    DAQExpress_array,
    DIAdem_array,
    DMM_array,
    DSAHW_array,
    Digital_IO_array,
    FIRST_array,
    FieldBus_array,
    FieldPoint_array,
    FlexLogger_array,
    FunctionalSafety_array,
    GATI_array,
    GPIB_array,
    HMI_array,
    HiQ_array,
    HighSpeedDigital_IO_array,
    IMAQ_array,
    IOTechVibration_array,
    IndustrialCommunications_array,
    InsightCM_array,
    LV_array,
    LVCDSim_array,
    LVComms_array,
    LVControls_array,
    LVEmbedded_array,
    LVMathScriptRT_array,
    LVNXG_array,
    LVNXT_array,
    LVDSC_array,
    LVFPGA_array,
    LVPDA_array,
    LVRT_array,
    LabWindows_CVI_array,
    Lookout_array,
    MATRIXx_array,
    MStudioDotNet_array,
    MStudioVisualBasic_array,
    MStudioVisualC_array,
    Measure_array,
    Motion_array,
    MultifunctionDAQ_array,
    MultimediaTest_array,
    Multisim_array,
    NIUpdateService_array,
    OPCServers_array,
    Optical_array,
    PXIChassis_array,
    PXITimingandSync_array,
    PowerSuppliesandSMUs_array,
    PowertrainControls_array,
    RAID_array,
    RF_array,
    RFSoftware_array,
    RIO_array,
    SCExpress_array,
    SCC_array,
    SCXI_array,
    SPEEDY33_array,
    STS_array,
    ScopesDigitizers_array,
    Serial_array,
    SignalSources_array,
    SignalCondOther_array,
    SignalExpress_array,
    SoftwareDefinedInstruments_array,
    SoundandVibrationSW_array,
    SwitchExecutive_array,
    Switches_array,
    SystemLink_array,
    TestStand_array,
    USRP_array,
    UltiboardEWB_array,
    VBench_array,
    VILogger_array,
    VXI_MXI_array,
    VeriStand_array,
    VisionSW_array,
    VolumeLicenseMgr_array,
    WSN_array,
    WebUIBuilder_array,
    myRIO_array])

#ignore keyword strings that are empty
KeywordStrings = []
for column in Output:
    SRData = column[0]
    SRType = column[1]
    if SRData == "":
        pass
    else:
        KeywordStrings.append([SRData, SRType])

with open(keywordstringsfilelocation, mode='w+', newline='', encoding='utf-8') as CSVtoWrite:
    csvWriter = csv.writer(CSVtoWrite, delimiter=',')
    csvWriter.writerows(KeywordStrings)


#initialize SRType counts
CAN = 0
CMCSeries = 0
Calibration = 0
CounterTimer = 0
DAQExpress = 0
DIAdem = 0
DMM = 0
DSAHW = 0
Digital_IO = 0
FIRST = 0
FieldBus = 0
FieldPoint = 0
FlexLogger = 0
FunctionalSafety = 0
GATI = 0
GPIB = 0
HMI = 0
HiQ = 0
HighSpeedDigital_IO = 0
IMAQ = 0
IOTechVibration = 0
IndustrialCommunications = 0
InsightCM = 0
LV = 0
LVCDSim = 0
LVComms = 0
LVControls = 0
LVEmbedded = 0
LVMathScriptRT = 0
LVNXG = 0
LVNXT = 0
LVDSC = 0
LVFPGA = 0
LVPDA = 0
LVRT = 0
LabWindows_CVI = 0
Lookout = 0
MATRIXx = 0
MStudioDotNet = 0
MStudioVisualBasic = 0
MStudioVisualC = 0
Measure = 0
Motion = 0
MultifunctionDAQ = 0
MultimediaTest = 0
Multisim = 0
NIUpdateService = 0
OPCServers = 0
Optical = 0
PXIChassis = 0
PXITimingandSync = 0
PowerSuppliesandSMUs = 0
PowertrainControls = 0
RAID = 0
RF = 0
RFSoftware = 0
RIO = 0
SCExpress = 0
SCC = 0
SCXI = 0
SPEEDY33 = 0
STS = 0
ScopesDigitizers = 0
Serial = 0
SignalSources = 0
SignalCondOther = 0
SignalExpress = 0
SoftwareDefinedInstruments = 0
SoundandVibrationSW = 0
SwitchExecutive = 0
Switches = 0
SystemLink = 0
TestStand = 0
USRP = 0
UltiboardEWB = 0
VBench = 0
VILogger = 0
VXI_MXI = 0
VeriStand = 0
VisionSW = 0
VolumeLicenseMgr = 0
WSN = 0
WebUIBuilder = 0
myRIO = 0

#create array of SRTypes
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

SRTypeArray = []
DataArray = []

# import raw training data and count number of SRs per type
with open(rawtrainingfilelocation, encoding='utf-8', errors='ignore') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for column in readCSV:
        SRData = column[0]
        SRType = column[1]
        SRTypeArray.append(SRType)
        DataArray.append(SRData)
        if SRType == "CAN":
            CAN = CAN + 1
        if SRType == "CM C Series":
            CMCSeries = CMCSeries + 1
        if SRType == "Calibration":
            Calibration = Calibration + 1
        if SRType == "CounterTimer":
            CounterTimer = CounterTimer + 1
        if SRType == "DAQExpress":
            DAQExpress = DAQExpress + 1
        if SRType == "DIAdem":
            DIAdem = DIAdem + 1
        if SRType == "DMM":
            DMM = DMM + 1
        if SRType == "DSA HW":
            DSAHW = DSAHW + 1
        if SRType == "Digital_IO":
            Digital_IO = Digital_IO + 1
        if SRType == "FIRST (NIC Only)":
            FIRST = FIRST + 1
        if SRType == "FieldBus":
            FieldBus = FieldBus + 1
        if SRType == "FieldPoint":
            FieldPoint = FieldPoint + 1
        if SRType == "FlexLogger":
            FlexLogger = FlexLogger + 1
        if SRType == "Functional Safety":
            FunctionalSafety = FunctionalSafety + 1
        if SRType == "GATI":
            GATI = GATI + 1
        if SRType == "GPIB":
            GPIB = GPIB + 1
        if SRType == "HMI and Industrial PCs":
            HMI = HMI + 1
        if SRType == "HiQ":
            HiQ = HiQ + 1
        if SRType == "HighSpeedDigital_IO":
            HighSpeedDigital_IO = HighSpeedDigital_IO + 1
        if SRType == "IMAQ":
            IMAQ = IMAQ + 1
        if SRType == "IOTech Vibration":
            IOTechVibration = IOTechVibration + 1
        if SRType == "Industrial Communications":
            IndustrialCommunications = IndustrialCommunications + 1
        if SRType == "InsightCM":
            InsightCM = InsightCM + 1
        if SRType == "LV":
            LV = LV + 1
        if SRType == "LV CD&Sim":
            LVCDSim = LVCDSim + 1
        if SRType == "LV Comms":
            LVComms = LVComms + 1
        if SRType == "LV Controls Add-Ons":
            LVControls = LVControls + 1
        if SRType == "LV Embedded":
            LVEmbedded = LVEmbedded + 1
        if SRType == "LV MathScript RT":
            LVMathScriptRT = LVMathScriptRT + 1
        if SRType == "LV NXG":
            LVNXG = LVNXG + 1
        if SRType == "LV NXT":
            LVNXT = LVNXT + 1
        if SRType == "LVDSC":
            LVDSC = LVDSC + 1
        if SRType == "LVFPGA":
            LVFPGA = LVFPGA + 1
        if SRType == "LVPDA and LV Touch Panel":
            LVPDA = LVPDA + 1
        if SRType == "LVRT":
            LVRT = LVRT + 1
        if SRType == "LabWindows_CVI":
            LabWindows_CVI = LabWindows_CVI + 1
        if SRType == "Lookout":
            Lookout = Lookout + 1
        if SRType == "MATRIXx":
            MATRIXx = MATRIXx + 1
        if SRType == "MStudioDotNet":
            MStudioDotNet = MStudioDotNet + 1
        if SRType == "MStudioVisualBasic":
            MStudioVisualBasic = MStudioVisualBasic + 1
        if SRType == "MStudioVisualC":
            MStudioVisualC = MStudioVisualC + 1
        if SRType == "Measure (Legacy)":
            Measure = Measure + 1
        if SRType == "Motion":
            Motion = Motion + 1
        if SRType == "MultifunctionDAQ":
            MultifunctionDAQ = MultifunctionDAQ + 1
        if SRType == "Multimedia Test HW/SW":
            MultimediaTest = MultimediaTest + 1
        if SRType == "Multisim (EWB)":
            Multisim = Multisim + 1
        if SRType == "NI Update Service":
            NIUpdateService = NIUpdateService + 1
        if SRType == "OPC Servers":
            OPCServers = OPCServers + 1
        if SRType == "Optical (OSI)":
            Optical = Optical + 1
        if SRType == "PXI Controllers, Chassis, MXI":
            PXIChassis = PXIChassis + 1
        if SRType == "PXI Timing and Sync":
            PXITimingandSync = PXITimingandSync + 1
        if SRType == "Power Supplies and SMUs":
            PowerSuppliesandSMUs = PowerSuppliesandSMUs + 1
        if SRType == "Powertrain Controls":
            PowertrainControls = PowertrainControls + 1
        if SRType == "RAID":
            RAID = RAID + 1
        if SRType == "RF":
            RF = RF + 1
        if SRType == "RF Software":
            RFSoftware = RFSoftware + 1
        if SRType == "RIO":
            RIO = RIO + 1
        if SRType == "SC Express":
            SCExpress = SCExpress + 1
        if SRType == "SCC":
            SCC = SCC + 1
        if SRType == "SCXI":
            SCXI = SCXI + 1
        if SRType == "SPEEDY-33 (Hyperception)":
            SPEEDY33 = SPEEDY33 + 1
        if SRType == "STS":
            STS = STS + 1
        if SRType == "ScopesDigitizers":
            ScopesDigitizers = ScopesDigitizers + 1
        if SRType == "Serial":
            Serial = Serial + 1
        if SRType == "Signal Sources":
            SignalSources = SignalSources + 1
        if SRType == "SignalCondOther":
            SignalCondOther = SignalCondOther + 1
        if SRType == "SignalExpress":
            SignalExpress = SignalExpress + 1
        if SRType == "Software Defined Instruments":
            SoftwareDefinedInstruments = SoftwareDefinedInstruments + 1
        if SRType == "Sound and Vibration SW":
            SoundandVibrationSW = SoundandVibrationSW + 1
        if SRType == "SwitchExecutive":
            SwitchExecutive = SwitchExecutive + 1
        if SRType == "Switches":
            Switches = Switches + 1
        if SRType == "SystemLink":
            SystemLink = SystemLink + 1
        if SRType == "TestStand":
            TestStand = TestStand + 1
        if SRType == "USRP":
            USRP = USRP + 1
        if SRType == "Ultiboard (EWB)":
            UltiboardEWB = UltiboardEWB + 1
        if SRType == "VBench":
            VBench = VBench + 1
        if SRType == "VI Logger":
            VILogger = VILogger + 1
        if SRType == "VXI_MXI":
            VXI_MXI = VXI_MXI + 1
        if SRType == "VeriStand":
            VeriStand = VeriStand + 1
        if SRType == "VisionSW":
            VisionSW = VisionSW + 1
        if SRType == "VolumeLicenseMgr":
            VolumeLicenseMgr = VolumeLicenseMgr + 1
        if SRType == "WSN":
            WSN = WSN + 1
        if SRType == "Web UI Builder":
            WebUIBuilder = WebUIBuilder + 1
        if SRType == "myRIO":
            myRIO = myRIO + 1
        else:
            pass

classes = []
#create array of counts
SRTypeCounts = np.array([
    CAN,
    CMCSeries,
    Calibration,
    CounterTimer,
    DAQExpress,
    DIAdem,
    DMM,
    DSAHW,
    Digital_IO,
    FIRST,
    FieldBus,
    FieldPoint,
    FlexLogger,
    FunctionalSafety,
    GATI,
    GPIB,
    HMI,
    HiQ,
    HighSpeedDigital_IO,
    IMAQ,
    IOTechVibration,
    IndustrialCommunications,
    InsightCM,
    LV,
    LVCDSim,
    LVComms,
    LVControls,
    LVEmbedded,
    LVMathScriptRT,
    LVNXG,
    LVNXT,
    LVDSC,
    LVFPGA,
    LVPDA,
    LVRT,
    LabWindows_CVI,
    Lookout,
    MATRIXx,
    Measure,
    MStudioDotNet,
    MStudioVisualBasic,
    MStudioVisualC,
    Motion,
    MultifunctionDAQ,
    MultimediaTest,
    Multisim,
    NIUpdateService,
    OPCServers,
    Optical,
    PXIChassis,
    PXITimingandSync,
    PowerSuppliesandSMUs,
    PowertrainControls,
    RAID,
    RF,
    RFSoftware,
    RIO,
    SCExpress,
    SCC,
    SCXI,
    SPEEDY33,
    STS,
    ScopesDigitizers,
    Serial,
    SignalSources,
    SignalCondOther,
    SignalExpress,
    SoftwareDefinedInstruments,
    SoundandVibrationSW,
    SwitchExecutive,
    Switches,
    SystemLink,
    TestStand,
    USRP,
    UltiboardEWB,
    VBench,
    VILogger,
    VXI_MXI,
    VeriStand,
    VisionSW,
    VolumeLicenseMgr,
    WSN,
    WebUIBuilder,
    myRIO
])

#create class array for analysis of keywords
for i in range(len(SRTypeCounts)):
    if SRTypeCounts[i] > 0:
        classes.append(SRTypes[i])
    else:
        pass

#categorize SR types by if they have sufficient data
LowSRs = []
HighSRs = []
ZeroSRs = []
for i in range(len(SRTypeCounts)):
    if SRTypeCounts[i] > 0 and SRTypeCounts[i] < threshold:
        LowSRs.append([SRTypes[i], SRTypeCounts[i]])
    if SRTypeCounts[i] >= threshold:
        HighSRs.append(SRTypes[i])
    if SRTypeCounts[i] == 0:
        ZeroSRs.append(SRTypes[i])
    else:
        pass


#determine how many SRs need to be artificially generated for low SR types
NumbersToAdd = []
for column in LowSRs:
    Type = column[0]
    Count = column[1]
    Add = threshold - Count
    NumbersToAdd.append([Type, Add])


ArtificialData = []
#generate artificial SRs for low SR types using keywordstrings
for column in NumbersToAdd:
    AmountToAdd = column[1]
    SRType = column[0]
    if SRType == "CAN" and CAN_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(CAN_array)
            i = i + 1
    if SRType == "CM C Series" and CMCSeries_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(CMCSeries_array)
            i = i + 1
    if SRType == "Calibration" and Calibration_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(Calibration_array)
            i = i + 1
    if SRType == "CounterTimer" and CounterTimer_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(CounterTimer_array)
            i = i + 1
    if SRType == "DAQExpress" and DAQExpress_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(DAQExpress_array)
            i = i + 1
    if SRType == "DIAdem" and DIAdem_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(DIAdem_array)
            i = i + 1
    if SRType == "DMM" and DMM_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(DMM_array)
            i = i + 1
    if SRType == "DSA HW" and DSAHW_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(DSAHW_array)
            i = i + 1
    if SRType == "Digital_IO" and Digital_IO_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(Digital_IO_array)
            i = i + 1
    if SRType == "FIRST (NIC Only)" and FIRST_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(FIRST_array)
            i = i + 1
    if SRType == "FieldBus" and FieldBus_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(FieldBus_array)
            i = i + 1
    if SRType == "FieldPoint" and FieldPoint_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(FieldPoint_array)
            i = i + 1
    if SRType == "FlexLogger" and FlexLogger_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(FlexLogger_array)
            i = i + 1
    if SRType == "Functional Safety" and FunctionalSafety_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(FunctionalSafety_array)
            i = i + 1
    if SRType == "GATI" and GATI_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(GATI_array)
            i = i + 1
    if SRType == "GPIB" and GPIB_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(GPIB_array)
            i = i + 1
    if SRType == "HMI and Industrial PCs" and HMI_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(HMI_array)
            i = i + 1
    if SRType == "HiQ" and HiQ_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(HiQ_array)
            i = i + 1
    if SRType == "HighSpeedDigital_IO" and HighSpeedDigital_IO_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(HighSpeedDigital_IO_array)
            i = i + 1
    if SRType == "IMAQ" and IMAQ_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(IMAQ_array)
            i = i + 1
    if SRType == "IOTech Vibration" and IOTechVibration_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(IOTechVibration_array)
            i = i + 1
    if SRType == "Industrial Communications" and IndustrialCommunications_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(IndustrialCommunications_array)
            i = i + 1
    if SRType == "InsightCM" and InsightCM_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(InsightCM_array)
            i = i + 1
    if SRType == "LV" and LV_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(LV_array)
            i = i + 1
    if SRType == "LV CD&Sim" and LVCDSim_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(LVCDSim_array)
            i = i + 1
    if SRType == "LV Comms" and LVComms_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(LVComms_array)
            i = i + 1
    if SRType == "LV Controls Add-Ons" and LVControls_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(LVControls_array)
            i = i + 1
    if SRType == "LV Embedded" and LVEmbedded_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(LVEmbedded_array)
            i = i + 1
    if SRType == "LV MathScript RT" and LVMathScriptRT_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(LVMathScriptRT_array)
            i = i + 1
    if SRType == "LV NXG" and LVNXG_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(LVNXG_array)
            i = i + 1
    if SRType == "LV NXT" and LVNXT_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(LVNXT_array)
            i = i + 1
    if SRType == "LVDSC" and LVDSC_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(LVDSC_array)
            i = i + 1
    if SRType == "LVFPGA" and LVFPGA_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(LVFPGA_array)
            i = i + 1
    if SRType == "LVPDA and LV Touch Panel" and LVPDA_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(LVPDA_array)
            i = i + 1
    if SRType == "LVRT" and LVRT_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(LVRT_array)
            i = i + 1
    if SRType == "LabWindows_CVI" and LabWindows_CVI_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(LabWindows_CVI_array)
            i = i + 1
    if SRType == "Lookout" and Lookout_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(Lookout_array)
            i = i + 1
    if SRType == "MATRIXx" and MATRIXx_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(MATRIXx_array)
            i = i + 1
    if SRType == "MStudioDotNet" and MStudioDotNet_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(MStudioDotNet_array)
            i = i + 1
    if SRType == "MStudioVisualBasic" and MStudioVisualBasic_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(MStudioVisualBasic_array)
            i = i + 1
    if SRType == "MStudioVisualC" and FieldBus_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(MStudioVisualC_array)
            i = i + 1
    if SRType == "Measure (Legacy)" and Measure_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(Measure_array)
            i = i + 1
    if SRType == "Motion" and Motion_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(Motion_array)
            i = i + 1
    if SRType == "MultifunctionDAQ" and MultifunctionDAQ_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(MultifunctionDAQ_array)
            i = i + 1
    if SRType == "Multimedia Test HW/SW" and MultimediaTest_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(MultimediaTest_array)
            i = i + 1
    if SRType == "Multisim (EWB)" and Multisim_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(Multisim_array)
            i = i + 1
    if SRType == "NI Update Service" and NIUpdateService_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(NIUpdateService_array)
            i = i + 1
    if SRType == "OPC Servers" and OPCServers_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(OPCServers_array)
            i = i + 1
    if SRType == "Optical (OSI)" and Optical_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(Optical_array)
            i = i + 1
    if SRType == "PXI Controllers, Chassis, MXI" and PXIChassis_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(PXIChassis_array)
            i = i + 1
    if SRType == "PXI Timing and Sync" and PXITimingandSync_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(PXITimingandSync_array)
            i = i + 1
    if SRType == "Power Supplies and SMUs" and PowerSuppliesandSMUs_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(PowerSuppliesandSMUs_array)
            i = i + 1
    if SRType == "Powertrain Controls" and PowertrainControls_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(PowertrainControls_array)
            i = i + 1
    if SRType == "RAID" and RAID_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(RAID_array)
            i = i + 1
    if SRType == "RF" and RF_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(RF_array)
            i = i + 1
    if SRType == "RF Software" and RFSoftware_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(RFSoftware_array)
            i = i + 1
    if SRType == "RIO" and RIO_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(RIO_array)
            i = i + 1
    if SRType == "SC Express" and SCExpress_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(SCExpress_array)
            i = i + 1
    if SRType == "SCC" and SCC_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(SCC_array)
            i = i + 1
    if SRType == "SCXI" and SCXI_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(SCXI_array)
            i = i + 1
    if SRType == "SPEEDY-33 (Hyperception)" and SPEEDY33_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(SPEEDY33_array)
            i = i + 1
    if SRType == "STS" and STS_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(STS_array)
            i = i + 1
    if SRType == "ScopesDigitizers" and ScopesDigitizers_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(ScopesDigitizers_array)
            i = i + 1
    if SRType == "Serial" and Serial_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(Serial_array)
            i = i + 1
    if SRType == "Signal Sources" and SignalSources_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(SignalSources_array)
            i = i + 1
    if SRType == "SignalCondOther" and SignalCondOther_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(SignalCondOther_array)
            i = i + 1
    if SRType == "SignalExpress" and SignalExpress_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(SignalExpress_array)
            i = i + 1
    if SRType == "Software Defined Instruments" and SoftwareDefinedInstruments_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(SoftwareDefinedInstruments_array)
            i = i + 1
    if SRType == "Sound and Vibration SW" and SoundandVibrationSW_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(SoundandVibrationSW_array)
            i = i + 1
    if SRType == "SwitchExecutive" and SwitchExecutive_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(SwitchExecutive_array)
            i = i + 1
    if SRType == "Switches" and Switches_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(Switches_array)
            i = i + 1
    if SRType == "SystemLink" and SystemLink_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(SystemLink_array)
            i = i + 1
    if SRType == "TestStand" and TestStand_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(TestStand_array)
            i = i + 1
    if SRType == "USRP" and USRP_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(USRP_array)
            i = i + 1
    if SRType == "Ultiboard (EWB)" and UltiboardEWB_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(UltiboardEWB_array)
            i = i + 1
    if SRType == "VBench" and VBench_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(VBench_array)
            i = i + 1
    if SRType == "VI Logger" and VILogger_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(VILogger_array)
            i = i + 1
    if SRType == "VXI_MXI" and VXI_MXI_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(VXI_MXI_array)
            i = i + 1
    if SRType == "VeriStand" and VeriStand_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(VeriStand_array)
            i = i + 1
    if SRType == "VisionSW" and VisionSW_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(VisionSW_array)
            i = i + 1
    if SRType == "VolumeLicenseMgr" and VolumeLicenseMgr_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(VolumeLicenseMgr_array)
            i = i + 1
    if SRType == "WSN" and WSN_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(WSN_array)
            i = i + 1
    if SRType == "Web UI Builder" and WebUIBuilder_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(WebUIBuilder_array)
            i = i + 1
    if SRType == "myRIO" and myRIO_str != "":
        i = 0
        while i < AmountToAdd:
            ArtificialData.append(myRIO_array)
            i = i + 1
    else:
        pass

#add high volume SRType keywords ONCE
for i in HighSRs:
    SRType = i
    if SRType == "CAN" and CAN_str != "":
        ArtificialData.append(CAN_array)
    if SRType == "CM C Series" and CMCSeries_str != "":
            ArtificialData.append(CMCSeries_array)
    if SRType == "Calibration" and Calibration_str != "":
            ArtificialData.append(Calibration_array)
    if SRType == "CounterTimer" and CounterTimer_str != "":
            ArtificialData.append(CounterTimer_array)
    if SRType == "DAQExpress" and DAQExpress_str != "":
            ArtificialData.append(DAQExpress_array)
    if SRType == "DIAdem" and DIAdem_str != "":
            ArtificialData.append(DIAdem_array)
    if SRType == "DMM" and DMM_str != "":
            ArtificialData.append(DMM_array)
    if SRType == "DSA HW" and DSAHW_str != "":
            ArtificialData.append(DSAHW_array)
    if SRType == "Digital_IO" and Digital_IO_str != "":
            ArtificialData.append(Digital_IO_array)
    if SRType == "FIRST (NIC Only)" and FIRST_str != "":
            ArtificialData.append(FIRST_array)
    if SRType == "FieldBus" and FieldBus_str != "":
            ArtificialData.append(FieldBus_array)
    if SRType == "FieldPoint" and FieldPoint_str != "":
            ArtificialData.append(FieldPoint_array)
    if SRType == "FlexLogger" and FlexLogger_str != "":
            ArtificialData.append(FlexLogger_array)
    if SRType == "Functional Safety" and FunctionalSafety_str != "":
            ArtificialData.append(FunctionalSafety_array)
    if SRType == "GATI" and GATI_str != "":
            ArtificialData.append(GATI_array)
    if SRType == "GPIB" and GPIB_str != "":
            ArtificialData.append(GPIB_array)
    if SRType == "HMI and Industrial PCs" and HMI_str != "":
            ArtificialData.append(HMI_array)
    if SRType == "HiQ" and HiQ_str != "":
            ArtificialData.append(HiQ_array)
    if SRType == "HighSpeedDigital_IO" and HighSpeedDigital_IO_str != "":
            ArtificialData.append(HighSpeedDigital_IO_array)
    if SRType == "IMAQ" and IMAQ_str != "":
            ArtificialData.append(IMAQ_array)
    if SRType == "IOTech Vibration" and IOTechVibration_str != "":
            ArtificialData.append(IOTechVibration_array)
    if SRType == "Industrial Communications" and IndustrialCommunications_str != "":
            ArtificialData.append(IndustrialCommunications_array)
    if SRType == "InsightCM" and InsightCM_str != "":
            ArtificialData.append(InsightCM_array)
    if SRType == "LV" and LV_str != "":
            ArtificialData.append(LV_array)
    if SRType == "LV CD&Sim" and LVCDSim_str != "":
            ArtificialData.append(LVCDSim_array)
    if SRType == "LV Comms" and LVComms_str != "":
            ArtificialData.append(LVComms_array)
    if SRType == "LV Controls Add-Ons" and LVControls_str != "":
            ArtificialData.append(LVControls_array)
    if SRType == "LV Embedded" and LVEmbedded_str != "":
            ArtificialData.append(LVEmbedded_array)
    if SRType == "LV MathScript RT" and LVMathScriptRT_str != "":
            ArtificialData.append(LVMathScriptRT_array)
    if SRType == "LV NXG" and LVNXG_str != "":
            ArtificialData.append(LVNXG_array)
    if SRType == "LV NXT" and LVNXT_str != "":
            ArtificialData.append(LVNXT_array)
    if SRType == "LVDSC" and LVDSC_str != "":
            ArtificialData.append(LVDSC_array)
    if SRType == "LVFPGA" and LVFPGA_str != "":
            ArtificialData.append(LVFPGA_array)
    if SRType == "LVPDA and LV Touch Panel" and LVPDA_str != "":
            ArtificialData.append(LVPDA_array)
    if SRType == "LVRT" and LVRT_str != "":
            ArtificialData.append(LVRT_array)
    if SRType == "LabWindows_CVI" and LabWindows_CVI_str != "":
            ArtificialData.append(LabWindows_CVI_array)
    if SRType == "Lookout" and Lookout_str != "":
            ArtificialData.append(Lookout_array)
    if SRType == "MATRIXx" and MATRIXx_str != "":
            ArtificialData.append(MATRIXx_array)
    if SRType == "MStudioDotNet" and MStudioDotNet_str != "":
            ArtificialData.append(MStudioDotNet_array)
    if SRType == "MStudioVisualBasic" and MStudioVisualBasic_str != "":
            ArtificialData.append(MStudioVisualBasic_array)
    if SRType == "MStudioVisualC" and FieldBus_str != "":
            ArtificialData.append(MStudioVisualC_array)
    if SRType == "Measure (Legacy)" and Measure_str != "":
            ArtificialData.append(Measure_array)
    if SRType == "Motion" and Motion_str != "":
            ArtificialData.append(Motion_array)
    if SRType == "MultifunctionDAQ" and MultifunctionDAQ_str != "":
            ArtificialData.append(MultifunctionDAQ_array)
    if SRType == "Multimedia Test HW/SW" and MultimediaTest_str != "":
            ArtificialData.append(MultimediaTest_array)
    if SRType == "Multisim (EWB)" and Multisim_str != "":
            ArtificialData.append(Multisim_array)
    if SRType == "NI Update Service" and NIUpdateService_str != "":
            ArtificialData.append(NIUpdateService_array)
    if SRType == "OPC Servers" and OPCServers_str != "":
            ArtificialData.append(OPCServers_array)
    if SRType == "Optical (OSI)" and Optical_str != "":
            ArtificialData.append(Optical_array)
    if SRType == "PXI Controllers, Chassis, MXI" and PXIChassis_str != "":
            ArtificialData.append(PXIChassis_array)
    if SRType == "PXI Timing and Sync" and PXITimingandSync_str != "":
            ArtificialData.append(PXITimingandSync_array)
    if SRType == "Power Supplies and SMUs" and PowerSuppliesandSMUs_str != "":
            ArtificialData.append(PowerSuppliesandSMUs_array)
    if SRType == "Powertrain Controls" and PowertrainControls_str != "":
            ArtificialData.append(PowertrainControls_array)
    if SRType == "RAID" and RAID_str != "":
            ArtificialData.append(RAID_array)
    if SRType == "RF" and RF_str != "":
            ArtificialData.append(RF_array)
    if SRType == "RF Software" and RFSoftware_str != "":
            ArtificialData.append(RFSoftware_array)
    if SRType == "RIO" and RIO_str != "":
            ArtificialData.append(RIO_array)
    if SRType == "SC Express" and SCExpress_str != "":
            ArtificialData.append(SCExpress_array)
    if SRType == "SCC" and SCC_str != "":
            ArtificialData.append(SCC_array)
    if SRType == "SCXI" and SCXI_str != "":
            ArtificialData.append(SCXI_array)
    if SRType == "SPEEDY-33 (Hyperception)" and SPEEDY33_str != "":
            ArtificialData.append(SPEEDY33_array)
    if SRType == "STS" and STS_str != "":
            ArtificialData.append(STS_array)
    if SRType == "ScopesDigitizers" and ScopesDigitizers_str != "":
            ArtificialData.append(ScopesDigitizers_array)
    if SRType == "Serial" and Serial_str != "":
            ArtificialData.append(Serial_array)
    if SRType == "Signal Sources" and SignalSources_str != "":
            ArtificialData.append(SignalSources_array)
    if SRType == "SignalCondOther" and SignalCondOther_str != "":
            ArtificialData.append(SignalCondOther_array)
    if SRType == "SignalExpress" and SignalExpress_str != "":
            ArtificialData.append(SignalExpress_array)
    if SRType == "Software Defined Instruments" and SoftwareDefinedInstruments_str != "":
            ArtificialData.append(SoftwareDefinedInstruments_array)
    if SRType == "Sound and Vibration SW" and SoundandVibrationSW_str != "":
            ArtificialData.append(SoundandVibrationSW_array)
    if SRType == "SwitchExecutive" and SwitchExecutive_str != "":
            ArtificialData.append(SwitchExecutive_array)
    if SRType == "Switches" and Switches_str != "":
            ArtificialData.append(Switches_array)
    if SRType == "SystemLink" and SystemLink_str != "":
            ArtificialData.append(SystemLink_array)
    if SRType == "TestStand" and TestStand_str != "":
            ArtificialData.append(TestStand_array)
    if SRType == "USRP" and USRP_str != "":
            ArtificialData.append(USRP_array)
    if SRType == "Ultiboard (EWB)" and UltiboardEWB_str != "":
            ArtificialData.append(UltiboardEWB_array)
    if SRType == "VBench" and VBench_str != "":
            ArtificialData.append(VBench_array)
    if SRType == "VI Logger" and VILogger_str != "":
            ArtificialData.append(VILogger_array)
    if SRType == "VXI_MXI" and VXI_MXI_str != "":
            ArtificialData.append(VXI_MXI_array)
    if SRType == "VeriStand" and VeriStand_str != "":
            ArtificialData.append(VeriStand_array)
    if SRType == "VisionSW" and VisionSW_str != "":
            ArtificialData.append(VisionSW_array)
    if SRType == "VolumeLicenseMgr" and VolumeLicenseMgr_str != "":
            ArtificialData.append(VolumeLicenseMgr_array)
    if SRType == "WSN" and WSN_str != "":
            ArtificialData.append(WSN_array)
    if SRType == "Web UI Builder" and WebUIBuilder_str != "":
            ArtificialData.append(WebUIBuilder_array)
    if SRType == "myRIO" and myRIO_str != "":
            ArtificialData.append(myRIO_array)
    else:
        pass

# GENERATE HIGH VOLUME SRTYPE TRAINING DATA
CAN_array = []
CMCSeries_array = []
Calibration_array = []
CounterTimer_array = []
DAQExpress_array = []
DIAdem_array = []
DMM_array = []
DSAHW_array = []
Digital_IO_array = []
FIRST_array = []
FieldBus_array = []
FieldPoint_array = []
FlexLogger_array = []
FunctionalSafety_array = []
GATI_array = []
GPIB_array = []
HMI_array = []
HiQ_array = []
HighSpeedDigital_IO_array = []
IMAQ_array = []
IOTechVibration_array = []
IndustrialCommunications_array = []
InsightCM_array = []
LV_array = []
LVCDSim_array = []
LVComms_array = []
LVControls_array = []
LVEmbedded_array = []
LVMathScriptRT_array = []
LVNXG_array = []
LVNXT_array = []
LVDSC_array = []
LVFPGA_array = []
LVPDA_array = []
LVRT_array = []
LabWindows_CVI_array = []
Lookout_array = []
MATRIXx_array = []
MStudioDotNet_array = []
MStudioVisualBasic_array = []
MStudioVisualC_array = []
Measure_array = []
Motion_array = []
MultifunctionDAQ_array = []
MultimediaTest_array = []
Multisim_array = []
NIUpdateService_array = []
OPCServers_array = []
Optical_array = []
PXIChassis_array = []
PXITimingandSync_array = []
PowerSuppliesandSMUs_array = []
PowertrainControls_array = []
RAID_array = []
RF_array = []
RFSoftware_array = []
RIO_array = []
SCExpress_array = []
SCC_array = []
SCXI_array = []
SPEEDY33_array = []
STS_array = []
ScopesDigitizers_array = []
Serial_array = []
SignalSources_array = []
SignalCondOther_array = []
SignalExpress_array = []
SoftwareDefinedInstruments_array = []
SoundandVibrationSW_array = []
SwitchExecutive_array = []
Switches_array = []
SystemLink_array = []
TestStand_array = []
USRP_array = []
UltiboardEWB_array = []
VBench_array = []
VILogger_array = []
VXI_MXI_array = []
VeriStand_array = []
VisionSW_array = []
VolumeLicenseMgr_array = []
WSN_array = []
WebUIBuilder_array = []
myRIO_array = []

CAN = 0
CMCSeries = 0
Calibration = 0
CounterTimer = 0
DAQExpress = 0
DIAdem = 0
DMM = 0
DSAHW = 0
Digital_IO = 0
FIRST = 0
FieldBus = 0
FieldPoint = 0
FlexLogger = 0
FunctionalSafety = 0
GATI = 0
GPIB = 0
HMI = 0
HiQ = 0
HighSpeedDigital_IO = 0
IMAQ = 0
IOTechVibration = 0
IndustrialCommunications = 0
InsightCM = 0
LV = 0
LVCDSim = 0
LVComms = 0
LVControls = 0
LVEmbedded = 0
LVMathScriptRT = 0
LVNXG = 0
LVNXT = 0
LVDSC = 0
LVFPGA = 0
LVPDA = 0
LVRT = 0
LabWindows_CVI = 0
Lookout = 0
MATRIXx = 0
MStudioDotNet = 0
MStudioVisualBasic = 0
MStudioVisualC = 0
Measure = 0
Motion = 0
MultifunctionDAQ = 0
MultimediaTest = 0
Multisim = 0
NIUpdateService = 0
OPCServers = 0
Optical = 0
PXIChassis = 0
PXITimingandSync = 0
PowerSuppliesandSMUs = 0
PowertrainControls = 0
RAID = 0
RF = 0
RFSoftware = 0
RIO = 0
SCExpress = 0
SCC = 0
SCXI = 0
SPEEDY33 = 0
STS = 0
ScopesDigitizers = 0
Serial = 0
SignalSources = 0
SignalCondOther = 0
SignalExpress = 0
SoftwareDefinedInstruments = 0
SoundandVibrationSW = 0
SwitchExecutive = 0
Switches = 0
SystemLink = 0
TestStand = 0
USRP = 0
UltiboardEWB = 0
VBench = 0
VILogger = 0
VXI_MXI = 0
VeriStand = 0
VisionSW = 0
VolumeLicenseMgr = 0
WSN = 0
WebUIBuilder = 0
myRIO = 0

LowData = []

#grab requested number of SRs for high volume SR types
with open(rawtrainingfilelocation, encoding='utf-8', errors='ignore') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for column in readCSV:
        SRData = column[0]
        SRType = column[1]
        if SRType in HighSRs:
            if SRType == "CAN":
                CAN = CAN + 1
                if CAN <= threshold:
                    CAN_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "CM C Series":
                CMCSeries = CMCSeries + 1
                if CMCSeries <= threshold:
                    CMCSeries_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Calibration":
                Calibration = Calibration + 1
                if CMCSeries <= threshold:
                    Calibration_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "CounterTimer":
                CounterTimer = CounterTimer + 1
                if CounterTimer <= threshold:
                    CounterTimer_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "DAQExpress":
                DAQExpress = DAQExpress + 1
                if DAQExpress <= threshold:
                    DAQExpress_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "DIAdem":
                DIAdem = DIAdem + 1
                if DIAdem <= threshold:
                    DIAdem_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "DMM":
                DMM = DMM + 1
                if DMM <= threshold:
                    DMM_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "DSA HW":
                DSAHW = DSAHW + 1
                if DSAHW <= threshold:
                    DSAHW_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Digital_IO":
                Digital_IO = Digital_IO + 1
                if Digital_IO <= threshold:
                    Digital_IO_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "FIRST (NIC Only)":
                FIRST = FIRST + 1
                if FIRST <= threshold:
                    FIRST_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "FieldBus":
                FieldBus = FieldBus + 1
                if FieldBus <= threshold:
                    FieldBus_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "FieldPoint":
                FieldPoint = FieldPoint + 1
                if FieldPoint <= threshold:
                    FieldPoint_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "FlexLogger":
                FlexLogger = FlexLogger + 1
                if FlexLogger <= threshold:
                    FlexLogger_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Functional Safety":
                FunctionalSafety = FunctionalSafety + 1
                if FunctionalSafety <= threshold:
                    FunctionalSafety_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "GATI":
                GATI = GATI + 1
                if GATI <= threshold:
                    GATI_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "GPIB":
                GPIB = GPIB + 1
                if GPIB <= threshold:
                    GPIB_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "HMI and Industrial PCs":
                HMI = HMI + 1
                if HMI <= threshold:
                    HMI_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "HiQ":
                HiQ = HiQ + 1
                if HiQ <= threshold:
                    HiQ_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "HighSpeedDigital_IO":
                HighSpeedDigital_IO = HighSpeedDigital_IO + 1
                if HighSpeedDigital_IO <= threshold:
                    HighSpeedDigital_IO_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "IMAQ":
                IMAQ = IMAQ + 1
                if IMAQ <= threshold:
                    IMAQ_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "IOTech Vibration":
                IOTechVibration = IOTechVibration + 1
                if IOTechVibration <= threshold:
                    IOTechVibration_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Industrial Communications":
                IndustrialCommunications = IndustrialCommunications + 1
                if IndustrialCommunications <= threshold:
                    IndustrialCommunications_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "InsightCM":
                InsightCM = InsightCM + 1
                if InsightCM <= threshold:
                    InsightCM_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "LV":
                LV = LV + 1
                if LV <= threshold:
                    LV_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "LV CD&Sim":
                LVCDSim = LVCDSim + 1
                if LVCDSim <= threshold:
                    LVCDSim_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "LV Comms":
                LVComms = LVComms + 1
                if LVComms <= threshold:
                    LVComms_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "LV Controls Add-Ons":
                LVControls = LVControls + 1
                if LVControls <= threshold:
                    LVControls_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "LV Embedded":
                LVEmbedded = LVEmbedded + 1
                if LVEmbedded <= threshold:
                    LVEmbedded_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "LV MathScript RT":
                LVMathScriptRT = LVMathScriptRT + 1
                if LVMathScriptRT <= threshold:
                    LVMathScriptRT_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "LV NXG":
                LVNXG = LVNXG + 1
                if LVNXG <= threshold:
                    LVNXG_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "LV NXT":
                LVNXT = LVNXT + 1
                if LVNXT <= threshold:
                    LVNXT_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "LVDSC":
                LVDSC = LVDSC + 1
                if LVDSC <= threshold:
                    LVDSC_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "LVFPGA":
                LVFPGA = LVFPGA + 1
                if LVFPGA <= threshold:
                    LVFPGA_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "LVPDA and LV Touch Panel":
                LVPDA = LVPDA + 1
                if LVPDA <= threshold:
                    LVPDA_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "LVRT":
                LVRT = LVRT + 1
                if LVRT <= threshold:
                    LVRT_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "LabWindows_CVI":
                LabWindows_CVI = LabWindows_CVI + 1
                if LabWindows_CVI <= threshold:
                    LabWindows_CVI_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Lookout":
                Lookout = Lookout + 1
                if Lookout <= threshold:
                    Lookout_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "MATRIXx":
                MATRIXx = MATRIXx + 1
                if MATRIXx <= threshold:
                    MATRIXx_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "MStudioDotNet":
                MStudioDotNet = MStudioDotNet + 1
                if MStudioDotNet <= threshold:
                    MStudioDotNet_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "MStudioVisualBasic":
                MStudioVisualBasic = MStudioVisualBasic + 1
                if MStudioVisualBasic <= threshold:
                    MStudioVisualBasic_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "MStudioVisualC":
                MStudioVisualC = MStudioVisualC + 1
                if MStudioVisualC <= threshold:
                    MStudioVisualC_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Measure (Legacy)":
                Measure = Measure + 1
                if Measure <= threshold:
                    Measure_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Motion":
                Motion = Motion + 1
                if Motion <= threshold:
                    Motion_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "MultifunctionDAQ":
                MultifunctionDAQ = MultifunctionDAQ + 1
                if MultifunctionDAQ <= threshold:
                    MultifunctionDAQ_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Multimedia Test HW/SW":
                MultimediaTest = MultimediaTest + 1
                if MultimediaTest <= threshold:
                    MultimediaTest_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Multisim (EWB)":
                Multisim = Multisim + 1
                if Multisim <= threshold:
                    Multisim_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "NI Update Service":
                NIUpdateService = NIUpdateService + 1
                if NIUpdateService <= threshold:
                    NIUpdateService_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "OPC Servers":
                OPCServers = OPCServers + 1
                if OPCServers <= threshold:
                    OPCServers_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Optical (OSI)":
                Optical = Optical + 1
                if Optical <= threshold:
                    Optical_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "PXI Controllers, Chassis, MXI":
                PXIChassis = PXIChassis + 1
                if PXIChassis <= threshold:
                    PXIChassis_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "PXI Timing and Sync":
                PXITimingandSync = PXITimingandSync + 1
                if PXITimingandSync <= threshold:
                    PXITimingandSync_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Power Supplies and SMUs":
                PowerSuppliesandSMUs = PowerSuppliesandSMUs + 1
                if PowerSuppliesandSMUs <= threshold:
                    PowerSuppliesandSMUs_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Powertrain Controls":
                PowertrainControls = PowertrainControls + 1
                if PowertrainControls <= threshold:
                    PowertrainControls_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "RAID":
                RAID = RAID + 1
                if RAID <= threshold:
                    RAID_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "RF":
                RF = RF + 1
                if RF <= threshold:
                    RF_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "RF Software":
                RFSoftware = RFSoftware + 1
                if RFSoftware <= threshold:
                    RFSoftware_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "RIO":
                RIO = RIO + 1
                if RIO <= threshold:
                    RIO_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "SC Express":
                SCExpress = SCExpress + 1
                if SCExpress <= threshold:
                    SCExpress_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "SCC":
                SCC = SCC + 1
                if SCC <= threshold:
                    SCC_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "SCXI":
                SCXI = SCXI + 1
                if SCXI <= threshold:
                    SCXI_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "SPEEDY-33 (Hyperception)":
                SPEEDY33 = SPEEDY33 + 1
                if SPEEDY33 <= threshold:
                    SPEEDY33_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "STS":
                STS = STS + 1
                if STS <= threshold:
                    STS_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "ScopesDigitizers":
                ScopesDigitizers = ScopesDigitizers + 1
                if ScopesDigitizers <= threshold:
                    ScopesDigitizers_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Serial":
                Serial = Serial + 1
                if Serial <= threshold:
                    Serial_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Signal Sources":
                SignalSources = SignalSources + 1
                if SignalSources <= threshold:
                    SignalSources_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "SignalCondOther":
                SignalCondOther = SignalCondOther + 1
                if SignalCondOther <= threshold:
                    SignalCondOther_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "SignalExpress":
                SignalExpress = SignalExpress + 1
                if SignalExpress <= threshold:
                    SignalExpress_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Software Defined Instruments":
                SoftwareDefinedInstruments = SoftwareDefinedInstruments + 1
                if SoftwareDefinedInstruments <= threshold:
                    SoftwareDefinedInstruments_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Sound and Vibration SW":
                SoundandVibrationSW = SoundandVibrationSW + 1
                if SoundandVibrationSW <= threshold:
                    SoundandVibrationSW_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "SwitchExecutive":
                SwitchExecutive = SwitchExecutive + 1
                if SwitchExecutive <= threshold:
                    SwitchExecutive_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Switches":
                Switches = Switches + 1
                if Switches <= threshold:
                    SwitchExecutive_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "SystemLink":
                SystemLink = SystemLink + 1
                if SystemLink <= threshold:
                    SystemLink_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "TestStand":
                TestStand = TestStand + 1
                if TestStand <= threshold:
                    TestStand_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "USRP":
                USRP = USRP + 1
                if USRP <= threshold:
                    USRP_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Ultiboard (EWB)":
                UltiboardEWB = UltiboardEWB + 1
                if UltiboardEWB <= threshold:
                    UltiboardEWB_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "VBench":
                VBench = VBench + 1
                if VBench <= threshold:
                    VBench_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "VI Logger":
                VILogger = VILogger + 1
                if VILogger <= threshold:
                    VILogger_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "VXI_MXI":
                VXI_MXI = VXI_MXI + 1
                if VXI_MXI <= threshold:
                    VXI_MXI_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "VeriStand":
                VeriStand = VeriStand + 1
                if VeriStand <= threshold:
                    VeriStand_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "VisionSW":
                VisionSW = VisionSW + 1
                if VisionSW <= threshold:
                    VisionSW_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "VolumeLicenseMgr":
                VolumeLicenseMgr = VolumeLicenseMgr + 1
                if VolumeLicenseMgr <= threshold:
                    VolumeLicenseMgr_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "WSN":
                WSN = WSN + 1
                if WSN <= threshold:
                    WSN_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "Web UI Builder":
                WebUIBuilder = WebUIBuilder + 1
                if WebUIBuilder <= threshold:
                    WebUIBuilder_array.append([SRData, SRType])
                else:
                    pass
            if SRType == "myRIO":
                myRIO = myRIO + 1
                if myRIO <= threshold:
                    myRIO_array.append([SRData, SRType])
                else:
                    pass
        else:
            LowData.append([SRData, SRType])

#create an array of the SRType arrays
array = np.array([
    CAN_array,
    CMCSeries_array,
    Calibration_array,
    CounterTimer_array,
    DAQExpress_array,
    DIAdem_array,
    DMM_array,
    DSAHW_array,
    Digital_IO_array,
    FIRST_array,
    FieldBus_array,
    FieldPoint_array,
    FlexLogger_array,
    FunctionalSafety_array,
    GATI_array,
    GPIB_array,
    HMI_array,
    HiQ_array,
    HighSpeedDigital_IO_array,
    IMAQ_array,
    IOTechVibration_array,
    IndustrialCommunications_array,
    InsightCM_array,
    LV_array,
    LVCDSim_array,
    LVComms_array,
    LVControls_array,
    LVEmbedded_array,
    LVMathScriptRT_array,
    LVNXG_array,
    LVNXT_array,
    LVDSC_array,
    LVFPGA_array,
    LVPDA_array,
    LVRT_array,
    LabWindows_CVI_array,
    Lookout_array,
    MATRIXx_array,
    MStudioDotNet_array,
    MStudioVisualBasic_array,
    MStudioVisualC_array,
    Measure_array,
    Motion_array,
    MultifunctionDAQ_array,
    MultimediaTest_array,
    Multisim_array,
    NIUpdateService_array,
    OPCServers_array,
    Optical_array,
    PXIChassis_array,
    PXITimingandSync_array,
    PowerSuppliesandSMUs_array,
    PowertrainControls_array,
    RAID_array,
    RF_array,
    RFSoftware_array,
    RIO_array,
    SCExpress_array,
    SCC_array,
    SCXI_array,
    SPEEDY33_array,
    STS_array,
    ScopesDigitizers_array,
    Serial_array,
    SignalSources_array,
    SignalCondOther_array,
    SignalExpress_array,
    SoftwareDefinedInstruments_array,
    SoundandVibrationSW_array,
    SwitchExecutive_array,
    Switches_array,
    SystemLink_array,
    TestStand_array,
    USRP_array,
    UltiboardEWB_array,
    VBench_array,
    VILogger_array,
    VXI_MXI_array,
    VeriStand_array,
    VisionSW_array,
    VolumeLicenseMgr_array,
    WSN_array,
    WebUIBuilder_array,
    myRIO_array])

#create 2d array of all SRTypes that were maxed at the threshold
BigTraining = []
for i in range(len(array)):
    if len(array[i]) == threshold:
        BigTraining.extend(array[i])

#add the data that is less than the threshold
BigTraining.extend(LowData)
RealData = BigTraining

#merge artificial and big training data to create equal weighted data
RealData.extend(ArtificialData)
TrainingData = RealData

#write training data to a spreadsheet
with open(trainingfilelocation, mode='w+', newline='', encoding='utf-8') as CSVtoWrite:
    csvWriter = csv.writer(CSVtoWrite, delimiter=',')
    csvWriter.writerows(TrainingData)

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
with open(testfilelocation, encoding='utf-8', errors='replace') as testfile:
    readCSV = csv.reader(testfile, delimiter=',')
    TestDataArray=[]
    TestSRTypeArray=[]
    for column in readCSV:
         TestData = column[0]
         TestSRType = column[1]
         TestSRTypeArray.append(TestSRType)
         TestDataArray.append(TestData)
test_data = TestDataArray
test_target = TestSRTypeArray

#initialize SRType counts
CAN = 0
CMCSeries = 0
Calibration = 0
CounterTimer = 0
DAQExpress = 0
DIAdem = 0
DMM = 0
DSAHW = 0
Digital_IO = 0
FIRST = 0
FieldBus = 0
FieldPoint = 0
FlexLogger = 0
FunctionalSafety = 0
GATI = 0
GPIB = 0
HMI = 0
HiQ = 0
HighSpeedDigital_IO = 0
IMAQ = 0
IOTechVibration = 0
IndustrialCommunications = 0
InsightCM = 0
LV = 0
LVCDSim = 0
LVComms = 0
LVControls = 0
LVEmbedded = 0
LVMathScriptRT = 0
LVNXG = 0
LVNXT = 0
LVDSC = 0
LVFPGA = 0
LVPDA = 0
LVRT = 0
LabWindows_CVI = 0
Lookout = 0
MATRIXx = 0
MStudioDotNet = 0
MStudioVisualBasic = 0
MStudioVisualC = 0
Measure = 0
Motion = 0
MultifunctionDAQ = 0
MultimediaTest = 0
Multisim = 0
NIUpdateService = 0
OPCServers = 0
Optical = 0
PXIChassis = 0
PXITimingandSync = 0
PowerSuppliesandSMUs = 0
PowertrainControls = 0
RAID = 0
RF = 0
RFSoftware = 0
RIO = 0
SCExpress = 0
SCC = 0
SCXI = 0
SPEEDY33 = 0
STS = 0
ScopesDigitizers = 0
Serial = 0
SignalSources = 0
SignalCondOther = 0
SignalExpress = 0
SoftwareDefinedInstruments = 0
SoundandVibrationSW = 0
SwitchExecutive = 0
Switches = 0
SystemLink = 0
TestStand = 0
USRP = 0
UltiboardEWB = 0
VBench = 0
VILogger = 0
VXI_MXI = 0
VeriStand = 0
VisionSW = 0
VolumeLicenseMgr = 0
WSN = 0
WebUIBuilder = 0
myRIO = 0

target_names = []
for i in test_target:
    SRType = i
    if SRType == "CAN":
        CAN = CAN + 1
    if SRType == "CM C Series":
        CMCSeries = CMCSeries + 1
    if SRType == "Calibration":
        Calibration = Calibration + 1
    if SRType == "CounterTimer":
        CounterTimer = CounterTimer + 1
    if SRType == "DAQExpress":
        DAQExpress = DAQExpress + 1
    if SRType == "DIAdem":
        DIAdem = DIAdem + 1
    if SRType == "DMM":
        DMM = DMM + 1
    if SRType == "DSA HW":
        DSAHW = DSAHW + 1
    if SRType == "Digital_IO":
        Digital_IO = Digital_IO + 1
    if SRType == "FIRST (NIC Only)":
        FIRST = FIRST + 1
    if SRType == "FieldBus":
        FieldBus = FieldBus + 1
    if SRType == "FieldPoint":
        FieldPoint = FieldPoint + 1
    if SRType == "FlexLogger":
        FlexLogger = FlexLogger + 1
    if SRType == "Functional Safety":
        FunctionalSafety = FunctionalSafety + 1
    if SRType == "GATI":
        GATI = GATI + 1
    if SRType == "GPIB":
        GPIB = GPIB + 1
    if SRType == "HMI and Industrial PCs":
        HMI = HMI + 1
    if SRType == "HiQ":
        HiQ = HiQ + 1
    if SRType == "HighSpeedDigital_IO":
        HighSpeedDigital_IO = HighSpeedDigital_IO + 1
    if SRType == "IMAQ":
        IMAQ = IMAQ + 1
    if SRType == "IOTech Vibration":
        IOTechVibration = IOTechVibration + 1
    if SRType == "Industrial Communications":
        IndustrialCommunications = IndustrialCommunications + 1
    if SRType == "InsightCM":
        InsightCM = InsightCM + 1
    if SRType == "LV":
        LV = LV + 1
    if SRType == "LV CD&Sim":
        LVCDSim = LVCDSim + 1
    if SRType == "LV Comms":
        LVComms = LVComms + 1
    if SRType == "LV Controls Add-Ons":
        LVControls = LVControls + 1
    if SRType == "LV Embedded":
        LVEmbedded = LVEmbedded + 1
    if SRType == "LV MathScript RT":
        LVMathScriptRT = LVMathScriptRT + 1
    if SRType == "LV NXG":
        LVNXG = LVNXG + 1
    if SRType == "LV NXT":
        LVNXT = LVNXT + 1
    if SRType == "LVDSC":
        LVDSC = LVDSC + 1
    if SRType == "LVFPGA":
        LVFPGA = LVFPGA + 1
    if SRType == "LVPDA and LV Touch Panel":
        LVPDA = LVPDA + 1
    if SRType == "LVRT":
        LVRT = LVRT + 1
    if SRType == "LabWindows_CVI":
        LabWindows_CVI = LabWindows_CVI + 1
    if SRType == "Lookout":
        Lookout = Lookout + 1
    if SRType == "MATRIXx":
        MATRIXx = MATRIXx + 1
    if SRType == "MStudioDotNet":
        MStudioDotNet = MStudioDotNet + 1
    if SRType == "MStudioVisualBasic":
        MStudioVisualBasic = MStudioVisualBasic + 1
    if SRType == "MStudioVisualC":
        MStudioVisualC = MStudioVisualC + 1
    if SRType == "Measure (Legacy)":
        Measure = Measure + 1
    if SRType == "Motion":
        Motion = Motion + 1
    if SRType == "MultifunctionDAQ":
        MultifunctionDAQ = MultifunctionDAQ + 1
    if SRType == "Multimedia Test HW/SW":
        MultimediaTest = MultimediaTest + 1
    if SRType == "Multisim (EWB)":
        Multisim = Multisim + 1
    if SRType == "NI Update Service":
        NIUpdateService = NIUpdateService + 1
    if SRType == "OPC Servers":
        OPCServers = OPCServers + 1
    if SRType == "Optical (OSI)":
        Optical = Optical + 1
    if SRType == "PXI Controllers, Chassis, MXI":
        PXIChassis = PXIChassis + 1
    if SRType == "PXI Timing and Sync":
        PXITimingandSync = PXITimingandSync + 1
    if SRType == "Power Supplies and SMUs":
        PowerSuppliesandSMUs = PowerSuppliesandSMUs + 1
    if SRType == "Powertrain Controls":
        PowertrainControls = PowertrainControls + 1
    if SRType == "RAID":
        RAID = RAID + 1
    if SRType == "RF":
        RF = RF + 1
    if SRType == "RF Software":
        RFSoftware = RFSoftware + 1
    if SRType == "RIO":
        RIO = RIO + 1
    if SRType == "SC Express":
        SCExpress = SCExpress + 1
    if SRType == "SCC":
        SCC = SCC + 1
    if SRType == "SCXI":
        SCXI = SCXI + 1
    if SRType == "SPEEDY-33 (Hyperception)":
        SPEEDY33 = SPEEDY33 + 1
    if SRType == "STS":
        STS = STS + 1
    if SRType == "ScopesDigitizers":
        ScopesDigitizers = ScopesDigitizers + 1
    if SRType == "Serial":
        Serial = Serial + 1
    if SRType == "Signal Sources":
        SignalSources = SignalSources + 1
    if SRType == "SignalCondOther":
        SignalCondOther = SignalCondOther + 1
    if SRType == "SignalExpress":
        SignalExpress = SignalExpress + 1
    if SRType == "Software Defined Instruments":
        SoftwareDefinedInstruments = SoftwareDefinedInstruments + 1
    if SRType == "Sound and Vibration SW":
        SoundandVibrationSW = SoundandVibrationSW + 1
    if SRType == "SwitchExecutive":
        SwitchExecutive = SwitchExecutive + 1
    if SRType == "Switches":
        Switches = Switches + 1
    if SRType == "SystemLink":
        SystemLink = SystemLink + 1
    if SRType == "TestStand":
        TestStand = TestStand + 1
    if SRType == "USRP":
        USRP = USRP + 1
    if SRType == "Ultiboard (EWB)":
        UltiboardEWB = UltiboardEWB + 1
    if SRType == "VBench":
        VBench = VBench + 1
    if SRType == "VI Logger":
        VILogger = VILogger + 1
    if SRType == "VXI_MXI":
        VXI_MXI = VXI_MXI + 1
    if SRType == "VeriStand":
        VeriStand = VeriStand + 1
    if SRType == "VisionSW":
        VisionSW = VisionSW + 1
    if SRType == "VolumeLicenseMgr":
        VolumeLicenseMgr = VolumeLicenseMgr + 1
    if SRType == "WSN":
        WSN = WSN + 1
    if SRType == "Web UI Builder":
        WebUIBuilder = WebUIBuilder + 1
    if SRType == "myRIO":
        myRIO = myRIO + 1
    else:
        pass

#create array of counts
SRTypeCounts = np.array([
    CAN,
    CMCSeries,
    Calibration,
    CounterTimer,
    DAQExpress,
    DIAdem,
    DMM,
    DSAHW,
    Digital_IO,
    FIRST,
    FieldBus,
    FieldPoint,
    FlexLogger,
    FunctionalSafety,
    GATI,
    GPIB,
    HMI,
    HiQ,
    HighSpeedDigital_IO,
    IMAQ,
    IOTechVibration,
    IndustrialCommunications,
    InsightCM,
    LV,
    LVCDSim,
    LVComms,
    LVControls,
    LVEmbedded,
    LVMathScriptRT,
    LVNXG,
    LVNXT,
    LVDSC,
    LVFPGA,
    LVPDA,
    LVRT,
    LabWindows_CVI,
    Lookout,
    MATRIXx,
    Measure,
    MStudioDotNet,
    MStudioVisualBasic,
    MStudioVisualC,
    Motion,
    MultifunctionDAQ,
    MultimediaTest,
    Multisim,
    NIUpdateService,
    OPCServers,
    Optical,
    PXIChassis,
    PXITimingandSync,
    PowerSuppliesandSMUs,
    PowertrainControls,
    RAID,
    RF,
    RFSoftware,
    RIO,
    SCExpress,
    SCC,
    SCXI,
    SPEEDY33,
    STS,
    ScopesDigitizers,
    Serial,
    SignalSources,
    SignalCondOther,
    SignalExpress,
    SoftwareDefinedInstruments,
    SoundandVibrationSW,
    SwitchExecutive,
    Switches,
    SystemLink,
    TestStand,
    USRP,
    UltiboardEWB,
    VBench,
    VILogger,
    VXI_MXI,
    VeriStand,
    VisionSW,
    VolumeLicenseMgr,
    WSN,
    WebUIBuilder,
    myRIO
])

#categorize SR types by if they have sufficient data
for i in range(len(SRTypeCounts)):
    if SRTypeCounts[i] > 0:
        target_names.append(SRTypes[i])
    else:
        pass

#add stop words
my_stop_words = text.ENGLISH_STOP_WORDS.union(["cost", "solution", "help", "question", "thanks", "please"])

#create model
vectorizer = TfidfVectorizer(decode_error= 'ignore', stop_words= my_stop_words)
NB = MultinomialNB(fit_prior=True, alpha=1)
model = make_pipeline(vectorizer, NB)
classifier = model.fit(train_data, train_target)
predicted = model.predict(test_data)

#get features with highest coefficients for each type
class_labels=NB.classes_
print(class_labels)
top_features = []
feature_names = vectorizer.get_feature_names()
for i, class_label in enumerate(classes):
    top10 = np.argsort(NB.coef_[i])[-10:]
    print("%s: %s" % (class_label,
          " ".join(feature_names[j] for j in top10)))

#write correct vs. predicted data to file
results = []
results.append(["Actual SR Type", "Predicted", "Data"])
for i in range(len(predicted)):
    results.append([test_target[i], predicted[i], test_data[i]])

#create results file
with open(predictionresultsfile, mode='w+', newline='', encoding='utf-8') as CSVtoWrite:
    csvWriter = csv.writer(CSVtoWrite, delimiter=',')
    csvWriter.writerows(results)

#determine accuracy of model
print("Accuracy is " + str(accuracy_score(test_target, predicted)*100) + "%")
print(metrics.classification_report(test_target, predicted, target_names=target_names, labels=target_names))
