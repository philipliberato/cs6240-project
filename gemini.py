"""wiki load test"""
import logging
from gensim.models import Word2Vec


def main():

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
		seg.pop(0)
		documents.append(seg)

	matches = 0
	no_matches = 0
	no_match_list = []

	for document in documents:
		for token in document:
			try:
				candidates = model.most_similar(positive=[token],topn=num_similarities)
				candidate_strings = [str(c[0]) if c[1] > threshold else "" for c in candidates]
				intersect = set(document).intersection(candidate_strings)
				if len(intersect) == 0:
					#print("No match:" + str(token) + str(candidate_strings))
					if token not in no_match_list:
						no_match_list.append(token)
						no_matches += 1
				else:
					#print("Match:" + str(intersect))
					matches += 1
			except KeyError as e:
				pass #print("Exception:" + token)
			
	print(matches)
	print(no_matches)
	print(no_match_list)





   #model.train(sentences)
   #print(model.similarity('malloc', 'free'))
   #print(sentences)


   #print(model.similarity('woman', 'man'))

if __name__ == "__main__":
    main()
