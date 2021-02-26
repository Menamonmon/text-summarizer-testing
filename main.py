import os
import sys
import spacy
"""hi"""
def import_data(dataset_name):
	"""
	Takes the name of the dataset and reads the file into memory and returns it
	"""
	with open(f"./data/{dataset_name}.txt") as f:
		data = f.read()

	return data

def make_frequency_table(data):
	freqs = {}
	for word in data:
		if word in freqs:
			freqs[word] += 1
		else:
			freqs[word] = 1
	return freqs

def main():
	# Loading the Natural Language processing model
	nlp = spacy.load("en_core_web_sm")

	# Reading the dataset
	data = import_data("facebook")

	# Feeding the data into the model
	doc = nlp(data)

	# Dividing the data into sentences
	sentences = list(doc.sents)
	print(len(sentences))

	# STOP WORDS are words that are very common but don't contribute much to the meaning of the passage

	# Filtering the document so that we only have alphabetic words (excluding punctuation, numbers and stop words)
	tokens = [token for token in doc if token.is_alpha and not token.is_stop]

	# Lemmaization is the process of simplyfying the word so that it's in its most simple form
	# ex: walking  =>  walk
	token_lemmas = [token.lemma_ for token in tokens]
	word_scores_table = make_frequency_table(token_lemmas)
	
	# Sorting the table by the words that occur the most in the document
	table_to_list = [(key, value) for key, value in word_scores_table.items()]
	sorted_list = sorted(table_to_list, key=lambda x: x[1], reverse=True)

	# Printing all of the words that occur more than once
	sents_rank = []
	sent_len_min = 15
	for sent in sentences:
		if len(sent) < sent_len_min:
			continue

		sent_score = sum(word_scores_table.get(str(word.lemma_), 0) for word in sent) / len(sent)
		sents_rank.append((sent, sent_score))

	sents_sorted = sorted(sents_rank, key=lambda x: x[1], reverse=True)
	[print(sent) for (sent, score) in sents_sorted[:10]]

if __name__ == "__main__":
  main()