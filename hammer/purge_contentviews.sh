#!/bin/bash

# Constants
org_id="1"
org_name="ConocoPhillips"
log_dir="/var/log/satellite"
log_file="${logDir}/purge_cv.log_${dateStamp}"
tmp_dir="/tmp/satellite"
composite_out="${tmp_dir}/composite.dat"
regular_out="${tmp_dir}/regular_cv.dat"
purge_count=2

function validate_dirs() {
# create directories if missing
    if [ ! -d "${1}" ]
    then 
       mkdir -p "${1}"
    fi
}

function list_content_view(){
# creates a file with content view id and name
    hammer --no-headers \
      --csv \
      --output-file ${1} \
      content-view list --organization-id ${org_id} --composite ${2} --fields "content view id,name"
}

function purge_cvs(){
# remove unused content views 
    while read i
    do 
       cv_id=$(echo $i | cut -d, -f1)
       if [ $cv_id -gt 1 ]
       then
          hammer content-view purge --count ${purge_count} --id $cv_id
       fi
    done < $1
}

# Script start

# validate directories
for i in ${log_dir} ${tmp_dir}
do 
  validate_dirs $i
done

# create content view lists
list_content_view ${composite_out} true 
list_content_view ${regular_out} false 

# purge content views 
purge_cvs ${composite_out}
sleep 10
purge_cvs ${regular_out}
