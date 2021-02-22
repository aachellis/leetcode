from collections import Counter
def firstUniqChar(s):
	counter = Counter(s)
	for index, item in enumerate(s):
		if counter[item] == 1:
			return index
	return -1

print(firstUniqChar("leetcode"))
