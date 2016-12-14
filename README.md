# cs6240-project
CS 6240: Software Engineering Semester Project

Pre-requisites:
  You must first apt-get install Clang/LLVM and Graphviz (all needed to generate the documents)
  Additionally gensim must be installed via pip ("pip install gensim")
  
Run the create_dot_files.sh script, which seeks out all .c and .cpp files, gets their call graphs,
  and pipes this output into the document_builder.py script
  
After this, you will have a documents.txt file containing all of the function call grouping in the format:
  ::caller_function:: callee1 callee2 callee3
  ::caller_function2:: foo bar 

Now it is time to use the gemini.py script to analyze the documents.txt file
Gemini.py takes in a few cmd line arguments.  They are:
 - 'filename' where filename is the name of the file containing the documents for your program (do not include '.txt')
      --additionally, Gemini expects this to file to be located in the docs folder
 - 'wiki'/'code'/'both' which is meant to analyze what model to load (only code model is functional at the moment)
 - threshold (from 0 to 1)
 - number of min occurrences desired (note this helps Gemini know which model to load.  e.g. model "code_corpus_25.model" is        the model trained using 25 as its min occurrences level
 - number of similarities (used for querying model)
 
Once run, Gemini will print out a lot of information, such as cmd line inputs, number of matches, number of non-matches, the dictionary of no-match functions, the size of that dictionary, and the size of the "no key" dictionary (function names not in the model).  This can all be saved to a file if desired.  Note, this is what we have done for Git/Linux/SQLite at several different parameter settings.  These can all be found in the results folder, and the labeling convention is as follows:

- e.g. "git_docs_results_code_10_1000_5.txt" is the output from the git_docs.txt documents file using the code model, with a threshold of .1 (which is multiplied by 100 for clarity in filename), number of min occurrences of 1000, and number of similarities of 5.

- [Project Proposal](https://docs.google.com/document/d/1ggJiaL3gdO8rZxeZbgVWhGYrrS6GGHh7yDA4107d3Ro/edit)
- [Project Progress](https://docs.google.com/document/d/1kT5qNgq6uY77Gc5A8uavghyJn15jyCUctbhLtkaiXQw/edit)
- [C/C++ Projects zip](https://drive.google.com/open?id=0B12cEF8wVKRXX0Vsci1WeUpPUWc)
