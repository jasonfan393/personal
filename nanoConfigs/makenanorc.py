rclist = ['pref','cpp','python','vhdl']
outputfile = open('../../.nanorc', 'w')
for i in rclist:
  readfile = open(i+'.nanorc','r')
  for line in readfile:
    outputfile.write(line)
  readfile.close()
outputfile.close()
