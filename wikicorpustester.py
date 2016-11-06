"""wiki load test"""
import logging
from gensim.models import Word2Vec

def main():
   print("Loading model")
   model = Word2Vec.load("local/en_1000_no_stem/en.model")
   print(model.similarity('woman', 'man'))

if __name__ == "__main__":
    main()
