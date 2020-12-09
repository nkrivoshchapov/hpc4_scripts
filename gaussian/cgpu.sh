#!/bin/sh
#SBATCH -J eqax
#SBATCH -D /s/ls4/users/knvvv
#SBATCH -o test.out
#SBATCH -e test.err
#SBATCH -t 3-00:00:00
#SBATCH -p hpc5-gpu-3d
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=16
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
