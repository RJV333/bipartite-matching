import networkx as nx
from networkx.algorithms import bipartite
import random
import time

def test1():
	B = nx.Graph()
	B.add_nodes_from([1,2,3,4,5,6,7,8,9,10], bipartite=0) # Add the node attribute "bipartite"
	B.add_nodes_from(['a','b','c','d','e','f','g'], bipartite=1)
	B.add_edge(1, 'a', weight = 10)
	B.add_edge(1, 'b', weight = 5)
	B.add_edge(1, 'c', weight = 1)

	B.add_edge(2, 'a', weight = 1)
	B.add_edge(2, 'b', weight = 10)

	B.add_edge(3, 'a', weight = 5)

	B.add_edge(4, 'b', weight = 1)

	B.add_edge(5, 'c', weight = 5)

	B.add_edge(6, 'c', weight = 1)
	B.add_edge(6, 'd', weight = 5)
	B.add_edge(6, 'e', weight = 10)

	B.add_edge(7, 'd', weight = 1)
	B.add_edge(7, 'e', weight = 5)

	B.add_edge(8, 'f', weight = 5)

	B.add_edge(9, 'f', weight = 10)

	B.add_edge(10, 'e', weight = 10)
	B.add_edge(10, 'f', weight = 1)
	B.add_edge(10, 'g', weight = 5)
	#B.add_edges_from([(1,'a'), (1,'b'), ((2,'b'), (2,'c'), (3,'c'), (4,'a')])

	res = nx.algorithms.matching.max_weight_matching(B, maxcardinality=False)
	return res

def test2():
	B = nx.Graph()
	B.add_nodes_from([1,2,3], bipartite=0) # Add the node attribute "bipartite"
	B.add_nodes_from([5, 6], bipartite=1)

	B.add_edge(1, 5, weight = 3)
	B.add_edge(1, 6, weight = 99)
	B.add_edge(2, 6, weight = 1)
	B.add_edge(3, 6, weight = 2)
	res = nx.algorithms.matching.max_weight_matching(B, maxcardinality=False)
	return res
def test2b():
	B = nx.Graph()
	B.add_nodes_from([1,2,3], bipartite=0) # Add the node attribute "bipartite"
	B.add_nodes_from([5, 6], bipartite=1)

	B.add_edge(1, 5, weight = 3)
	B.add_edge(1, 6, weight = 4)
	B.add_edge(2, 6, weight = 1)
	B.add_edge(3, 6, weight = 2)
	res = nx.algorithms.matching.max_weight_matching(B, maxcardinality=False)
	return res

def test3():
	B = nx.Graph()
	B.add_nodes_from([1,2,3,4,5,6,7], bipartite=0)
	B.add_nodes_from(['a','b','c','d','e'], bipartite=1)

	B.add_edge(1, 'a', weight = 1)

	B.add_edge(2, 'a', weight = 2)
	B.add_edge(2, 'b', weight = 3)

	B.add_edge(3, 'b' ,weight = 1)

	B.add_edge(4, 'b', weight = 2)
	B.add_edge(4, 'c', weight = 3)

	B.add_edge(5, 'c', weight = 1)
	B.add_edge(5, 'd', weight = 2)

	B.add_edge(6, 'd', weight = 3)
	B.add_edge(6, 'e', weight = 1)

	B.add_edge(7, 'd', weight = 2)

	B.add_edge(8, 'e', weight = 3)

	res = nx.algorithms.matching.max_weight_matching(B, maxcardinality=False)
	return res

def test4():
	B = nx.Graph()
	B.add_nodes_from([1,2,3,4,5,6,7], bipartite=0)
	B.add_nodes_from(['a','b','c','d','e'], bipartite=1)

	B.add_edge(1, 'a', weight = 6)

	B.add_edge(2, 'a', weight = 2)
	B.add_edge(2, 'b', weight = 4)

	B.add_edge(3, 'b' ,weight = 6)

	B.add_edge(4, 'b', weight = 2)
	B.add_edge(4, 'c', weight = 4)

	B.add_edge(5, 'c', weight = 6)
	B.add_edge(5, 'd', weight = 2)

	B.add_edge(6, 'd', weight = 4)
	B.add_edge(6, 'e', weight = 6)

	B.add_edge(7, 'd', weight = 2)

	B.add_edge(8, 'e', weight = 4)

	res = nx.algorithms.matching.max_weight_matching(B, maxcardinality=False)
	return res

