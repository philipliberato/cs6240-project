# cs6240-project
CS 6240: Software Engineering Semester Project

Pre-requisites:
  You must first install Clang/LLVM and Graphviz (all needed to generate the documents)
  
Run the create_dot_files.sh script, which seeks out all .c and .cpp files, gets their call graphs,
  and pipes this output into the document_builder.py script
  
After this, you will have a documents.txt file containing all of the function call grouping in the format:
  ::caller_function:: callee1 callee2 callee3
  ::caller_function2:: foo bar 

Now it is time to use the gemini.py script to analyze the documents.txt file
Gemini.py takes in a few cmd line arguments.  They are:
  1) 'filename' where filename is the name of the file containing the documents for your program (do not include '.txt')
      --additionally, Gemini expects this to file to be located in the docs folder
  2) 'wiki'/'code'/'both' which is meant to analyze what model to load (only code model is functional at the moment)
  3) threshold (from 0 to 1)
  4) number of min occurences desired (note this helps Gemini know which model to load.  e.g. model "code_corpus_25.model" is        the model trained using 25 as its min occurences level
  5) number of similarities (used for querying model)

- [Project Proposal](https://docs.google.com/document/d/1ggJiaL3gdO8rZxeZbgVWhGYrrS6GGHh7yDA4107d3Ro/edit)
- [Project Progress](https://docs.google.com/document/d/1kT5qNgq6uY77Gc5A8uavghyJn15jyCUctbhLtkaiXQw/edit)
- [C/C++ Projects zip](https://drive.google.com/open?id=0B12cEF8wVKRXX0Vsci1WeUpPUWc)
