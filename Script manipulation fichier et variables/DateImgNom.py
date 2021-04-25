import os
import time
list=['.png','.jpg', '.jpeg', '.tif', '.tga']
folder_path = "/Users/macbookpro/Documents/Image"

for root, dirs, files in os.walk(folder_path):
 #f = open('IMG4.txt',"w")
 for fileName in files:
 	z = os.path.splitext(fileName[0])
 if fileName.endswith(tuple(list)):
  a = os.path.getctime(folder_path)
      
print (a)
b = time.ctime(a)
b.replace(':',"_")

for root, dirs, files in os.walk(folder_path):
 #f = open('IMG4.txt',"w")
 for fileName in files:
  os.rename(fileName, fileName.replace(str(z), str(b)))

#with open(fileName,'r') as d:
#print (a)
#print (d)