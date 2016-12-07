#!/bin/bash

# chmod +x create_dot_files.sh
# ./create_dot_files.sh .

files=$(ack-grep $1 -f --type=cc)
for file in $files; do
    clang-3.5 -S -emit-llvm $file -o - | opt -analyze -dot-callgraph
    echo callgraph.dot $file | python document_builder.py
done