def test5():
	start = time.time()
	B = nx.Graph()
	B.add_nodes_from([i for i in range(1000)], bipartite=0)
	B.add_nodes_from([i for i in range(1000, 20000)], bipartite=1)

	for i in range(1000):
		for r in range(1000, 2000):
			if i == (r-1000):
				B.add_edge(i, r, weight = 100)
			else:
				B.add_edge(i, r, weight = random.randint(95, 99) )
	print "made it here"
	res = nx.algorithms.matching.max_weight_matching(B, maxcardinality=False)
	end = time.time()
	print(end-start)
	return res

def test6():
	#test2 on a larger scale
	start = time.time()
	B = nx.Graph()
	B.add_nodes_from([i for i in range(999)], bipartite=0)
	B.add_nodes_from([i for i in range(999, 1665)], bipartite=1)

	i = 0
	r = 999
	while(i<998):
		B.add_edge(i, r, weight = 3)
		B.add_edge(i, r+1, weight = 100)
		B.add_edge(i+1, r+1, weight = 1)
		B.add_edge(i+2, r+1, weight = 2)
		i+=3
		r+=2
	print "made it here"
	res = nx.algorithms.matching.max_weight_matching(B, maxcardinality=False)
	end = time.time()
	print(end-start)
	return res

def test7():
	#2b on larger scale
		#test2 on a larger scale
	start = time.time()
	B = nx.Graph()
	B.add_nodes_from([i for i in range(999)], bipartite=0)
	B.add_nodes_from([i for i in range(999, 1665)], bipartite=1)

	i = 0
	r = 999
	while(i<998):
		B.add_edge(i, r, weight = 3)
		B.add_edge(i, r+1, weight = 4)
		B.add_edge(i+1, r+1, weight = 1)
		B.add_edge(i+2, r+1, weight = 2)
		i+=3
		r+=2
	print "made it here"
	res = nx.algorithms.matching.max_weight_matching(B, maxcardinality=False)
	end = time.time()
	print(end-start)
	return res

def test8():
	#2b on larger scale
		#test2 on a larger scale
	start = time.time()
	B = nx.Graph()
	B.add_nodes_from([i for i in range(999)], bipartite=0)
	B.add_nodes_from([i for i in range(999, 1665)], bipartite=1)

	i = 0
	r = 999
	while(i<998):
		B.add_edge(i, r, weight = 3)
		B.add_edge(i+1, r, weight = 3)
		B.add_edge(i+2, r, weight = 3)

		B.add_edge(i+1, r+1, weight = 1)
		B.add_edge(i+2, r+1, weight = 2)
		i+=2
		r+=2
	print "made it here"
	res = nx.algorithms.matching.max_weight_matching(B, maxcardinality=False)
	end = time.time()
	print(end-start)
	return res	

def test9():
	#Alternation on test8
	start = time.time()
	B = nx.Graph()
	B.add_nodes_from([i for i in range(999)], bipartite=0)
	B.add_nodes_from([i for i in range(999, 1665)], bipartite=1)

	i = 0
	r = 999
	while(i<998):
		B.add_edge(i, r, weight = 4)
		B.add_edge(i+1, r, weight = 3)
		B.add_edge(i+2, r, weight = 3)

		B.add_edge(i+1, r+1, weight = 2)
		B.add_edge(i+2, r+1, weight = 1)
		i+=2
		r+=2
	print "made it here"
	res = nx.algorithms.matching.max_weight_matching(B, maxcardinality=False)
	end = time.time()
	print(end-start)
	return res	