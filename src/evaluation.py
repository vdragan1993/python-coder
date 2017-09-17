import numpy as np
import ast
from nltk.translate import bleu_score

from prep import split_to_words
from prep import word_to_index
from prep import pad_seq

def vec_to_words(predictions, vocab):
  codes = []
  for prediction in predictions:
    code = [vocab[np.argmax(words)] for words in prediction]
    codes.append(' '.join([word for word in code if word != 'ZERO']))

  return codes

def predict_codes(auto_encoder,
                  sentences,
                  input_dict,
                  input_length,
                  output_vocab):

  predictions = auto_encoder.predict(sentences)

  return vec_to_words(predictions, output_vocab)

def code_compiles(code):
    """
    Check if given Python code compiles
    :param code: Python source code as string
    :return: True or False
    """
    try:
        ast.parse(code)
    except SyntaxError:
        return False
    return True

def calculate_bleu(original, translated):
    """
    Calculates BLEU score for translated code
    :param source: original source code string
    :param translated: translated source code string
    :return: BLEU score
    """
    hypothesis = list(translated)
    reference = list(original)
    return bleu_score.sentence_bleu([reference], hypothesis)

def average_bleu(original, translated):
  sum = 0

  for i in range(0, len(original)):
    sum += calculate_bleu(original[i], translated[i])

  return sum / len(original)

def average_code_compilance(codes):
  count = 0

  for code in codes:
    if code_compiles(code):
      count += 1

  return count / len(codes)
