import os
import random
import lxml.etree as ET
import lxml.builder import E
somepath="./1/"
XMIN=1335
YMIN=449
XMAX=1376
YMAX=510
for (dirpath,dirnames,filenames) in walk(some_path):
    for item in filenames:
        xmin1=XMIN+random.randint(-10,10)
        ymin1=YMIN+random.randint(-5,5)
        xmax1=XMAX+random.randint(-10,10)
        ymax1=YMAX+random.randint(-5,5)
        p=dirpath+item
        file=(
            E.annotation(
                E.folder("1"),
                E,filename(item),
                E.path(p),
                E.source(
                    E.database("Unknown")
                    ),
                E.size(
                    E.width("1920"),
                    E.height("1090"),
                    E.depth("3")
                    )
                E.segmented("0"),
                E.object(
                    E.name("reference"),
                    E.pose("Unspecified"),
                    E.truncated("0"),
                    E.difficult("0"),
                    E.bnd_box(
                        E.xmin(str(xmin1)),
                        E.ymin(str(ymin1)),
                        E.xmax(str(xmax1)),
                        E.ymax(str(ymax1))
                        )
                    )
                )
            )
        XML_data=ET.tostring(file)
        XML_data=XML_data.decode("utf-8")
        fname=dirpath+str(item.split(".")[0])+".xml"
        print(fname)
        f=open(fname,"w+")
        f.write(str(XML_data))
        
        
