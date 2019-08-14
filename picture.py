import sys

infile = open('const.js', 'r')
outfile = open('pictureChange.js', 'w')

outfile.write("import " + sys.argv[2] + " from './pictures/food/" + sys.argv[2] + ".jpg'")

lines = infile.readlines()

skip = False

counter = 0

for line in lines:
    if counter == 2:
        outfile.write("    picture: " + sys.argv[2] + ',\n')
        counter = 0
        skip = False
        continue
    if skip == True:
        counter += 1
    if str(sys.argv[1]) in line:
        skip = True
    outfile.write(line)

infile.close()
outfile.close()


# user on UI will choose name from dropdown and then type name of image
'''
open infile and outfile
append import at the beginning of the file with name as second argv
find name equal to first argument from dropdown
Use technique similar to description to replace picture with the variable with name of second argv

'''