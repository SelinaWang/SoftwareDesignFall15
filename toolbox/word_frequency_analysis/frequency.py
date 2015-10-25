""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	word_list =[]

	# loading the file and stripping away the header and bottom comment
	f = open(file_name,'r')
	lines = f.readlines()
	header_line = 0
	while lines[header_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		header_line += 1
	end_line = header_line
	while lines[end_line].find('END OF THIS PROJECT GUTENBERG EBOOK') == -1:
		end_line += 1
	lines = lines[header_line+1:end_line-1]
	
	# Get rid of all the non-text stuff
	for line in lines:
		# replace non-text with spaces before splitting
		for val in string.punctuation:
			line = line.replace(str(val), ' ')
		line = line.lower()
		line = line.split()
		for word in line:
			word_list.append(word)
	print "Total number of words: " + str(len(word_list))
	return word_list


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	word_counts = {}
	for word in word_list:
		if word_counts.has_key(word):
			word_counts[word] +=1
		else:
			word_counts.update({word:1})
	print 'Number of different words: ' + str(len(word_counts))
	# Return a sorted list of the word frequency from the most to the least
	ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)

	return ordered_by_frequency[0:n]

if __name__ == '__main__':
	word_list = get_word_list('sherlock.txt')
	print get_top_n_words(word_list,100)