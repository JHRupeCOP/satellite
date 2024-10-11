#!/bin/bash

export REPORT_DIR="/home/ruppej/reports"

if [[ ! -e $REPORT_DIR ]]
then
    mkdir -p $REPORT_DIR
elif [[ ! -d $REPORT_DIR ]]
then
    echo "$REPORT_DIR already exists but is not a directory" 1>&2
fi

for host_group in $(/bin/hammer --no-headers hostgroup list --fields name)
do
  /bin/hammer --no-headers --csv --output-file "${REPORT_DIR}/host_by_hostgroup_${host_group}.csv" \
     host list --search "hostgroup = $host_group --fields name"
done

