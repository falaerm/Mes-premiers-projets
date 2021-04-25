import os

folder_path = "/Users/macbookpro/Documents/Python/fifi"
print (os.listdir(folder_path))
for root, dirs, files in os.walk(folder_path):
    #f = open('titi.txt','w')
	for filename in files:
		os.rename(filename, filename.replace("i", "ii"))
		print(filename)
	  