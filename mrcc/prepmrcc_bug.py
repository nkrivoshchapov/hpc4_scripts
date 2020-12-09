import os, sys, subprocess, time, random

def runc(runline):
    p = subprocess.Popen(runline, shell = True)
    while p.poll() == None:
        time.sleep(2)

rank = int(sys.argv[1])
starttime = time.time()

def runcalc(file):
    try:
        jfile = open(file,"r")
    except:
        return 0
    jlines = jfile.readlines()
    jfile.close()
    if os.path.getmtime(file)>starttime:
        return 0;
    runc("touch "+file)
    p = subprocess.Popen("./bin/mrcc/runmrcc.x " + file, shell = True)
    print("Started MRCC calc of " + file)
    while p.poll() == None:
        time.sleep(4)
    time.sleep(10)
    return 0

docalc = open("mdo_calc.dat","r").readlines()
print("Script started on rank " +str(rank)+"\n")
while len(docalc) > 0:
    print("We have "+str(rank)+" rank and "+str(len(docalc))+" files\n")
    if len(docalc) > rank:
        runcalc(docalc[rank].replace("\n",""))
    time.sleep(10)
    for line in docalc:
        if os.path.isfile(line.replace("gjf","log").replace("\n","")):
            docalc.remove(line)
sys.exit(0)
