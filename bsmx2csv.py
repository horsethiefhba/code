# Beersmith to Excel (CSV):

__author__ = "Charles Toepfer"
__copyright__ = ""
__credits__ = [""]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = ""
__email__ = "charles.toepfer@gmail.com"
__status__ = "Test"

import csv
from bs4 import BeautifulSoup

infile = 'C:\Program Files (x86)\BeerSmith3\Grain.bsmx'
outfile = 'grains.csv'

# Open and read the XML file
with open(infile, 'r') as file:
    xml = file.read()

# Use BeautifulSoup to parse the XML
soup = BeautifulSoup(xml, 'xml')
# Get the root element
root = soup.find()
# Get the name of the root element
rootelename = root.name
headwriten = False

# Creating a CSV file 
with open(outfile, mode='w', newline='') as csv_file:
    #Iterate through each Data tag
    for datatags in soup.find_all('Data'):
        #Iterate through each root element named tag
        for elemtag in datatags.find_all(rootelename):
            fieldnames = []
            data = {}
            csvdata = []
            # Iterating through each subnode of the grain
            for child in elemtag.children:
                fieldnames.append(child.name)
                data[child.name] = child.text.replace('\n', '')
                csvdata.append(child.text)
            # Create a CSV writer
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            # Write header
            if not headwriten:
                writer.writeheader()
                headwriten = True
            # Write data
            writer.writerow(data)

# Print contents of CSV:
with open(outfile, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)