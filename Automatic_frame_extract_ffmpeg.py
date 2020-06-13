import glob
import os
path="./folder1/"
parent path="./folder2/"

for d in glob.glob(parent_path+"*"):
    print(d)
    str=d.split("/")[-1]
    print(str)
    str1=str.split(".")[0]
    img_name=path+str1+"_Frames/"+str1+"_%05d.jpg"
    print(img_name)
    os.makedirs(path+str1+"_Frames")
    os.system("ffmpeg -i "+d+"-r 1/20 "+img_name)
