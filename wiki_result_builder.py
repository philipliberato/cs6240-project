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
num_similarities = 5

def main():

	files = ['linux_docs', 'git_docs', 'sqlite_docs']
	corpusii = ['wiki']
	thresholds_list = [.1, .5, .6, .7, .8, .9, .95, .99]
	num_similarities_list = [1,5,10,25,50,100,250,500,1000]

	model = Word2Vec.load('local/en_1000_no_stem/en.model')

	for file in files:
		query_doc = open('./docs/' + file + '.txt','r')
		documents = []
		for line in query_doc:
			seg = line.split()
			callingFunc = seg.pop(0)
			documents.append(seg)
		for corpus in corpusii:
			for thresh in thresholds_list:
				for num in num_similarities_list:
					global threshold
					global min_occurences
					global num_similarities

					#parameters to adjust for results
					threshold = thresh
					num_similarities = num
					check_document(model, callingFunc, set(seg))
					#ignore any user-specified functions from avoid.txt
					avoid_doc = open('avoid.txt','r')
					for line in avoid_doc:
						seg = line.split()[0]
						if seg in no_match_dict.keys():
							no_match_dict.pop(seg, None)
					threshWhole = int(threshold * 100)
					sys.stdout = open('wiki_results/' + file + '_results_' + corpus + '_' + str(threshWhole)+'_'+ str(num_similarities)+'.txt', 'w')
					outString = "['gemini.py', '"+file+"', 'wiki', '"+str(threshWhole)+"', '" + str(num)+"']"
					print(outString)
					print(matches)
					print(no_matches)
					pprint(no_match_dict)
					print(len(no_match_dict))
					print(len(key_error_list))
					print(no_matches - len(no_match_dict))
					sys.stdout = open('global_results.txt','a')
					print(file+' '+corpus+' '+str(threshWhole)+' '+str(num_similarities)+' '+str(matches)+' '+str(no_matches)+' '+str(len(no_match_dict))+' '+str(len(key_error_list)))
					

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
