
import os
import glob
from xml.etree import cElementTree as ET

class XmlDictConfig(list):
    def __init__(self, aList):
        for element in aList:
            if element:
                # treat like dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(XmlDictConfig(element))
                # treat like list
                elif element[0].tag == element[1].tag:
                    self.append(XmlListConfig(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)


filenames= glob.glob('./*.xml')
width = 1920
height = 1080
d=1
for f in filenames :
	
	g=f.split('.')[0] + ".txt"
	tree = ET.parse(f)
	root = tree.getroot()
	file=open(g,'w')
	xmldict = XmlDictConfig(root)
	i = 6	
	while (i>=6) and (i<len(xmldict)) :
		
		val=xmldict[i][0]
		#Bounding box coordinates in xml file
		x1=int(xmldict[i][4][0])
		y1=int(xmldict[i][4][1])
		x2=int(xmldict[i][4][2])
		y2=int(xmldict[i][4][3])
		cx='{0:.6f}'.format((x1+x2)/(2*width))		
		cy='{0:.6f}'.format((y1+y2)/(2*height))
		pw='{0:.6f}'.format((x2-x1)/width)
		ph='{0:.6f}'.format((y2-y1)/height)

		#Based on target variable (full,bald or headgear), assigning a numerix tag(0,1,2)
		#And writing in the txt file
		if(val=='full') :
			p='0'
			file.write(p + " " + cx + " " + cy + " " + pw + " " + ph + "\n")
			
		if(val=='bald') :
			p='1'
			file.write(p + " " + cx + " " + cy + " " + pw + " " + ph + "\n")
			
		if(val=='headgear') :
			p='2'
			file.write(p + " " + cx + " " + cy + " " + pw + " " + ph + "\n")
			
		
		
	
		i=i+1
	os.remove(f)
	d=d+1	
	print(d)

