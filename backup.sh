#!/bin/bash


fecha_actual=$(date +%Y-%m-%d)


fecha_ayer=$(date -d "yesterday" +%Y-%m-%d)


mkdir -p "/var/tmp/Backups/$fecha_actual"


rsync -av --link-dest="/var/tmp/Backups/$fecha_ayer" /home/urko/UPV3/ISSKS/LAB/LAB5/Segurtasuna/ "/var/tmp/Backups/$fecha_actual/"
