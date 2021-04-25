import os
r=[]
list=['.png','.jpg', '.jpeg', '.tif', '.tga']
folder_path = "/Users/macbookpro/Documents/Image"
#print (os.listdir(folder_path))
for root, dirs, files in os.walk(folder_path):
 for fileName in files:
      	if fileName.endswith(tuple(list)):
   	      r.append(str(fileName))
with open('ImgFichier.txt','w') as o:
        
          o.write(str(r))
with open ('ImgFichier.txt', 'r') as f:
  	    	print(f.read())
  	    	print(r)