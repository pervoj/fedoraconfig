#!/bin/bash

# this is a runner script for the Fedora Config program

# config
script="https://gitlab.com/pervoj/fedoraconfig/-/archive/main/fedoraconfig-main.zip"
dir="/tmp/.fedoraconfigscripttmp"
file="$dir/script.zip"
extract="$dir/extract"

# create dirs
[[ -d $dir ]] && rm -R $dir
mkdir $dir $direx

# download and extract files
wget -qO $file $script
unzip -q $file -d $extract

# determine program path and run it
rundir="$extract/$(ls $extract)"
python $rundir

# clean
rm -R $dir
