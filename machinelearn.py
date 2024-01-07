import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers
import keras

dat = 521
dat2 = 79
book = pd.read_excel(r"book3.xlsx")
x_train = np.zeros([dat,1,5])
y_train = np.zeros([dat,1])
bookt = book.transpose()

x_test = np.zeros([dat2,1,5])
y_test = np.zeros([dat2,1])

for i in range(dat):
    x_train[i]=[book.values[i][1:7]]
    y_train[i]=bookt.values[0][i]
    
for p in range(dat2):
    print(dat+p)
    x_test[p]=[book.values[p+dat][1:7]]
    y_test[p]=bookt.values[0][p+dat]

y_train = tf.keras.utils.to_categorical(y_train,10)
y_test = tf.keras.utils.to_categorical(y_test,10)

model_lr = tf.keras.models.Sequential([layers.Flatten(), layers.Dense(64,activation='relu',input_shape=x_train.shape[1:])])
model_lr.add(layers.Dense(64, activation='relu'))
model_lr.add(layers.Dense(64, activation='relu'))
model_lr.add(layers.Dense(10, activation='softmax'))
model_lr.compile(optimizer='adam', loss='categorical_crossentropy', metrics='accuracy')

model_lr.fit(x_train, y_train, batch_size = 32, epochs=150, shuffle=True)

model_lr.summary()

#model.evaluate(x_test, y_test)

#model.predict(thing)

#model_lr.evaluate(x_test,y_test)


