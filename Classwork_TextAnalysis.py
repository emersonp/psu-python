text_file = open("Classwork_OriginalText.txt", "r")
word_dictionary = {}
total_para = 0
total_sentence = 0
total_word = 0
para_length = []
sentence_length = []
word_length = []



def import_text(text_file):
  str_line = text_file.read()
  return str_line

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
  sentence_array = split_para(para)
  for sentence in sentence_array:
    if len(sentence) == 0:
      continue
    total_sentence += 1
    word_array = split_sentence(sentence)
    for word in word_array:
      if len(word) == 0:
        continue
      total_word += 1
      word_length.append(len(word))
      input_word = word.lower()
      if input_word in word_dictionary:
        word_dictionary[input_word] += 1
      else:
        word_dictionary[input_word] = 1

print("Paragraphs:", total_para)
print("Sentences:", total_sentence)
print("Words:", total_word)
print(word_dictionary)
print("Average Word Length:", format(float(sum(word_length) / len(word_length)), ".2f"))
