import numpy as np
import os
import cv2
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# definir constantes
TRAIN_DIR = '/home/kberton/PycharmProjects/fabiokavlac/images/EU.jpg'
TEST_DIR = '/home/kberton/PycharmProjects/fabiokavlac/images/tests'
IMAGE_SIZE = 128
NUM_CLASSES = 2

# carregar imagens de treinamento
train_images = []
train_labels = []
for label in os.listdir(TRAIN_DIR):
    for image_file in os.listdir(os.path.join(TRAIN_DIR, label)):
        image = cv2.imread(os.path.join(TRAIN_DIR, label, image_file))
        image = cv2.resize(image, (IMAGE_SIZE, IMAGE_SIZE))
        train_images.append(image)
        train_labels.append(int(label))

# converter as listas em arrays numpy
train_images = np.array(train_images)
train_labels = to_categorical(train_labels, NUM_CLASSES)

# criar modelo de rede neural
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(NUM_CLASSES, activation='softmax'))

# compilar modelo de rede neural
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# treinar modelo de rede neural
model.fit(train_images, train_labels, epochs=10, batch_size=32)

# salvar modelo de rede neural treinado
model.save('my_model.h5')
