import sys
import re
import json


scores = {} 
newscores = {} 
instances = {} 

def createwordDict():
    sent_file = open(sys.argv[1])
    for line in sent_file:
	term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character"
	scores[term] = int(score) # Convert the score to an integer.

def scoreTweets():
	tweet_count = 1
	tweet_file = open(sys.argv[2])
	for line in tweet_file:
		tweet_score = 0
		result = json.loads(line)
		string = result.get('text','zz').encode("ascii", "ignore")
		#words = re.compile('\w+').findall(string)
		words = string.strip().split()
		newwords= []
		for word in words:
			word = word.encode('utf-8')
			word_score = int(scores.get(word,'1000000'))
			# Means word was not found in original dictionary
			if word_score==1000000:
				newwords.append(word)
			else:
				tweet_score = tweet_score + word_score
			# Now check for all new words encountered
		for word in newwords:
			newscores[word]= newscores.get(word,0)+tweet_score
		tweet_count= tweet_count +1

def displayWords():
	for key, value in sorted(newscores.iteritems(), key=lambda (k,v): (v,k)):
		print "%s %s" % (key, value)

def lines(fp):
    print str(len(fp.readlines()))

def main():
   # sent_file = open(sys.argv[1])
   # tweet_file = open(sys.argv[2])
    createwordDict()
    scoreTweets()
    displayWords()

if __name__ == '__main__':
    main()
