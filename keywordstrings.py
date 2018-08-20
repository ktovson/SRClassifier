import csv
import numpy as np

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

with open(r'C:\Users\ktovson\Desktop\SR Classifier Project\SRData\Keywords.csv', encoding='utf-8') as csvfile:
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

KeywordStrings = []
for column in Output:
    SRData = column[0]
    SRType = column[1]
    if SRData == "":
        pass
    else:
        KeywordStrings.append([SRData, SRType])

with open(r"C:\Users\ktovson\Desktop\SR Classifier Project\SRData\Keywordstrings.csv", mode='w+', newline='', encoding='utf-8') as CSVtoWrite:
    csvWriter = csv.writer(CSVtoWrite, delimiter=',')
    csvWriter.writerows(Output2)
