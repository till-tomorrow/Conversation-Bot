import sys
import gensim, logging
# from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from tsne import bh_sne

plt.switch_backend('Qt4Agg')

def do_preprocessing(sentence):
	####### convert to lower case ######
	sentence = sentence.lower()
	####### remove punctuations #######
	tokenizer = RegexpTokenizer(r'\w+')
	sentence = tokenizer.tokenize(sentence)
	####### remove stopwords ##########
	stop = stopwords.words('english')
	sentence = [i for i in sentence if i not in stop]
	####### Don't append sentences with length = 0 or length > 10 #####
	if len(sentence) == 0:
		return None
	else:
		return sentence


def read_file(fname):
	sentences = list()
	f = open(fname,'r')
	for line in f:
		# line = line.split()
		line = do_preprocessing(line)
		if line != None:
			sentences.append(line)
	return sentences

def get_embeddings(sentences,count,size):
	model = gensim.models.Word2Vec(sentences,min_count=count,size=size,window=10,sg=0)
	return model

def get_points(model):
	X = list()
	y = list()
	for word in model.vocab.keys():
		X.append(model[word])
		y.append(word)
	return X,y

def perform_tsne_transformation(X):
	######### There is a bug in scikit-learn, hence cant do tsne with it. ##############
	# tsne_model = TSNE(n_components=2,random_state=0)
	# X_new = tsne_model.fit_transform(X)

	X = np.asarray(X).astype('float64')
	X = X.reshape((X.shape[0],-1))
	X_new = bh_sne(X,perplexity=5)
	return X_new

def get_tsne_plot(X,y):
	fig,ax = plt.subplots()
	ax.scatter(X[:,0],X[:,1])
	for i,label in enumerate(y):
		ax.annotate(label,(X[i,0],X[i,1]))
	plt.show()
	# plt.savefig('foo.png')

def save_embeddings_model(model):
	model.save("embeddings")


def start_embedding_process(fname):
	# min_count = [5,10,15,20]
	# hidden_size = [100,120,130,150,180,200]
	min_count = 5
	hidden_size = 100
	sentences = read_file(fname)
	# for m_count in min_count:
		# for h_size in hidden_size:
	# print "\n\nPerforming with %d hidden layes size and %d min count in vocab:\n"%(h_size,m_count)
	model = get_embeddings(sentences,min_count,hidden_size)
	save_embeddings_model(model)
	X,y = get_points(model)
	X_new = perform_tsne_transformation(X)
	get_tsne_plot(X_new,y)
	return (X_new,y)


# if __name__ == '__main__':
# 	fname = sys.argv[1]
# 	main(fname)

