"""wiki load test"""
import logging
from gensim.models import Word2Vec
from pprint import pprint
import sys

matches = 0
no_matches = 0
no_match_dict = {}
key_error_list = []
threshold = 0
min_occurences = 1
num_similarities = 5

def main():

	args = []
	if len(sys.argv) != 6:
		exit()
	
	args.append(sys.argv[1])
	args.append(sys.argv[2])

	global threshold
	global min_occurences
	global num_similarities

	#parameters to adjust for results
	threshold = float(sys.argv[3])
	min_occurences = int(sys.argv[4])
	num_similarities = int(sys.argv[5])

	model_name = ''
	if args[1] == 'wiki':
		model_name = 'local/en_1000_no_stem/en.model'
		print('wiki')
	elif args[1] == 'code':
		model_name = 'local/code_corpus_'+str(min_occurences)+'.model'
		print('code')
	elif args[1] == 'both':
		model_name = ' '
		print('both')
	else:
		print("Error, arg2 invalid")
		exit()

	model = Word2Vec.load(model_name)
	#model_doc is corpus of C/C++ projects' functions
	#query_doc is current project to analyze
	model_doc = open('./docs/documents.txt', 'r')
	query_doc = open(args[0] + '.txt','r')
   
	documents = []
	for line in model_doc:
		seg = line.split()
		seg.pop(0)
		documents.append(seg)


	#model.build_vocab(documents)
	#model.train(documents, total_examples=len(documents))
	#train the model on all stashed project data
	#model = Word2Vec(documents, min_count=min_occurences)

	#analyze the current subject's functions calls
	documents = []
	for line in query_doc:
		seg = line.split()
		callingFunc = seg.pop(0)
		check_document(model, callingFunc, set(seg))

	#ignore any user-specified functions from avoid.txt
	avoid_doc = open('avoid.txt','r')
	for line in avoid_doc:
		seg = line.split()[0]
		if seg in no_match_dict.keys():
			no_match_dict.pop(seg, None)

	#model.save('local/'+args[1]+'_corpus_'+str(min_occurences)+'.model')
	thresh = int(threshold * 100)
	sys.stdout = open(args[0] + '_results_' + args[1] + '_' + str(thresh)+'_'+str(min_occurences) + '_' + str(num_similarities)+'.txt', 'w')
	print(sys.argv)
	print(matches)
	print(no_matches)
	pprint(no_match_dict)
	print(len(no_match_dict))
	print(len(key_error_list))
	print(no_matches - len(no_match_dict))

#collect data about missing functions with close distance to
#other present functions
def check_document(model, callingFunc, document):
	global threshold
	global num_similarities
	global matches
	global no_matches
	global no_match_dict
	global key_error_list

	#for a single document (caller function and its callees)
	for token in document:
		try:
			#get the top N function candidates and their distances
			candidates = model.most_similar(positive=[token],topn=num_similarities)
			#filter out distance values, show just closely-related functions
			candidate_strings = [str(c[0]) if c[1] > threshold else "" for c in candidates]
			intersect = set(document).intersection(candidate_strings)
			#if related functions not in callee functions, add to no_match dictionary
			if len(intersect) == 0:
				if "external_node" not in callingFunc:
					if token not in no_match_dict.keys():
						no_match_dict[token] = [callingFunc]
						no_matches += 1
					else:
						no_match_dict[token].append(callingFunc)
			else:
				matches += 1
		#catch error when the searched key is not in the model and track
		except KeyError as e:
			if token not in key_error_list:
				key_error_list.append(token) 
			
if __name__ == "__main__":
    main()
