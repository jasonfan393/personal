import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--i','--inputs', nargs = '+')
parser.add_argument('filename', nargs = '+')    

args = parser.parse_args()
for i in args.filename:
    f = open(i,'r')
    out = ''
    for line in f:
      if len(line) == 2:
        out = out+('0'+line)
      else:
        out = out+(line)
    f.close()
    g = open(i,'w')
    g.write(out)
    


exit()
