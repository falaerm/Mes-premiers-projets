import os
import time
list=['.png','.jpg', '.jpeg', '.tif', '.tga']
folder_path = "/Users/macbookpro/Documents/Image"
print (os.listdir(folder_path))
for root, dirs, files in os.walk(folder_path):
 for fileName in files:
      	if fileName.endswith(tuple(list)):
      		a= os.path.getctime(fileName)
with open('Img2Fichier.txt','w') as o:
          o.write(time.ctime(a))
with open ('Img2Fichier.txt', 'r') as f:
  	    	print(f.read())
  	    	print(a)