import sys

import word_embeddings as we
import clustering as c
import chat

def main(fname):
	X,y = we.start_embedding_process(fname)
	clusters = c.get_clusters(X,y)
	# exit(0)
	chat.start_chat(clusters)


if __name__ == '__main__':
	fname = sys.argv[1]
	main(fname)