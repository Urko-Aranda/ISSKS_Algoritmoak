#!/bin/bash

# Obtén la fecha actual en el formato deseado (por ejemplo, uuuu-hh-ee).
fecha_actual=$(date +%Y-%m-%d)

# Obtén la fecha de ayer en formato "uuuu-hh-ee"
fecha_ayer=$(date -d "yesterday" +%Y-%m-%d)

# Obtener los ficheros de la fecha de ayer del servidor externo al local
sync -av "urkoaragom@34.136.240.16:/var/tmp/Backups/$fecha_ayer" "/var/tmp/Backups/$fecha_ayer"

# Realiza la copia de seguridad incremental al directorio del servidor externo
rsync -av --link-dest="/var/tmp/Backups/$fecha_ayer" /home/urko/UPV3/ISSKS/LAB/LAB5/Segurtasuna/ "urkoaragom@34.136.240.16:/var/tmp/Backups/$fecha_actual"
