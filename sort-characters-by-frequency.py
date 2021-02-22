from collections import Counter
import operator
def frequencySort(s):
	counter = Counter(s)
	res = ''
	sorted_counter = dict(sorted(counter.items(), key = operator.itemgetter(1), reverse = True))
	print(sorted_counter)
	for element in sorted_counter:
		for iterator in range(sorted_counter[element]):
			res += element
	return res


print(frequencySort("tree"))