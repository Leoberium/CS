#!/bin/bash
while : ; do
	read a operation b
	if [[ $a == "exit" ]] ; then
		echo "bye"
		break
	elif [[ $a != "exit" && $# -eq 1 ]] ; then
		echo "error"
		break
	else
		case "$operation" in
			"+" ) echo "$(($a+$b))" ;;
			"-" ) echo "$(($a-$b))" ;;
			"*" ) echo "$(($a*$b))" ;;
			"/" ) echo "$(($a/$b))" ;;
			"%" ) echo "$(($a%$b))" ;;
			"**" ) echo "$(($a**$b))" ;;
			* ) echo "error" ; break
		esac
	fi
done
