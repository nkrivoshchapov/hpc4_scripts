#!/bin/sh
#SBATCH -J nbo
#SBATCH -D /s/ls4/users/knvvv
#SBATCH -o test.out
#SBATCH -e test.err
#SBATCH -t 2-00:00:00
#SBATCH -p hpc4-3d
#SBATCH --cpus-per-task=48
#SBATCH -N 8
#SBATCH --exclude=
#SBATCH --nodelist=
hostname
df
date
sleep 10
date
module load intel-compilers
$MPIRUN -n 8 `pwd`/prog2.out
while true
do
echo "I'm alive"
sleep 60
done
