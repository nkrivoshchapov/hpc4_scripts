import os, sys, subprocess, time, random
rank = int(sys.argv[1])

def runcalc(file):
    try:
        jfile = open(file,"r")
    except:
        return 0;
    jlines = jfile.readlines()
    jfile.close()
    
    p = subprocess.Popen("./bin/mrcc/runmrcc.x " + file, shell = True)
    print("Started MRCC calc of " + file)
    while p.poll() == None:
        time.sleep(4)
    time.sleep(10)
    return 0;

docalc = open("mdo_calc.dat","r").readlines()
print("Script started on rank " +str(rank)+"\n")
print("We have "+str(rank)+" rank and "+str(len(docalc))+" files\n")
runcalc(docalc[rank % len(docalc)].replace("\n",""))

sys.exit(0)
