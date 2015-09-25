import sys
import urllib
import json
import re

instances = {} 
count = 0

def getWords():
	global count
	tweet_file = open(sys.argv[1])
	for line in tweet_file:
		result = json.loads(line)
		string = result.get('text','').encode("ascii", "ignore")
		words = string.split()
		for word in words:
			instances[word]= int(instances.get(word,0))+1
			count= count+1
def printFrequencies():
	for key in instances.keys():
		print "%s %0.4f" % (key, instances[key]/count)
def main():
	getWords()
	printFrequencies()

if __name__ == '__main__':
	main()
