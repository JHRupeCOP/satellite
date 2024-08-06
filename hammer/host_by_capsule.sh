#!/bin/bash

export REPORT_DIR="/home/ruppej/reports"
  
for CAPSULE in $(/bin/hammer --no-headers  proxy list | cut -d"|" -f2)
do
  export CAPSULE_SHORT=$(echo $CAPSULE | cut -d. -f1)

  /bin/hammer --csv --output-file "${REPORT_DIR}/hostBycapsule_${CAPSULE_SHORT}.csv" \
   host list --search="registered_through = ${CAPSULE}"
done
