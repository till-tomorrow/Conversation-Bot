import sys

import intent_identification as intent

def get_word_to_cluster_mappings(clusters,mappings,query_with_pos,query_intent='search'):
	length_dict = {'maxi':['long','maxi','max'],'midi':['medium','midi','mid'],'mini':['short','mini','min']}
	size_dict = {'small':['s','small'],'medium':['m','medium'],'large':['l','large'],'extra_large':['xl','extra large','']}
	candidate_tocs = []
	candidate_colors = []
	candidate_lengths = []
	candidate_sizes = []

	for qpos in query_with_pos:
		if qpos[1] == 'n' or qpos[1] == 'a':
			candidate_tocs.append(qpos[0])
			candidate_colors.append(qpos[0])
			candidate_sizes.append(qpos[0])
			candidate_lengths.append(qpos[0])
			
	toc = color = size = length = None

	if mappings['color'] == None:
		for cluster in clusters:
			if cluster.name == 'color':
				color = set(candidate_colors) & set(cluster.words)
				if bool(color):
					mappings['color'] = color
				break

	if mappings['toc'] == None:
		for cluster in clusters:
			if cluster.name == 'toc':
				toc = set(candidate_tocs) & set(cluster.words)
				if bool(toc):
					mappings['toc'] = toc
				break

	if mappings['size'] == None:
		for s,values in size_dict.iteritems():
			if bool(set(values) & set(candidate_sizes)):
				size = set(values) & set(candidate_sizes)
				mappings['size'] = size
				break

	if mappings['length'] == None:
		for l,values in length_dict.iteritems():
			if bool(set(values) & set(candidate_lengths)):
				length = set(values) & set(candidate_lengths)
				mappings['length'] = length
				break

	return mappings


def start_chat(clusters):
	flag = True
	i = 0
	mappings = {'length':None,'size':None,'color':None,'toc':None}
	print "\n\n\n\nHello! What are you interested in?"
	while flag:
		query = input()
		query_intent,query_with_pos = intent.get_intent_and_lemmatized_query(query)
		mappings = get_word_to_cluster_mappings(clusters,mappings,query_with_pos)
		print "\n\nMappings: ",mappings,"\n\n"
		# flag = False
		if mappings['length'] == None:
			print "What length are you looking for(maxi,midi,mini)?"
		elif mappings['size'] == None:
			print "What size are you looking for(s,m,l,xl)?"
		elif mappings['color'] == None:
			print "What color are you looking for?"
		elif mappings['toc'] == None:
			print "What type of clothing are you looking for?"

		if None not in mappings.viewvalues():
			flag = False

def main():
	pass


if __name__ == '__main__':
	main()