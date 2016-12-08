import os

def main():
	files = ['git_docs', 'sqlite_docs']
	corpusii = ['code']
	thresholds = [.1, .5, .6, .7, .8, .9, .95, .99]
	min_occurences = [1,5,10,25,50,100,250,500,1000]
	num_similarities = [1,5,10,25,50,100,250,500,1000]


	for file in files:
		for corpus in corpusii:
			for thresh in thresholds:
				thresh = str(thresh)
				for occurence in min_occurences:
					occurence = str(occurence)
					for sims in num_similarities:
						sims = str(sims)
						command = 'python gemini.py '+file+' '+corpus+' '+thresh+' '+occurence+' '+sims
						os.system(command)

if __name__ == "__main__":
    main()