#!/bin/bash
date +"%Y/%m/%d %p %I:%M:%S"
FILE="foo.txt"
SUM=0
while read line;
do
   SUM=`expr $SUM + $line`
done < $FILE

echo "合計: ${SUM}"
date +"%Y/%m/%d %p %I:%M:%S"
