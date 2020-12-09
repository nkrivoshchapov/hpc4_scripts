#!/bin/sh
#SBATCH -J crest
#SBATCH -D /s/ls4/users/knvvv
#SBATCH -o crest.out
#SBATCH -e crest.err
#SBATCH -t 3-00:00:00
#SBATCH -p hpc4-3d
#SBATCH --cpus-per-task=48
#SBATCH -N 15
#SBATCH --exclude=
#SBATCH --nodelist=
hostname
df
date
sleep 10
date
module load intel-compilers
$MPIRUN -n 90 `pwd`/progcrest2_bug.out
while true
do
echo "I'm alive"
sleep 60
done
