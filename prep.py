from os import listdir
from os.path import join

import re
import gensim

def file_paths(data_path):
  return [join(data_path, name) for name in listdir(data_path)]

def training_data(data_path):
  paths = file_paths(data_path)
  raw_text = [open(path, 'r').read() for path in paths]

  dataX = []
  dataY = []
  for text in raw_text:
    data = split_data(text)
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
    return re.findall(r"[\w']+|[.,!?;:()/\[\]]/", sentence)

def word_to_vec_model(sentences):
  return gensim.models.Word2Vec(sentences, min_count=1, workers=2)
