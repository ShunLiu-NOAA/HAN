#!/bin/bash -l

OBSTYPE='rw'

genyaml=true

if [ $genyaml = "true" ]; then
   echo "generating confg.yaml"
fi

cat > config.yaml <<EOF
paths:
   inputdir: ./data 
   outputdir: ./output
VarName: radial_velocity'
inputfile: ufo_${OBSTYPE}_output_2020101300_0000.nc4
OBSTYPE: rw
subtask: 5
EOF
   
python han.py
#python han.py $taskdir/$filename $OBSTYPE $VarName $subtask
