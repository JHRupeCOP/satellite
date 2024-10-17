#!/bin/bash

export REPORT_DIR="/home/ruppej/reports"

# Check if output directory is there 
if [[ ! -e $REPORT_DIR ]]
then
    mkdir -p $REPORT_DIR
elif [[ ! -d $REPORT_DIR ]]
then
    echo "$REPORT_DIR already exists but is not a directory" 1>&2
    break
fi

# Remove any existing reports
if ls ${REPORT_DIR}/host_by_hostgroup_*.csv  1> /dev/null 2>&1; then
    echo "Deleting old report files"
    rm -f ${REPORT_DIR}/host_by_hostgroup_*.csv
fi

for host_group in $(/bin/hammer --no-headers hostgroup list --fields name)
do
  echo -e "Generating report for host group: ${host_group}"
  /bin/hammer --no-headers --csv --output-file "${REPORT_DIR}/host_by_hostgroup_${host_group}.csv" \
     host list --search "hostgroup = $host_group" --fields "name"
done

