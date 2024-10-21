Readme by Hari Thapliyal

# Regression Model 
- This is test regression model with random number
- It was created in colab.
- Saved model as full_model.keras, model.tflite, tensorflow.js model
- it is for training purpose.
- model saved here can be used from andorid app.

## full_model.keras
```
# Save the full model (architecture + weights)
model.save('full_model.keras')

model.save('full_model.h5')

```

## tensorflow-lite model 
```
import tensorflow as tf

# Convert the model to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the converted model
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)

```

## Tensorflow.js 
```
import tensorflowjs as tfjs
from tensorflow.keras.models import load_model

# Load your full model
model = load_model('full_model.keras')

# Convert and save the model to TensorFlow.js format
tfjs.converters.save_keras_model(model, 'tfjs_model/')
```


## Predict with Model
```
# prompt: for this model, can you give example of predict?

import numpy as np
# Predict on the test data
y_pred = model.predict(X_test)

# Example: Predict for a specific sample
sample_index = 10
sample_input = X_test[sample_index]
predicted_output = model.predict(np.array([sample_input]))

print("Input Sample:", sample_input)
print("Actual Output:", y_test[sample_index])
print("Predicted Output:", predicted_output[0][0])

```
