import os
pipi = open('moi.txt', 'w')
os.rename('moi.txt','remoi.txt')
open ('remoi.txt', 'w')
os.replace('remoi.txt','remoimoi.txt')
fi = open ('remoimoi.txt', 'r')
print(fi.name)