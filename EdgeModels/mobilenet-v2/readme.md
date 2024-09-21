This dataset can be download from 
https://www.kaggle.com/datasets/alxmamaev/flowers-recognition

Therefore not pushing into github.

Notebook: Google_MobileNetV2_90_Acc-Colab.ipynb
this notebook was run into colab. I used my local gpu machine to run this.
I created local server on wsl -> docker -> using tensorflow/tensorflow:latest-gpu-jupyter image
this created a server at http://127.0.0.1:8888/tree?token=cb531de7d0c315bb96de3c4d94fc5b78d027362417e8f13b
Used this server in google colab.

Notebook: google-mobilenet-v2.ipynb
This was run into kaggle directly.


## How to read image using matplotlib?

from matplotlib.pyplot import imread
image = imread(filename)
image.shape



# creating a dataset of images 
X = filenames
y = boolean_kinds

# creating train and test split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=18)

# show image 
plt.imshow(X[i])
plt.title(kinds[train_labels[i].argmax()])
plt.axis("off")


# How to load image from tensorhub 
```
import tensorflow as tf
import tensorflow_hub as hub

# Define the input shape based on your data
input_shape = [None, 224, 224, 3]

# Create an input layer
inputs = tf.keras.Input(shape=input_shape[1:])

# Load the TensorFlow Hub model
hub_layer = hub.KerasLayer("/kaggle/input/mobilenet-v2/tensorflow2/140-224-classification/2", trainable=False)

# Define a lambda function to use the Hub layer
def hub_layer_fn(inputs):
    return hub_layer(inputs)

# Apply the lambda function
x = tf.keras.layers.Lambda(hub_layer_fn)(inputs)

# Add a Dense output layer
outputs = tf.keras.layers.Dense(units=output_shape, activation="softmax")(x)

# Create the model
model = tf.keras.Model(inputs=inputs, outputs=outputs)

model.compile(
      loss=tf.keras.losses.CategoricalCrossentropy(),
      optimizer=tf.keras.optimizers.Adam(),
      metrics=["accuracy"]
  )
  
model.build(input_shape)

model.summary()

# Create early stopping callback
early_stopping = tf.keras.callbacks.EarlyStopping(monitor="accuracy",
                                                  patience=3)


def create_data_batches(X, y=None, batch_size=batch_size, test_data=False):
    if test_data:
        print("Creating test data batches...")
        data = tf.data.Dataset.from_tensor_slices((tf.constant(X))) # only filepaths (no labels)
        data_batch = data.map(process_image).batch(batch_size)
        return data_batch
    else:
        print("Creating data batches...")
        # Turn filepaths and labels into Tensors
        data = tf.data.Dataset.from_tensor_slices((tf.constant(X),
                                                   tf.constant(y)))
        # Shuffling pathnames and labels before mapping image processor function is faster than shuffling images
        data = data.shuffle(buffer_size=len(X))

        # Create (image, label) tuples (this also turns the iamge path into a preprocessed image)
        data = data.map(get_image_label)

        # Turn the training data into batches
        data_batch = data.batch(batch_size)
        return data_batch
		
		
		
train_data = create_data_batches(X_train, y_train)
												  
model.fit(x=train_data,epochs=150,callbacks=[early_stopping])
```
