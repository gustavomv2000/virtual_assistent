from tensorflow.keras.models import load_model
import numpy as np

#loading the model
model = load_model('nlu\\model.h5')

#loading the output labels
labels = open('labels.txt', 'r', encoding='utf-8').read().split('\n')

#creating index to label and label to index
label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label


def classify(text):
    # Criar um array de entrada
    x = np.zeros((1, 500, 256), dtype='float32')

    # Preencher o array com dados do texto.
    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0

    # Fazer a previsão
    out = model.predict(x)
    idx = out.argmax()

    return idx2label[idx]
