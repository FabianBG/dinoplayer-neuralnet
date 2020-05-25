import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models


def gen_model():
    model = models.Sequential()
    model.add(layers.Conv2D(
        32, (3, 3), activation='relu', input_shape=(40, 120, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(2, activation='softmax'))

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model


def train_model(model, data, epochs=20):
    print("samples ", len(data))
    x = []
    y = []
    for d in data:
        tmp = [d["stack"][0]/255, d["stack"][1]/255, d["stack"][2]/255]
        x.append(np.stack(tmp, axis=2))
        y.append(np.array(d["value"]))
    x = np.array(x)
    y = np.array(y)

    model.fit(x, y, epochs=epochs)
    tf.keras.models.save_model(model, 'model.tf')
