#!/bin/sh
xtbin='/s/ls4/users/knvvv/bin/xtb-6.3.2/bin/xtb'
crst='/s/ls4/users/knvvv/bin/xtb-6.3.2/bin/crest'

command -v $xtbin >/dev/null 2>&1 || { echo >&2 "Cannot find xtb binary. Exit."; exit 1; }
command -v $crst >/dev/null 2>&1 || { echo >&2 "Cannot find crest binary. Exit."; exit 1; }
cd $1
if [ $xtbin == 'xtb' ]
 then
    $crst $2 $4 -T $3 -ewin 5.0 > LOGFILE
 else
    $crst $2 $4 -T $3 -ewin 5.0  -xnam $xtbin > LOGFILE
 fi

