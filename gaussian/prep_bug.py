import os, sys, subprocess, time, random
rank = int(sys.argv[1])
wsize = int(sys.argv[2])
proc=16
starttime = time.time()
def runcalc(file):
    try:
        jfile = open(file,"r")
    except:
        return 0;
    if os.path.getmtime(file)>starttime:
        return 0;
    jlines = jfile.readlines()
    jfile.close()
    for line in reversed(jlines):
        if line.startswith("%nprocshared") or line.startswith("%RWF") or line.startswith("%rwf"):
            jlines.remove(line)
    jlines.insert(0,"%nprocshared="+str(proc)+"\n")
    tempfile = "temp"+str(rank)+"_"+str(random.randint(1,100000))
    jlines.insert(0, "%RWF="+tempfile+",30GB\n")
    jfile = open(file,"w")
    jfile.write("".join(jlines))
    jfile.close()
    p = subprocess.Popen("./bin/Mg16.x " + file, shell = True)
    print("Started Gaussian calc of " + file)
    while p.poll() == None:
        time.sleep(4)
    try:
        os.remove(tempfile+".rwf")
    except:
        pass
    return 0;

docalc = open("do_calc.dat","r").readlines()
print("Script started on rank " +str(rank)+"\n")
while len(docalc) > 0:
    print("We have "+str(rank)+" rank and "+str(len(docalc))+" files\n")
    if len(docalc) > rank:
        runcalc(docalc[rank].replace("\n",""))
    time.sleep(10)
    for line in docalc:
        if os.path.isfile(line.replace("gjf","log").replace("\n","")) or os.path.isfile(line.replace("gjf","2ordernbo").replace("\n","")):
            docalc.remove(line)


sys.exit(0)
