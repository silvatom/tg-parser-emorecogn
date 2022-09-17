#!/bin/bash

# Script to compare the quantity of lines in the validation file and in the output file

COMMON="/home/anjose-d/tg/tg-parser-emorecogn"
OUTPUT="output"
VALIDATION="validation"
EQUIVALENT="$COMMON/$VALIDATION"

for filename in /home/anjose-d/tg/tg-parser-emorecogn/$OUTPUT/*; do
	if [ "$(wc -l < $filename)" -eq "$(wc -l < $EQUIVALENT/$(basename $filename).txt)" ];
		then
			echo 'Match!';
		else
			echo "Warning: No Match in file $(basename $filename.txt)!";
	fi
done
