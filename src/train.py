import pprint
import argparse
import numpy as np

from prep import untar
from prep import prep_data

from evaluation import average_code_compilance, average_bleu, predict_codes, vec_to_words

from model import get_model

ap = argparse.ArgumentParser()
ap.add_argument('--tar_path', type=str, default='./data.tar.gz')
ap.add_argument('--test_tar_path', type=str, default='./test.tar.gz')
ap.add_argument('--dataset', type=str, default='./data')
ap.add_argument('--test', type=str, default='./test')
ap.add_argument('--x_length', type=int, default=15)
ap.add_argument('--y_length', type=int, default=20)
ap.add_argument('--epochs', type=int, default=50)
ap.add_argument('--hidden_size', type=int, default=128)
ap.add_argument('--num_layers', type=int, default=2)
ap.add_argument('--batch_size', type=int, default=32)

args = vars(ap.parse_args())

TAR_PATH = args['tar_path']
TEST_TAR_PATH = args['test_tar_path']
DATASET_PATH = args['dataset']
TEST_PATH = args['test']
INPUT_LENGTH = args['x_length']
OUTPUT_LENGTH = args['y_length']
EPOCHS = args['epochs']
HIDDEN_SIZE = args['hidden_size']
NUM_LAYERS = args['num_layers']
BATCH_SIZE = args['batch_size']

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

auto_encoder.summary()

k_start = 1

X = np.array(X)
Y = np.array(Y)

for k in range(k_start, EPOCHS + 1):
  # Shuffling the training data every epoch to avoid local minima
  indices = np.arange(len(X))
  # np.random.shuffle(indices)
  X = X[indices]
  Y = Y[indices]

  # Training 32 sequences at a time
  for i in range(0, len(X), 32):
    if i + 32 >= len(X):
      i_end = len(X)
    else:
      i_end = i + 32

    # y_sequences = process_data(y[i:i_end], y_max_len, y_word_to_ix)

    print('[INFO] Training model: epoch {}th {}/{} samples'.format(k, i, len(X)))
    auto_encoder.fit(X[i:i_end], Y[i:i_end], batch_size=BATCH_SIZE, epochs=1, verbose=2)
    auto_encoder.save_weights('/output/checkpoint_epoch_{}.hdf5'.format(k))

  expected_codes = vec_to_words(Y_test, test_output_vocab)
  codes = predict_codes(auto_encoder,
                        X_test,
                        input_dict,
                        INPUT_LENGTH,
                        output_vocab)

  print('*************************************************')
  print('MODEL EVALUATION')
  print(average_bleu(expected_codes, codes))
  print(average_code_compilance(codes))
  pprint.PrettyPrinter().pprint(codes)
  print('*************************************************')
