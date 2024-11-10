#!/bin/sh


for D in [A-Z]*; do
    if test -d $D; then
	if test $D/$D.csv -nt $D/README.md; then
	    $HOME/bin/do_command.sh "python make_README.py $D"
	fi
    fi
done
	  

# end
