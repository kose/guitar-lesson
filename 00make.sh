#!/bin/sh


for D in [A-Z]*; do
    if test -d $D; then
	$HOME/bin/do_command.sh "python make_README.py $D"
    fi
done
	  

# end
