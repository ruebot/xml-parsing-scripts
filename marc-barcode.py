'''
Make lots of marc xml files from one big marcxml file
using the barcode as the filename.
'''

from xml.etree import ElementTree
import xml.dom.minidom

ElementTree.register_namespace('marc','http://www.loc.gov/MARC21/slim')

f = open("FOO.xml", "r")
tree = ElementTree.parse(f)
root = tree.getroot()

ns = '{http://www.loc.gov/MARC21/slim}'
records = root.iter(ns+'record')
#print records

for record in records:
    identifier = record.find('./'+ns+'datafield[@tag="999"]/'+ns+'subfield[@code="i"]').text
    outfile = file(identifier + "_MARC.xml", "w")
    print "Trying to write " + identifier + "_MARC.xml..."
    outfile.write(ElementTree.tostring(record).encode('utf-8'))
    outfile.close()
