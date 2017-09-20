import argparse
import pprint
import numpy as np

from prep import untar
from prep import prep_data

from evaluation import predict_codes, vec_to_words, average_bleu, average_code_compilance

from model import get_model

ap = argparse.ArgumentParser()
ap.add_argument('--tar_path', type=str, default='./data.tar.gz')
ap.add_argument('--test_tar_path', type=str, default='./test.tar.gz')
ap.add_argument('--dataset', type=str, default='./data')
ap.add_argument('--test', type=str, default='./test')
ap.add_argument('--x_length', type=int, default=15)
ap.add_argument('--y_length', type=int, default=20)
ap.add_argument('--hidden_size', type=int, default=128)
ap.add_argument('--num_layers', type=int, default=2)
ap.add_argument('--model_weights', type=str, default='./model_weights.hdf5')

args = vars(ap.parse_args())

TAR_PATH = args['tar_path']
TEST_TAR_PATH = args['test_tar_path']
DATASET_PATH = args['dataset']
TEST_PATH = args['test']
INPUT_LENGTH = args['x_length']
OUTPUT_LENGTH = args['y_length']
HIDDEN_SIZE = args['hidden_size']
NUM_LAYERS = args['num_layers']
MODEL_WEIGHTS = args['model_weights']

if TAR_PATH is not None:
  untar(TAR_PATH)

if TEST_TAR_PATH is not None:
  untar(TEST_TAR_PATH)

X, Y, input_vocab, output_vocab, input_dict, output_dict = prep_data(DATASET_PATH, INPUT_LENGTH, OUTPUT_LENGTH)

X_test, Y_test, test_input_vocab, test_output_vocab, _, _ = prep_data(TEST_PATH, INPUT_LENGTH, OUTPUT_LENGTH)

auto_encoder = get_model(len(input_vocab),
                         INPUT_LENGTH,
                         len(output_vocab),
                         OUTPUT_LENGTH,
                         HIDDEN_SIZE,
                         NUM_LAYERS)
auto_encoder.load_weights(MODEL_WEIGHTS)

expected_codes = vec_to_words(Y_test, test_output_vocab)
codes = predict_codes(auto_encoder,
                      X_test,
                      input_dict,
                      INPUT_LENGTH,
                      output_vocab)

print '*************************************************'
print 'MODEL EVALUATION'
print(average_bleu(expected_codes, codes))
print(average_code_compilance(codes))
pprint.PrettyPrinter().pprint(codes)
print '*************************************************'
