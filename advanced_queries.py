"""wiki load test"""
import logging
from gensim.models import Word2Vec
from pprint import pprint
import sys

def main():

	query_funcs = [	['fopen', 'close', 'open'],
					['fclose', 'open', 'close'],
					['fread', 'write', 'read'],
					['fwrite', 'read', 'write'],
					['malloc', 'free', 'calloc'],
					['close', 'calloc', 'free'],
					['pthread_create', 'pthread_mutex_unlock', 'pthread_mutex_lock'],
					['pthread_join', 'pthread_mutex_lock', 'pthread_mutex_unlock'],
					['sleep', 'pthread_cond_signal', 'pthread_cond_wait'],
					['pthread_mutex_lock', 'pthread_cancel', 'pthread_create'],
					['calloc', 'memcpy', 'malloc'],
					['fwrite', 'fgets', 'fputs'],
					['fclose', 'fputs', 'fgets'],
					['puts', 'fgets', 'fputs'],
					['stat', 'fputs', 'fgets'],
					['printf', 'sscanf', 'sprintf'],
					['send', 'wait', 'signal'] ] 

	min_occurences = [1,5,10,25,50,100,250,500,1000]
	
	print(str(sys.argv) + '\n')
	for min_occ in min_occurences:
		model_name = 'local/code_corpus_'+str(min_occ)+'.model'
		model = Word2Vec.load(model_name)
		print("Loading model with min_occ " + str(min_occ))
		for query in query_funcs:
			print('\t' + str(query))
			try:	
				pprint(model.most_similar(positive=[query[0], query[1]], negative=[query[2]], topn=10))
			except KeyError as e:
				print('\t' + str(e))
			print('\n')
	
if __name__ == "__main__":
    main()
