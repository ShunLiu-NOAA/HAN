subtask=5
OBSTYPE='rw'
VarName='radial_velocity'
taskdir=./data
filename="ufo_${OBSTYPE}_output_2020101300_0000.nc4"
python han.py $taskdir/$filename $OBSTYPE $VarName $subtask
