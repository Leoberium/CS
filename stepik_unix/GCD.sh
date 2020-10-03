#!/bin/bash
gcd ()
{
	if [[ $1 -eq $2 ]] ; then
		GCD=$1
	elif [[ $1 -gt $2 ]] ; then
		diff=$(($1 - $2))
		gcd $diff $2
	else
		diff=$(($2 - $1))
		gcd $1 $diff
	fi
}
while true ; do
	read m n
	if [[ -z $m || -z $n ]] ; then
		echo "bye"
		break
	else
		gcd $m $n
		echo "GCD is $GCD"
	fi
done
