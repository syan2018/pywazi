import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img

model = load_model("model.h5")

def getMessage(arg):
    image = load_img(arg, target_size = (150, 150))
    image = np.array(image)
    image = image.reshape(1, 150, 150, 3)
    image = image.astype("float32")
    image /= 255
    prediction = model.predict(image)
    return {
        "safe": float(prediction[0][0]),
        "notsafe": float(1 - prediction[0][0]),
        "message": "This is a safe image" if prediction[0][0] > 0.5 else "This is not a safe image"
    }
