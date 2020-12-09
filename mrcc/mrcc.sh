#!/bin/sh
#SBATCH -J OObond
#SBATCH -D /s/ls4/users/knvvv
#SBATCH -o job.out
#SBATCH -e job.err
#SBATCH -t 3-00:00:00
#SBATCH -p hpc4-3d
#SBATCH --cpus-per-task=48
#SBATCH -N 1
#SBATCH --exclude=
#SBATCH --nodelist=
module load intel-compilers
. /s/ls4/sw/anaconda/2/5.1.0/etc/profile.d/conda.sh
export OMP_NUM_THREADS=48
export MKL_NUM_THREADS=48
export PATH=$PATH:/s/ls4/users/knvvv/bin/mrcc
$MPIRUN -n 1 `pwd`/progmrcc2.out
