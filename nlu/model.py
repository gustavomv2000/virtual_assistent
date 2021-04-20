import yaml
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.utils import to_categorical

#importing data from yml file
data = yaml.safe_load(open('nlu\\train.yml', 'r', encoding='utf-8').read())

#creating inputs and outputs arrays
inputs, outputs = [], []
fwrite_inputs = open('inputs.txt', 'w', encoding='utf-8')

for command in data['commands']:
    command = command['command']
    inputs.append(command['input'].lower())
    fwrite_inputs.write(command['input'].lower() + '\n')
    outputs.append('{}|{}'.format(command['entity'], command['action']))
fwrite_inputs.close()

#getting max size of info in a example
max_seq = max([len(bytes(x.encode('utf-8'))) for x in inputs])


#creating data set with zeros (number of examples, max size of the examples, size of a byte)
input_data = np.zeros((len(inputs), max_seq, 256), dtype='float32')

#populating the data set with the char converted to the byte correspondent
for i, inp in enumerate(inputs):
    for k, ch in enumerate(bytes(inp.encode('utf-8'))):
        input_data[i, k, int(ch)] = 1.0


#set of the outputs, removes duplicates
labels = set(outputs)

#creating a file to store the labels
fwrite = open('labels.txt', 'w', encoding='utf-8')

#creating index to label and label to index
label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label
    fwrite.write(label + '\n')
fwrite.close()

#creates the output array with the index of each label output
output_data = []

for output in outputs:
    output_data.append(label2idx[output])


#changing output_data from integers to matrix of postions
output_data = to_categorical(output_data, len(output_data))


#creating the model
model = Sequential()
model.add(LSTM(128))
model.add(Dense(len(output_data), activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

model.fit(input_data, output_data, epochs=256)

#saving model
model.save('model.h5')