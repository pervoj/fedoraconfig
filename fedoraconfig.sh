#!/bin/bash

# this is a runner script for the Fedora Config program

# config
script="https://github.com/pervoj/fedoraconfig/archive/main.zip"
dir="/tmp/.fedoraconfigscripttmp"
file="$dir/script.zip"
extract="$dir/extract"

# create dirs
[[ -d $dir ]] && rm -R $dir
mkdir $dir $direx

wget -qO $file $script
unzip -q $file -d $extract

rundir="$extract/$(ls $extract)"
python $rundir

# clean
rm -R $dir
