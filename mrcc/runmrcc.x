#!/bin/sh

if [[ $# < 1 ]]
then
    echo "Usage: runmrcc input.gjf"
    exit
fi

export OMP_NUM_THREADS=48
export MKL_NUM_THREADS=48
export PATH=$PATH:/s/ls4/users/knvvv/bin/mrcc

MRCCDIR="/s/ls4/users/knvvv/bin/mrcc/"
SCRDIR=$MRCCDIR"Scratch/"
RANDOMDIR=$SCRDIR`basename $1`"_"`{ date +%s%N; echo $RANDOM; } | tr -d "\n"`

mkdir $RANDOMDIR
INPFILE=`pwd`/$1
OUTFILE=$INPFILE.out

cd $RANDOMDIR
cp $INPFILE MINP
dmrcc > $OUTFILE
cp COORD.xyz $INPFILE.xyz
cd $SCRDIR
#rm -R $RANDOMDIR
