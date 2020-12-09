#!/bin/sh
DIRECT=`pwd`
INPUTF=$1
INPEXT=${INPUTF##*.}
INPUTF=${INPUTF%.$INPEXT}

sleep 1s
#########################
export GAUSS_SCRDIR=$DIRECT/bin/scratch
export GAUSS_EXEDIR=$DIRECT/bin/g16sse
export GAUSS_ARCHDIR="/g16/arch"
export GMAIN=$GAUSS_EXEDIR
export LD_LIBRARY_PATH=$GAUSS_EXEDIR
export G09BASIS="$DIRECT/bin/g16sse"
export F_ERROPT1="271,271,2,1,2,2,2,2"
export TRAP_FPE="OVERFL=ABORT;DIVZERO=ABORT;INT_OVERFL=ABORT"
export MP_STACK_OVERFLOW="OFF"
export KMP_DUPLICATE_LIB_OK="TRUE"
export PATH=${PATH}:${GAUSS_EXEDIR}
$GAUSS_EXEDIR/g16 $INPUTF."$INPEXT"
#########################
