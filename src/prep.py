from os import listdir
from os.path import join

import numpy as np
import re

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

def dictionary(words):
  words_count = len(words)
  words_dict = {}

  for i in range(0, len(words)):
    encoded_word = np.zeros(words_count)
    encoded_word[i] = 1
    words_dict[words[i]] = encoded_word

  return words_dict
