"""
Basic statistics functions
"""
import math
from collections import Counter

def mean(x):
	return sum(x)/len(x)

def median(x):
	n = len(x)
	sorted_x = sorted(x)
	midpoint = n // 2

	if n % 2 == 1:
		'''if odd, return the middle value'''
		return sorted_x[midpoint]
	else:
		# if even, return the average of the two values near the middle
		lo = midpoint-1
		hi = midpoint
		return (sorted_x[lo] + sorted_x[hi]) / 2

def quantile(x,p):
	'''returns the p-th percentile value in x
	value of p should be between 0 and 1'''
	p_index = int(p * len(x))
	return sorted(x)[p_index]

def mode(x):
	'''returns a list with the most common value/values'''
	counts = Counter(x)
	max_count = max(counts.values())
	return [x_i for x_i, count in counts.iteritems() if count == max_count]

def deviation(x):
	'''translate x by substracting its mean'''
	x_bar = mean(x)
	return [x_i - x_bar for x_i in x]

def dot_product(x,y):
	"""computes the dot product of the two vectors"""
	return sum(x_i * y_i for x_i, y_i in zip(x,y))

def squared_sum(x):
	"""v_1 * v_1 + ... + v_n * v_n"""
	return dot(x,x)

def variance(x):
	n=len(x)
	deviations = deviation(x)
	return squared_sum(deviations)/ (n-1)

def standard_dev(x):
	return math.sqrt(variance(x))

def interquartile_range(x):
	return quantile(x, 0.75) - quantile(x,0.25)

def covariance(x,y):
	n = len(x)
	return dot_product(deviation(x),deviation(y)) / (n-1)

def correlation(x,y):
	std_x = standard_dev(x)
	std_y = standard_dev(y)
	if std_x > 0 and std_y > 0:
		return covariance(x,y) / std_x / std_y


