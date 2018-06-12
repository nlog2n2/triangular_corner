#!/bin/bash
date +"%Y/%m/%d %p %I:%M:%S"
FILE="foo.txt"

awk '{s += $1} END {print "合計: " s}' < $FILE

date +"%Y/%m/%d %p %I:%M:%S"
