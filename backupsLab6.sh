#!/bin/bash


fecha_actual=$(date +%Y-%m-%d)


fecha_ayer=$(date -d "yesterday" +%Y-%m-%d)


rsync -av --link-dest="/var/tmp/Backups/$fecha_ayer" /home/urko/UPV3/ISSKS/LAB/LAB5/Segurtasuna/ "urkoaragom@34.136.240.16:/var/tmp/Backups/$fecha_actual"
