# Copyright (c) 2014 Parker Harris Emerson
# Textual Analysis Program

# This program inputs a hardcoded text file and analyzes it, measuring
# various metrics: word/sentence/paragraph count, averages, and
# most frequent words.

import operator

# EDIT THIS HARDCODE FILE TO CHANGE INPUT TEXT
text_file = open("Classwork_OriginalText.txt", "r")

word_dictionary = {}
total_para = 0
total_sentence = 0
total_word = 0
para_length = []
sentence_length = []
word_length = []
words_in_sentence = 0
sentences_in_para = 0

BLACK_LIST = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "in", "for", "not", "on", "with", "he", "as", "you", "do", "at", "is", "it", "this", "but", "his", "are", "or"]

# Non-sentence-ending punctuation
PUNCTUATION = ["$", ",", ";", ":", "/", "(", ")", "-"]

def import_text(text_file):
  return text_file.read()

def split_text(text):
  return text.split("\n")

def split_para(para):
  return para.replace("?", ".").replace("!", ".").replace(". ", ".").split(".")

def split_sentence(sentence):
  return sentence.split(" ")


text = import_text(text_file)
para_array = split_text(text)
for para in para_array:
  if len(para) == 0:
    continue
  total_para += 1
  sentences_in_para = 0
  sentence_array = split_para(para)
  for sentence in sentence_array:
    if len(sentence) == 0:
      continue
    total_sentence += 1
    sentences_in_para += 1
    words_in_sentence = 0
    word_array = split_sentence(sentence)
    for word in word_array:
      if len(word) == 0:
        continue
      total_word += 1
      words_in_sentence += 1
      word_length.append(len(word))
      input_word = word.lower()
      for punct in PUNCTUATION:
        input_word.replace(punct, "")
      if input_word in word_dictionary:
        word_dictionary[input_word] += 1
      else:
        word_dictionary[input_word] = 1
    sentence_length.append(words_in_sentence)
  para_length.append(sentences_in_para)

# SORT WORDS BY FREQUENCY
sorted_word_length = sorted(word_dictionary, key=word_dictionary.__getitem__, reverse=True)[:5]

# REMOVE BLACKLIST WORDS
for word in word_dictionary:
  if word in BLACK_LIST:
    word_dictionary[word] = 0

# SORT WORDS BY FREQUENCY / WHITELIST
bl_sorted_word_length = sorted(word_dictionary, key=word_dictionary.__getitem__, reverse=True)[:5]

print("\nPARAGRAPHS\nParagraphs:", total_para)
print("Average Number of Sentences in Paragraph:", format(float(sum(para_length) / len(para_length)), ".2f"))
print("\nSENTENCES\nSentences:", total_sentence)
print("Average Number of Words in Sentence:", format(float(sum(sentence_length) / len(sentence_length)), ".2f"))
print("\nWORDS\nWords:", total_word)
#print(word_dictionary)
print("Five most used words:", sorted_word_length[:5])
print("Five most used words (after blacklist):", bl_sorted_word_length[:5])
print("Average Word Length:", format(float(sum(word_length) / len(word_length)), ".2f"))


print("\n" * 10)
text_file.close()
