# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 13:38:02 2018

@author: jamespatten
"""

import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')

from nltk import word_tokenize, pos_tag, ne_chunk

if __name__ == "__main__":

	sentence = "James Patten wants to join CDV"
	tokens = nltk.word_tokenize(sentence)
	print("tokens = %s" % tokens)

	tagged = nltk.pos_tag(tokens)

	entities = nltk.chunk.ne_chunk(tagged)
	print("entities = %s" % entities)