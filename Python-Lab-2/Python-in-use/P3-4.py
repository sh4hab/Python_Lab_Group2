import os.path
from os import path


print ("Is it Directory? \n" + str(path.isdir('input_files')))
if path.isdir('input_files'):
	print("Yes. There is.")
else:
	os.mkdir('input_files')
print ("Is it Directory? \n" + str(path.isdir('input_files')))
os.chdir('input_files')
f=open("new-file.txt","w+")
f.write("Amirhossein Fattahi")
