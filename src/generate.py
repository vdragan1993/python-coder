import argparse
import numpy as np

from prep import untar
from prep import prep_data
from prep import split_to_words
from prep import word_to_index
from prep import pad_seq

from model import get_model

ap = argparse.ArgumentParser()
ap.add_argument('--tar_path', type=str)
ap.add_argument('--dataset', type=str, default='./data')
ap.add_argument('--x_length', type=int)
ap.add_argument('--y_length', type=int)
ap.add_argument('--hidden_size', type=int, default=128)
ap.add_argument('--num_layers', type=int, default=2)
ap.add_argument('--model_weights', type=str, default='./model_weights.hdf5')

args = vars(ap.parse_args())

TAR_PATH = args['tar_path']
DATASET_PATH = args['dataset']
INPUT_LENGTH = args['x_length']
OUTPUT_LENGTH = args['y_length']
HIDDEN_SIZE = args['hidden_size']
NUM_LAYERS = args['num_layers']
MODEL_WEIGHTS = args['model_weights']

if TAR_PATH is not None:
  untar(TAR_PATH)

X, Y, input_vocab, output_vocab, input_dict, output_dict = prep_data(DATASET_PATH, INPUT_LENGTH, OUTPUT_LENGTH)

auto_encoder = get_model(len(input_vocab),
                         INPUT_LENGTH,
                         len(output_vocab),
                         OUTPUT_LENGTH,
                         HIDDEN_SIZE,
                         NUM_LAYERS)
auto_encoder.load_weights(MODEL_WEIGHTS)

sentence = 'print false if 1 appears in array [2, 2]'
words = split_to_words(sentence)

X_test = word_to_index([words], input_dict)
X_test = pad_seq(X_test, INPUT_LENGTH)

'''
predictions = np.argmax(auto_encoder.predict(X_test), axis=2)
sequences = []

for prediction in predictions:
  sequence = ' '.join([output_vocab(index) for index in prediction if index > 0])
  print(sequence)
  sequences.append(sequence)

np.savetxt('test_result', sequences, fmt='%s')
'''

predictions = auto_encoder.predict(X_test)

for sentence in predictions:
  for words in sentence:
    print(output_vocab[np.argmax(words)])

print(predictions.shape)
