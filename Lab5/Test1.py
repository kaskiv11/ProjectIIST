import numpy as np
from matplotlib import image
from tensorflow import keras
import matplotlib.pyplot as plt
from keras.layers import Dense, Flatten
from skimage import transform, color

def predict(number):
    number_i = x_test[number]
    matr = np.expand_dims(number_i, axis=0)
    predicted = model.predict(matr)
    print(f"Predicted number is: {np.argmax(predicted)}")
    plt.imshow(x_test[number], cmap=plt.cm.binary)
    plt.show()

def predict2():
    # Load and preprocess the custom image
    data = image.imread("Custom.png")
    data = color.rgb2gray(data)  # Convert to grayscale
    data = transform.resize(data, (28, 28))  # Resize to (28, 28)
    data = np.expand_dims(data, axis=-1)  # Add channel dimension
    data = np.expand_dims(data, axis=0)  # Add batch dimension

    # Make predictions
    predicted2 = model.predict(data)
    print(f"Predicted number is: {np.argmax(predicted2)}")
    plt.imshow(data[0, :, :, 0], cmap=plt.cm.binary)  # Display the grayscale image
    plt.show()

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

input("\nPress Enter to continue...\n")

x_train = x_train / 255
x_test = x_test / 255

y_train_cat = keras.utils.to_categorical(y_train, num_classes)
y_test_cat = keras.utils.to_categorical(y_test, num_classes)

model = keras.Sequential(
    [
        Flatten(input_shape=input_shape),
        Dense(128, activation='relu'),
        Dense(10, activation="softmax")
    ]
)

model.summary()

input("\nPress Enter to continue...\n")

batch_size = 32
epochs = 10

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(x_train, y_train_cat, batch_size=batch_size, epochs=epochs, validation_split=0.2)

score = model.evaluate(x_test, y_test_cat, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

input("\nPress Enter to continue...")

data = image.imread("Custom.png")
predict2()

data = image.imread("test2.png")
predict2()

input("\nPress Enter to continue...")

while True:
    x = input("\nEnter your number: ")
    if x == "stop":
        print("End of prediction")
        break
    else:
        predict(int(x))
