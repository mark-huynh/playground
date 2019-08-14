import sys

infile = open('const.js', 'r')
outfile = open('descChange.js', 'w')

lines = infile.readlines()

skip = False

counter = 0

for line in lines:
    if counter == 1:
        outfile.write("    description: \"" + sys.argv[2] + '\",\n')
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

'''
for each line
    if counter is 4
        write new description
        set counter to 0
        set skip to false
        continue
    if skip is true
        increment counter
    if the name is in the line
        set skip to true
    write line to file

'''

'''
for each line
    if skip4 is true
        increment counter
        if counter is 4
            set skip 4 and counter to 0
    if it has the name
        write the current line
        write the next two lines
        write a new fourth line that has the new description
        set skip4 to true
'''