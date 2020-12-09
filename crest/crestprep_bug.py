import os, sys, subprocess, time, random, ntpath
from shutil import copy2
rank = int(sys.argv[1])
wsize = int(sys.argv[2])
proc=8
extraargs="-gfn2"
starttime = time.time()
def runcalc(file):
    try:
        os.mkdir(file.replace(".xyz",""))
        copy2(file,file.replace(".xyz",""))
    except:
        return 0;
    p = subprocess.Popen("./bin/runcrest.x %s %s %d %s" % (file.replace(".xyz",""), ntpath.basename(file), proc, extraargs), shell = True)
    print("Started CREST calc of " + file)
    while p.poll() == None:
        time.sleep(4)
    return 0;

docalc = open("do_crest.dat","r").readlines()
print("Script started on rank " +str(rank)+"\n")
while len(docalc) > 0:
    print("We have "+str(rank)+" rank and "+str(len(docalc))+" files\n")
    print("My docalc = "+repr(docalc))
    if len(docalc) > rank:
        runcalc(docalc[rank].replace("\n",""))
    time.sleep(10)
    for line in docalc:
        if os.path.isdir(line.replace(".xyz","").replace("\n","")):
            docalc.remove(line)


sys.exit(0)
