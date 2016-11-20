#!/bin/bash
files=$(ack-grep . -f --type=cc)
for file in $files; do
    clang-3.5 -S -emit-llvm $file -o - | opt -analyze -dot-callgraph
    echo callgraph.dot | python document_builder.py
done
