#!/bin/bash

# Script to count all the lines of the splitted files

OUTPUT="output"
COUNT=0

for filename in /home/anjose-d/tg/tg-parser-emorecogn/$OUTPUT/*; do
	number=$(wc -l < $filename)
	COUNT=$((COUNT+number))
done
COUNT=$((COUNT-71+1))
printf "Total lines: %ld\n" $COUNT
