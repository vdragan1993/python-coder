from os import listdir
from os.path import join
import tarfile

import numpy as np
from keras.preprocessing.sequence import pad_sequences
import re

def untar(tar_path):
  with tarfile.open(tar_path) as tf:
    tf.extractall(path='./', members=None)

def file_paths(data_path):
  return [join(data_path, name) for name in listdir(data_path)]

def training_data(data_path):
  paths = file_paths(data_path)
  raw_text = [open(path, 'r').read() for path in paths]

  dataX = []
  dataY = []
  for text in raw_text:
    data = split_data(text)
    # reverse order of input words to boost lstm performance
    dataX.append(split_to_words(data[0]))
    dataY.append(split_to_words(data[1]))

  return dataX, dataY

# split inputs and outputs from data
def split_data(text):
  lines = text.split('\n')

  # first line without first character (#)
  input_text = lines.pop(0)[1:]
  # the rest of the text
  output_text = '\n'.join(lines)

  return input_text, output_text

def split_to_words(sentence):
  return re.findall(r"[\w]+|[^\s\w]", sentence)
  # return re.findall(r"[\w']+|[.,!?;:()\"]", sentence)

def max_sentence_length(sentences):
  return max([len(sentence) for sentence in sentences])

def dictionary(vocabulary):
  return { word:ix for ix, word in enumerate(vocabulary) }

def vocabulary(words):
  return list(set(words))

def pad_seq(sequences, max_length):
  return pad_sequences(sequences, maxlen=max_length, dtype="int32")

def word_to_index(words, dictionary):
  for i, sentence in enumerate(words):
    for j, word in enumerate(sentence):
      words[i][j] = dictionary.get(word, dictionary['UNK'])

  return words

def vectorize_sentences(sentences, max_length):
  vectorized_sentences = []
  for sentence in sentences:

    vectorized_sentence = []
    for word in sentence:
      vectorized_word = np.zeros(max_length)
      vectorized_word[word] = 1
      vectorized_sentence.append(vectorized_word)

    vectorized_sentences.append(vectorized_sentence)

  return vectorized_sentences
