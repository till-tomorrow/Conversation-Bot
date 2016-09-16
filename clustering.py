import sys
import math
import itertools
import operator
import random

mappings = {"color":["red","green","blue","yellow","pink","white","black",\
 "orange","purple","brown","beige","gray","silver","gold","teal"],\
  "toc":['dress','short','shirt','pant','tshirt'],"size":['s','small','m','medium','l','large'],\
 "length":['maxi','midi','mini']}

class Cluster(object):

	def __init__(self,index,center):
		self.index = index 
		self.name = 'NO_NAME'
		self.center = center
		self.points = []
		self.words = []

	def recenter(self):
		dim = len(self.center)
		dist = [0.0 for i in range(dim)]
		for point in self.points:
			for i in xrange(dim):
				dist[i] += float(point[i])	
		self.center = [float(dist[x])/float(len(self.points)) for x in range(dim)]

	def reinitialize_points(self):
		self.points = []
		self.words = []


def get_random_centroids(points,k):
	centroids = random.sample(points,k)
	return centroids


#Function to calculate the eucledian distance between two points
def get_distance(point1,point2):
	dim = len(point1)
	sqdist = sum([math.pow(float(point1[d])-float(point2[d]),2) for d in range(dim)])
	return math.sqrt(sqdist)


def kmeans(points,labels,centroids,k,itr):
	clusters = []
	for i in xrange(k):
		cluster = Cluster(i+1,centroids[i])
		clusters.append(cluster)

	for i in xrange(itr):
		for x,y in zip(points,labels):
			min_dist = float('inf')
			for index,cluster in enumerate(clusters):
				dist = get_distance(x,cluster.center)
				if min_dist > dist:
					min_dist = dist
					min_index = index
			clusters[min_index].points.append(x)
			clusters[min_index].words.append(y)

		if not i == itr-1:
			for cluster in clusters:
				cluster.recenter()
				cluster.reinitialize_points()

	return clusters

def get_cluster_name(clusters):
	for key,value in mappings.iteritems():
		count = {}
		for v in value:
			for cluster in clusters:
				if v in cluster.words:
					# print v, cluster.words
					if cluster.index in count:
						count[cluster.index] += 1
					else:
						count[cluster.index] = 1
					break
					
		if any(count):
			max_index = max(count.iteritems(),key=operator.itemgetter(1))[0]
			for cluster in clusters:
				if cluster.index == max_index:
					cluster.name = key

	for cluster in clusters:
		print cluster.name, cluster.words


def print_clusters(clusters):
	for index,cluster in enumerate(clusters):
		print "printing for cluster: %d\n"%(index)
		for x,y in zip(cluster.points,cluster.words):
			print x,y

def get_clusters(points,labels):
	k = 4
	itr = 100
	centroids = get_random_centroids(points,k)
	clusters = kmeans(points,labels,centroids,k,itr)
	print_clusters(clusters)
	get_cluster_name(clusters)
	return clusters

if __name__ == '__main__':
	########## main function is just for testing ###########
	word_list = [['dress','shirt','tshirt'],['small','medium','large'],['maxi','mini','midi'],['green','yellow','brown']]
	clusters = []
	for i in xrange(4):
		cluster = Cluster(i+1,i+10)		
		cluster.words = word_list[i]
		clusters.append(cluster)
	get_cluster_name(clusters)


