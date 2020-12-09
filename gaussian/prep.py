import os, sys, subprocess, time, random
rank = int(sys.argv[1])
proc=32

def runcalc(file):
    try:
        jfile = open(file,"r")
    except:
        return 0;
    jlines = jfile.readlines()
    jfile.close()
    for line in reversed(jlines):
        if line.startswith("%nprocshared") or line.startswith("%RWF") or line.startswith("%rwf"):
            jlines.remove(line)
    jlines.insert(0,"%nprocshared="+str(proc)+"\n")
    tempfile = "temp"+str(rank)+"_"+str(random.randint(1,100000))
    jlines.insert(0, "%RWF="+tempfile+",80GB\n")
    jfile = open(file,"w")
    jfile.write("".join(jlines))
    jfile.close()
    p = subprocess.Popen("./bin/Mg16.x " + file, shell = True)
    print("Started Gaussian calc of " + file)
    while p.poll() == None:
        time.sleep(4)
    #time.sleep(10)
    try:
        os.remove(tempfile+".rwf")
    except:
        pass
    return 0;

docalc = open("do_calc.dat","r").readlines()
print("Script started on rank " +str(rank)+"\n")
print("We have "+str(rank)+" rank and "+str(len(docalc))+" files\n")
runcalc(docalc[rank % len(docalc)].replace("\n",""))


sys.exit(0)
