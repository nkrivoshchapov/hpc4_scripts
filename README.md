Compile C++:
```
module load intel-compilers
mpicxx prog2.cpp -o prog2.out
```

! Set the right path to Gaussian, Xtb+Crest or MRCC in \*.x file.

Run Gaussian calculations on several nodes:
1. Create do_calc.dat file containing relative paths to gjf files:
```
data/nbo/fileA.gjf  # complete path is ~/data/nbo/fileA.gjf
data/nbo/fileB.gjf
data/nbo/fileC.gjf
```
do_calc.dat should be in ~/ along with calc.sh, prog2.out and python-script.

2. Set the number of nodes and MPI-threads in .sh-file:
```
#SBATCH -N 8    # 8 nodes
...
$MPIRUN -n 8 `pwd`/prog2.out   # 1 calculation (python-script) per node
```

3. Set the number of threads for Gaussian calculations in python-script:
```
...
proc=16
...
```

4. Submit the job to Slurm:
```
sbatch calc.sh
```

