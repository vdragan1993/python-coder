import numpy as np
import argparse

from prep import untar
from prep import prep_data

from model import get_model

ap = argparse.ArgumentParser()
ap.add_argument('--tar_path', type=str)
ap.add_argument('--dataset', type=str, default='./data')
ap.add_argument('--n_epochs', type=int, default=20)
ap.add_argument('--hidden_size', type=int, default=100)
ap.add_argument('--num_layers', type=int, default=3)
ap.add_argument('--batch_size', type=int, default=1000)

args = vars(ap.parse_args())

TAR_PATH = args['tar_path']
DATASET_PATH = args['dataset']
N_EPOCHS = args['n_epochs']
HIDDEN_SIZE = args['hidden_size']
NUM_LAYERS = args['num_layers']
BATCH_SIZE = args['batch_size']

if TAR_PATH is not None:
  untar(TAR_PATH)

X, Y, input_vocab, output_vocab, input_dict, output_dict, input_length, output_length = prep_data(DATASET_PATH)

auto_encoder = get_model(len(input_vocab),
                         input_length,
                         len(output_vocab),
                         output_length,
                         HIDDEN_SIZE,
                         NUM_LAYERS)

k_start = 1

X = np.array(X)
Y = np.array(Y)

for k in range(k_start, N_EPOCHS + 1):
  # Shuffling the training data every epoch to avoid local minima
  indices = np.arange(len(X))
  np.random.shuffle(indices)
  X = X[indices]
  Y = Y[indices]

  # Training 1000 sequences at a time
  for i in range(0, len(X), 1000):
    if i + 1000 >= len(X):
      i_end = len(X)
    else:
      i_end = i + 1000

    # y_sequences = process_data(y[i:i_end], y_max_len, y_word_to_ix)

    print('[INFO] Training model: epoch {}th {}/{} samples'.format(k, i, len(X)))
    auto_encoder.fit(X[i:i_end], Y[i:i_end], batch_size=BATCH_SIZE, nb_epoch=1, verbose=2)
    auto_encoder.save_weights('/output/checkpoint_epoch_{}.hdf5'.format(k))
