### IMPORT LIBRARIES ###
import urllib.request
from bs4 import BeautifulSoup

def GetHardware(SR_Number):

                ### PARSE HTML WITH SOUP ###

                # specify the URL
                SR_URL = "http://force.natinst.com:8000/pls/ebiz/niae_screenpop.main?p_incident_number="+str(SR_Number)+"&p_contact_number="

                # query website and return html to variable 'page'
                page = urllib.request.urlopen(SR_URL)

                # parse the html using beautiful soup and store in variable `soup`
                soup = BeautifulSoup(page, 'html.parser')

                ### SOFTWARE ###

                # find the last SR Created on the Web tag
                Web_label = soup.find_all("td", string="SR Created on the Web")[-1]

                # locate the tag for problem description data
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

                # get listed hardware
                HardwareIndex = Web_Data.find(HardwareString)
                OSIndex = Web_Data.find(OSString)
                Hardware_raw = Web_Data[HardwareIndex + 10:OSIndex]

                # remove free form entry str
                Hardware = Hardware_raw.replace("(Free form entry)", "")

                return(Hardware)