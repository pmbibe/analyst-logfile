NUM_OF_LINES=400000
filename = 'log3.txt'
with open(filename) as fin:
    fout = open('output/result0.txt','w')
    for i,line in enumerate(fin):
      a = str(line)
      fout.write(a)
      if (i+1)%NUM_OF_LINES == 0:
        fout.close()
        print ("--")
        fout = open("output/result%d.txt"%(i/NUM_OF_LINES+1),"w")

    fout.close()
