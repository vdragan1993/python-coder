from prep import training_data
from prep import dictionary

input_words, output_words = training_data('./test-data')

words = []
for sentence in input_words:
  words += sentence
for sentence in output_words:
  words += sentence

unique_words = list(set(words))
print unique_words
print len(unique_words)

words_dict = dictionary(unique_words)

dataX = [[word for word in snt] for snt in input_words]
dataY = [[word for word in snt] for snt in output_words]
