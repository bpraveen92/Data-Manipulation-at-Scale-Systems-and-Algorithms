import sys
import re
import json

scores = {}
def word_dict(filename):
    for line in filename:
	term,score = line.split("\t")
	scores[term] = int(score)

def tweet_sentiment(filename2):
    for line in filename2:
	final_tweet_score = 0
	result = json.loads(line)
	str = result.get('text','zz').encode('utf-8')
	words_in_tweets = re.compile('\w+').findall(str)
	cal_score(words_in_tweets)

def cal_score(word):
    final_tweet_score=0
    for w in word:
	if w in scores.keys():
		senti_score = scores[w]
		final_tweet_score = final_tweet_score + senti_score
	else:
		senti_score = 0
		final_tweet_score = final_tweet_score + senti_score
    print final_tweet_score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    word_dict(sent_file)
    tweet_sentiment(tweet_file)

if __name__ == '__main__':
    main()
