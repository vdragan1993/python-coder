from keras.models import Sequential
from keras.layers import Activation, TimeDistributed, Dense, RepeatVector, Embedding
from keras.layers.recurrent import LSTM


def get_model(X_vocab_len, X_max_len, y_vocab_len, y_max_len, hidden_size, num_layers):
    model = Sequential()

    # encoder
    model.add(Embedding(X_vocab_len, 64, input_length=X_max_len, mask_zero=True))
    model.add(LSTM(hidden_size))
    model.add(LSTM(hidden_size))
    model.add(RepeatVector(y_max_len))

    # decoder
    for _ in range(num_layers):
        model.add(LSTM(hidden_size, return_sequences=True))
    model.add(TimeDistributed(Dense(y_vocab_len)))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    return model
