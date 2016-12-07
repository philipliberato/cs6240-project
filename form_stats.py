#formulate functions statistics using documents.txt

def main():
    print("---loading txt file----")
    doc = open('documents.txt','r')
    print("---running stat analysis---")
    tracker = {}

    for line in doc:
    	seg = line.split()
    	#pop the caller func bc it's unneeded
    	seg.pop(0)
    	for func in seg:
	   		index = seg.index(func) + 1
	   		if func not in tracker:
	   			tracker[func] = {}
	   		while index < len(seg):
	   			if seg[index] not in tracker[func]:
	   				tracker[func][seg[index]] = 0
	   			tracker[func][seg[index]] = tracker[func][seg[index]] + 1
	   			index = index + 1
    
    doc.close()
    doc = open('results.txt', 'w')
    for key in tracker:
    	for key2 in tracker[key]:
    		doc.write(key + " " + key2 + " " + str(tracker[key][key2]))
    		doc.write("\n")
    print("---done---")

    #view results here
    #print(tracker['malloc']['free'])
  

    
if __name__ == "__main__":
	main()
