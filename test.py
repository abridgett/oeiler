#!/usr/bin/env python3

import oeiler
import re
from xml.etree import ElementTree as ET


#oeiler.getxml_legal('chris.xml')
#tree = ET.parse('chris.xml')

#oeiler.getxml_all('all.xml')

tree = ET.parse('all.xml')

root = tree.getroot()
print (root)

#data = root.find('procedureList')
count = 0
for item in tree.iter(tag='item'):
    #print ("ITEM=",item)
    ref = item.find('reference').text
    title = item.find('title').text
    title = re.sub("\n", " ", title)
    print("%s, %s" % (ref, title))
    count += 1

print("Total items = ", count)
