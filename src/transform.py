import numpy as np

from prep import split_to_words
from prep import word_to_index
from prep import pad_seq

def vec_to_words(prediction, output_vocab):
  return [output_vocab[np.argmax(words)] for sentence in prediction for words in sentence]
  # for sentence in predictions:
  #   for words in sentence:
  #     print(output_vocab[np.argmax(words)])

def prediction_to_code(auto_encoder,
                            sentence,
                            input_dict,
                            input_length,
                            output_vocab):

  words = split_to_words(sentence)

  X = word_to_index([words], input_dict)
  X = pad_seq(X, input_length)

  predictions = auto_encoder.predict(X)

  return vec_to_words(predictions, output_vocab)
