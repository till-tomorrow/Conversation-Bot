import sys

from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

intent_dict = {"get":"search","examine":"search","look":"search","show":"search","buy":"search"}


def get_tokens_pos_tag(tag):
	if tag.startswith('J'):
		return wordnet.ADJ
	elif tag.startswith('V'):
		return wordnet.VERB
	elif tag.startswith('N'):
		return wordnet.NOUN
	elif tag.startswith('R'):
		return wordnet.ADV
	else:
		return ''


def get_pos(tokens):
	tokens_pos = pos_tag(tokens)
	tokens_pos = [(pos[0],get_tokens_pos_tag(pos[1])) for pos in tokens_pos]
	# print tokens_pos
	return tokens_pos

def do_lemmatisation(tokens,tokens_pos):
	lemmatiser = WordNetLemmatizer()
	output_lemmatisation = [(lemmatiser.lemmatize(pos[0],pos=pos[1]),pos[1]) for pos in tokens_pos if pos[1] != '']
	# print output_lemmatisation
	return output_lemmatisation


def do_preprocessing(msg):
	tokens = word_tokenize(msg)
	tokens_pos = get_pos(tokens)
	output_lemmatisation = do_lemmatisation(tokens,tokens_pos)
	return output_lemmatisation


def get_intent_and_lemmatized_query(msg):
	msg = do_preprocessing(msg)
	print "\n\nQuery with pos: ",msg,"\n\n"
	for word in msg:
		if word[0] in intent_dict.keys():
			return (intent_dict[word[0]],msg)
	return('',msg)


def main():
	msg = "get me some clothing apparels"
	# intent = get_intent(msg)
	do_preprocessing(msg)
	# print intent

if __name__ == '__main__':
	main()


