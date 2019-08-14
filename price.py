# Changes the price of an item
import sys

infile = open('const.js', 'r')

outfile = open('pricechange.js', 'w')

lines = infile.readlines()

skip = False



for line in lines:
    if skip == True:
        skip = False
        continue
    if str(sys.argv[1]) in line:
        outfile.write(line)
        outfile.write("    price: " + sys.argv[2] + ',\n')
        skip = True
        continue
    outfile.write(line)

infile.close()
outfile.close()


'''
for each line
    if skip is true
        set skip to false
        continue
    if the command line arg is found in the line
        add the line
        add the new price line
        set skip to true
        continue
    add the line to the file
'''