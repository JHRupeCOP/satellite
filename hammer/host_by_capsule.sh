#!/bin/bash

export REPORT_DIR="/home/ruppej/reports"
  
for CAPSULE in $(/bin/hammer --no-headers  proxy list --fields name)
do
  export CAPSULE_SHORT=$(echo $CAPSULE | cut -d. -f1)

  /bin/hammer --no-headers --csv --output-file "${REPORT_DIR}/hostBycapsule_${CAPSULE_SHORT}.csv" \
   host list --fields "name,operating system,host group,ip,lifecycle environment" --search="registered_through = ${CAPSULE}"
done
