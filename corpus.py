import sys, os, re
from os import walk
#iterate over and map lines in text file with wav file path in directory

path = "/path/to/dir/"
dirs = os.listdir(path)
file_list = []
line_list = []

for file in dirs:
    file_list.append(file)

with open("/path/to/file/", "r") as f:
    for line in f:
        cleanedLine = line.rstrip('\n')
        cleanedLine = re.sub(r'^.*:', "", cleanedLine)
        cleanedLine = re.sub(r'^\s*', "", cleanedLine)
        line_list.append(cleanedLine)

with open("new.txt", "w+") as newtxt:
    newtxt.write("Phrase\tWav File Name\tGender\n")
    for line_list_value, file_list_value in zip(line_list, file_list):
        output = (line_list_value +'\t' + file_list_value + '\t')
        newtxt.write(output)
        file_list_value = re.sub(r'^.{17}', "", file_list_value)
        file_list_value = re.sub(r'\..*', "", file_list_value)
        output2 = (file_list_value + "\n")
        newtxt.write(output2)

print("Done. Try opening 'new.txt' in " + os.getcwd() + ".\n")
