# Working with the TenzorFlow library.
# Recognition of handwritten letters

# Task:
#   1. Connect the TenzorFlow library.
#   2. Perform image detection and recognition.
#   3. Connect the MNIST database


import os
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

print("Welcome to the NeuralNine (c) Handwritten Digits Recognition v0.1")

# Decide if to load an existing model or to train a new one
train_new_model = True

if train_new_model:
    # Loading the MNIST data set with samples and splitting it
    mnist = tf.keras.datasets.mnist
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Normalizing the data (making length = 1)
    X_train = tf.keras.utils.normalize(X_train, axis=1)
    X_test = tf.keras.utils.normalize(X_test, axis=1)

    # Create a neural network model
    # Add one flattened input layer for the pixels
    # Add two dense hidden layers
    # Add one dense output layer for the 10 digits
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))  # Added layer
    model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

    # Compiling and optimizing model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Training the model
    model.fit(X_train, y_train, epochs=30)

    # Evaluating the model
    val_loss, val_acc = model.evaluate(X_test, y_test)
    print(val_loss)
    print(val_acc)

    # Saving the model
    model.save('path/to/handwritten_digits.h5')  # or use '.keras' extension if preferred

else:
    # Load the model
    model = tf.keras.models.load_model('path/to/handwritten_digits.model')

# Create a drawing window
canvas = np.ones((300, 300), dtype="uint8") * 255
cv2.namedWindow("Digit Drawing")

# Flag to indicate drawing
drawing = False


# Mouse callback function
def draw(event, x, y, flags, param):
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(canvas, (x, y), 15, (0, 0, 0), -1)


# Set the callback function for mouse events
cv2.setMouseCallback("Digit Drawing", draw)

# Draw and predict 10 numbers
for _ in range(10):
    canvas[:] = 255  # Clear the canvas for a new digit

    while True:
        cv2.imshow("Digit Drawing", canvas)
        key = cv2.waitKey(1) & 0xFF

        # Press 'c' to clear the canvas
        if key == ord("c"):
            canvas[:] = 255

        # Press 'q' to exit the drawing and predict the number
        elif key == ord("q"):
            break

    # Preprocess the drawn image for prediction
    img = cv2.resize(canvas, (28, 28))
    img = np.invert(np.array([img]))
    img = tf.keras.utils.normalize(img, axis=1)

    # Predict the number
    prediction = model.predict(img)
    print("The drawn number is probably a {}".format(np.argmax(prediction)))

    # Display the drawn image
    plt.imshow(img[0], cmap=plt.cm.binary)
    plt.show()

cv2.destroyAllWindows()
