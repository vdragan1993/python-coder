import argparse

from keras.utils import plot_model

from prep import prep_data

from model import get_model

ap = argparse.ArgumentParser()
ap.add_argument('--dataset', type=str, default='./data')
ap.add_argument('--x_length', type=int, default=15)
ap.add_argument('--y_length', type=int, default=20)
ap.add_argument('--hidden_size', type=int, default=128)
ap.add_argument('--num_layers', type=int, default=2)
ap.add_argument('--show_shapes', type=bool, default=False)

args = vars(ap.parse_args())

DATASET_PATH = args['dataset']
INPUT_LENGTH = args['x_length']
OUTPUT_LENGTH = args['y_length']
HIDDEN_SIZE = args['hidden_size']
NUM_LAYERS = args['num_layers']
SHOW_SHAPES = args['show_shapes']

_, _, input_vocab, output_vocab, _, _ = prep_data(DATASET_PATH, INPUT_LENGTH, OUTPUT_LENGTH)

auto_encoder = get_model(len(input_vocab),
                         INPUT_LENGTH,
                         len(output_vocab),
                         OUTPUT_LENGTH,
                         HIDDEN_SIZE,
                         NUM_LAYERS)

plot_model(auto_encoder, to_file='model.png', show_shapes=SHOW_SHAPES)
