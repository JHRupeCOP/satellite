#!/bin/bash

export REPORT_DIR="/home/ruppej/reports"

if [[ ! -e $REPORT_DIR ]]
then
    mkdir -p $REPORT_DIR
elif [[ ! -d $REPORT_DIR ]]
then
    echo "$REPORT_DIR already exists but is not a directory" 1>&2
    break
fi

hammer --no-headers --csv --output-file "${REPORT_DIR}/content_views.csv" content-view list --fields "content view id,name,composite"
