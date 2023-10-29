#!/bin/bash

# Obtén la fecha actual en el formato deseado (por ejemplo, uuuu-hh-ee).
fecha_actual=$(date +%Y-%m-%d)

# Obtén la fecha de ayer en formato "uuuu-hh-ee"
fecha_ayer=$(date -d "yesterday" +%Y-%m-%d)

# Crea la carpeta con la fecha actual en /var/tmp/Backups/
mkdir -p "/var/tmp/Backups/$fecha_actual"

# Realiza la copia de seguridad incremental al directorio creado
rsync -av --link-dest="/var/tmp/Backups/$fecha_ayer" /home/urko/UPV3/ISSKS/LAB/LAB5/Segurtasuna/ "/var/tmp/Backups/$fecha_actual/"
