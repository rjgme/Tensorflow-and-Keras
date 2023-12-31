#GET MNIST DATA SET AND READ DIGITS
#Load the MINST data set, and normalize the image features to the 0-1 range. You will also need to one-hot encode the labels for your data in order to use the categorical cross-entropy loss function.
import tensorflow as tf
import tensorflow.keras as keras
from keras.datasets import mnist
# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train_subset, x_val_subset, y_train_subset, y_val_subset = train_test_split(x_train, y_train, test_size=0.2, random_state=42)
x_train_subset = x_train_subset.astype('float32') / 255
x_val_subset = x_val_subset.astype('float32') / 255
x_test = x_test.astype('float32') / 255
x_train_subset = tf.expand_dims(x_train_subset, axis =3)
x_val_subset = tf.expand_dims(x_val_subset, axis =3)
x_test = tf.expand_dims(x_test, axis =3)

num_classes = 10
y_train_subset = keras.utils.to_categorical(y_train_subset, num_classes)
y_val_subset = keras.utils.to_categorical(y_val_subset, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

x_train.shape


#Create a Convolution Neural Network (CNN)
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras import Sequential
model = Sequential()
batch_size = 128
epochs = 50
num_classes = 10
model.add(Conv2D(16, kernel_size=(3, 3), padding='same', activation='relu', input_shape=( 28, 28, 1), strides =1))
model.add(MaxPooling2D(pool_size=(2, 2), strides=2))
model.add(Flatten())
model.add(Dense(32, activation='relu'))

#Compile the model with categorical cross-entropy loss function, Adam optimizer, and set the metric to accuracy.
odel.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

start_time = time.time()
history = model.fit(x_train_subset, y_train_subset, batch_size=batch_size, epochs=epochs, validation_data=(x_val_subset, y_val_subset))
end_time = time.time()

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
model.summary()
print('Test accuracy: {test_acc}')

#Plot the training loss and validation loss of your model (accuracy versus epochs).
#Plot the Training accuracy and Validation accuracy of your model (versus epoch). 
import matplotlib.pyplot as plt

history = model.fit(x_train_subset, y_train_subset, validation_data=(x_test, y_test), epochs=10)
train_loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(train_loss) + 1)
plt.plot(epochs, train_loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

train_acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
epochs = range(1, len(train_acc) + 1)
plt.plot(epochs, train_acc, 'bo', label='Training')
plt.plot(epochs, val_acc, 'b', label='Validation')
plt.title('Training and validation')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

import tensorflow as tf
from tensorflow.keras.utils import to_categorical
import keras
import time
def create_model(dropout_rate):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='sigmoid'),
        keras.layers.Dropout(dropout_rate),
        tf.keras.layers.Dense(32, activation='sigmoid'),
        keras.layers.Dropout(dropout_rate),
        tf.keras.layers.Dense(32, activation='relu'),
        keras.layers.Dropout(dropout_rate),
        tf.keras.layers.Dense(20, activation=tf.nn.leaky_relu),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model

#Training 3 different models using three different Dropout rates (between 0.1, 0.5, 0.9).
    history_array = []
    for dropout_rate in [0.1, 0.5, 0.9]:
        print(f"Training model with dropout rate {dropout_rate}...")
        model = create_model(dropout_rate)
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


