#!/bin/bash
a=10
n=0
while [ $a -lt 20 ]
do	
	n=$[$n+1]
	if [ $n -eq 1000 ] 
	then 
		break
	fi
	INPUT=input$a.txt
	JAVAANS=java$a.txt
	JAVAOUT=javaout$a.txt
	STDOUT=stout$a.txt
	python generate.py > $INPUT
	cat $INPUT | java MainClass > $JAVAANS	
	cat $JAVAANS | python3 checkFormat.py
	if [ $? -eq 1 ]
	then 
		echo formatFail in $a
		a=$[$a+1]
		continue	
	fi
	cat $JAVAANS | python3 checkJava.py > javaout.txt
	cat $INPUT | python3 stans.py > stout.txt
	python3 comp.py

	if [ $? -eq 1 ]
	then
		echo fail in $a
		cp javaout.txt $JAVAOUT
		cp stout.txt $STDOUT
		a=$[$a+1]
	else 
		echo pass
	fi
done	 
