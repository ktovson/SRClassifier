# import libraries
import urllib.request
from bs4 import BeautifulSoup

def GetProblemDescription(SR_Number):

        # specify the URL
        SR_URL = "http://force.natinst.com:8000/pls/ebiz/niae_screenpop.main?p_incident_number="+str(SR_Number)+"&p_contact_number="

        # query website and return html to variable 'page'
        page = urllib.request.urlopen(SR_URL)

        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page, 'html.parser')

        # find the last Problem Description tag
        description_label = soup.find_all("td", string="Problem Description")[-1]

        # locate the tag for problem description data
        description_parent = description_label.find_all_next("td")[2]

        # acquire text
        description = description_parent.renderContents()

        # trim the space off text
        description_strip = description.strip()

        # remove break line tags
        break1 =description_strip.replace(b'<br/>',b'')
        break2=break1.replace(b'\r',b'')
        SR_Description = break2

        return str(SR_Description, 'utf-8')