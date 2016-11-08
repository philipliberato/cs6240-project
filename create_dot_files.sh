#!/bin/bash
files=$(ack-grep . -f --type=cc)
for file in $files; do
    echo $file
done
