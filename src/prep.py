from os import listdir
from os.path import join
import tarfile

import numpy as np
from keras.preprocessing.sequence import pad_sequences
import re

def prep_data(dataset_path):
  input_sentences, output_sentences = training_data(dataset_path)

  input_words = []
  for sentence in input_sentences:
    input_words += sentence

  output_words = []
  for sentence in output_sentences:
    output_words += sentence

  # number of words each sentence will be padded to
  input_length = max_sentence_length(input_sentences)
  output_length = max_sentence_length(output_sentences)

  # vocabularies (array of all distinct words in data set)
  # add "ZERO" as first element of vocabularies
  # add "UNK" as last element of vocabularies
  input_vocab = vocabulary(input_words)
  input_vocab.insert(0, 'ZERO')
  input_vocab.append('UNK')
  output_vocab = vocabulary(output_words)
  output_vocab.insert(0, 'ZERO')
  output_vocab.append('UNK')

  # create word to index dictionaries based on vocabulary(array of words)
  input_dict = dictionary(input_vocab)
  output_dict = dictionary(output_vocab)

  # transform words to be indexes in the vocabulary
  X = word_to_index(input_sentences, input_dict)
  Y = word_to_index(output_sentences, output_dict)

  # pad sequences so every sentence has the same number of words
  X = pad_seq(X, input_length)
  Y = pad_seq(Y, output_length)

  # vectorize output words
  Y = vectorize_sentences(Y,len(output_vocab))

  return (X, Y,
          input_vocab, output_vocab,
          input_dict, output_dict,
          input_length, output_length)

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
