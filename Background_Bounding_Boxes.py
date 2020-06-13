import numpy as np
import argparse 
import cv2
import os
import shutil
import PIL
import random

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
        help="path to input image")
ap.add_argument("-c", "--coun", required=True,
        help="no of bounding boxes")


args = vars(ap.parse_args())
count=int(args["coun"])
image = cv2.imread("input")
dirname = args["input"]
for file in sorted(os.listdir(dirname)):
        if(file.split(".")[1]=="jpg"):
                img_org = cv2.imread(dirname+file)
                h,w,c=(img_org.shape)
                f= open(dirname+file.split(".")[0]+".txt","r")
                lines = f.readlines()
                b_no=len(lines)
                fdata=[w,h,len(lines)]
                a=[fdata]
                f.close()
                for line in lines:
                        
                        CC=line.split(" ")[0]
                        C = int(CC)
                        Cx=int(float(line.split(" ")[1])*w)
                        Cy=int(float(line.split(" ")[2])*h)
                        Cwid=int(float(line.split(" ")[3])*w)
                        Cheg=int(float(line.split(" ")[4])*h)
                        sx=int(Cx-(Cwid/2))
                        ex=int(Cx+(Cwid/2))
                        sy=int(Cy-(Cheg/2))
                        ey=int(Cy+(Cheg/2))
                        b=[sx,sy,ex,ey]
                        a.append(b)
                for j in range (0,count):
                        flag=True
                        while(flag==True):
                                
                                nl.append(random.randint(0,w))
                                nl.append(random.randint(0,h))
                                nl.append(random.randint(nl[0],w))
                                nl.append(random.randint(nl[1],h))
                                i=1
                                for i in range(1,len(a)):
                                        
                                        flag=False
                                        
                                                
                                        xs=a[i][0]   #Start x coordinate of i^th bounding box
                                        ys=a[i][1]   #Start y coordinate of i^th bounding box
                                        xe=a[i][2]   #End x coordinate of i^th bounding box
                                        ye=a[i][3]   #End y coordinate of i^th bounding box
					l=[xs,ys,xe,ye]
                                        #if((Nendy<ys) or (Nendx<xs) or (Nstarty>ye) or  (Nstartx>xe)):
                                        #        asd=2
                                        #else:
                                        #        asd=1
                                        #        flag=True
                                        #        break
					f=comp(l,nl)
					if(f == False):
						del nl[0:3]
						del l[0:3]
						break
                                        
                                if():
                                        
                                        #b=[Nstartx,Nstarty,Nendx,Nendy]
                                        
                                        a.append(nl)
               



                w=a[0][2]
                for i in range(w+1,len(a)):
                        xs=a[i][0]   #Start x coordinate of i^th bounding box
                        ys=a[i][1]   #Start y coordinate of i^th bounding box
                        xe=a[i][2]   #End x coordinate of i^th bounding box
                        ye=a[i][3] 

                        xnorm1=((xs+xe)/2)
                        ynorm1=((ys+ye)/2)
                        xnorm=(xnorm1/a[0][0])
                        ynorm=(ynorm1/a[0][1])
                        wid=((xe-xs)/a[0][0])
                        heig=((ye-ys)/a[0][1])
                        su=str(3)+" "+str(xnorm)+" "+str(ynorm)+" "+str(wid)+" "+str(heig)
                        f=open(dirname+file.split(".")[0]+".txt","a")
                        f.write(su+"\n")
                        f.close()
                        
                        
def comp(l,nl):
	dxs=l[0]
	dys=l[1]
	dxe=l[2]
	dye=l[3]
	dnxs=nl[0]
	dnys=nl[1]
	dnxe=nl[2]
	dnye=nl[3]
	if((dnye<dys) or (dnxe<dxs) or (dnys>dye) or  (dnxs>dxe)): #Condition to compare the bounding boxes
		f=True
	else:
		f=False
	return f
	
                                              
                
