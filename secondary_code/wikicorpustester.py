"""wiki load test"""
import logging
from gensim.models import Word2Vec


def main():
   print("Loading model")
   #model = Word2Vec.load("local/en_1000_no_stem/en.model")
   doc = open('documents.txt','r')
   sentences = []

   for line in doc:
    	seg = line.lower().split()
    	#pop the caller func bc it's unneeded
    	seg.pop(0)
    	sentences.append(seg)

   model = Word2Vec(sentences, min_count=50)

   print(model.similarity('malloc', 'realloc'))
   
   #model.train(sentences)
   #print(model.similarity('malloc', 'free'))
   #print(sentences)
   print(model.most_similar(positive=['malloc'],topn=15))


   #print(model.similarity('woman', 'man'))

if __name__ == "__main__":
    main()
