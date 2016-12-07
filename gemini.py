"""wiki load test"""
import logging
from gensim.models import Word2Vec
from pprint import pprint

matches = 0
no_matches = 0
no_match_dict = {}
threshold = 0
min_occurences = 1
num_similarities = 5

def main():
	global threshold
	global min_occurences
	global num_similarities

	threshold = 0.5
	min_occurences = 1
	num_similarities = 1000

   #model = Word2Vec.load("local/en_1000_no_stem/en.model")
	model_doc = open('documents.txt', 'r')
	query_doc = open('linux_docs.txt','r')
   
	documents = []
	for line in model_doc:
		seg = line.lower().split()
		seg.pop(0)
		documents.append(seg)

	model = Word2Vec(documents, min_count=min_occurences)

	documents = []
	for line in query_doc:
		seg = line.lower().split()
		callingFunc = seg.pop(0)
		check_document(model, callingFunc, seg)
		#documents.append(seg)

	print(matches)
	print(no_matches)
	pprint(no_match_dict)

def check_document(model, callingFunc, document):
	global threshold
	global num_similarities
	global matches
	global no_matches
	global no_match_dict

	for token in document:
		try:
			candidates = model.most_similar(positive=[token],topn=num_similarities)
			candidate_strings = [str(c[0]) if c[1] > threshold else "" for c in candidates]
			intersect = set(document).intersection(candidate_strings)
			if len(intersect) == 0:
				#print("No match:" + str(token) + str(candidate_strings))
				if token not in no_match_dict.keys():
					no_match_dict[token] = [callingFunc]
					no_matches += 1
				else:
					no_match_dict[token].append(callingFunc)
			else:
				#print("Match:" + str(intersect))
				matches += 1
		except KeyError as e:
			pass #print("Exception:" + token)
			






   #model.train(sentences)
   #print(model.similarity('malloc', 'free'))
   #print(sentences)


   #print(model.similarity('woman', 'man'))

if __name__ == "__main__":
    main()
