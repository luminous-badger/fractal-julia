#!/bin/bash

xmin=-1.0
xmax=1.0
ymin=-1.0
ymax=1.0
offset=0.1

(( loopcount=0 ))
for Re in $( seq $xmin $offset $xmax )
do
	for Im in $( seq $ymin $offset $ymax )
	do
		echo "Re Im: " $Re $Im
		# 
		./arg_jc_power.py $Re $Im
		(( loopcount++ ))
		echo
	done	
done	

echo $loopcount
