import sys
import urllib
import json
import re

instances = {} 

def getHashTags():
	tweet_file = open(sys.argv[1])
	for line in tweet_file:
		result = json.loads(line)
		e = result.get('entities', None)
		if e!=None:
			h = e.get('hashtags',None)
			if h!=None:
				for i in range(0, len(h)):
					term = h[i].get('text').encode('ascii','ignore')
					instances[term] = int(instances.get(term,0))-1

def printFrequencies():
	count = 0
	for key, value in sorted(instances.iteritems(), key=lambda (k,v): (v,k)):
		if key!='' and count<10:
			print "%s %f" % (key, -instances[key])
			count = count+1

def main():
	getHashTags()
	printFrequencies()

if __name__ == '__main__':
	main()
