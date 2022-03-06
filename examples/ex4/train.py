import os
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Convolution2D, MaxPooling2D, Activation, Dropout, Flatten, Dense

model = Sequential()
model.add(Convolution2D(32, (3, 3), input_shape = (150, 150, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Convolution2D(32, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Convolution2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(loss = "binary_crossentropy", optimizer = "rmsprop", metrics = ["accuracy"])

trainDataGen = ImageDataGenerator(
    rescale = 1. / 255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True
)

testDataGen = ImageDataGenerator(
    rescale = 1. / 255
)

trainGenerator = trainDataGen.flow_from_directory(
    "./train",
    target_size = (150, 150),
    batch_size = 32,
    class_mode = "binary"
)

validationGenerator = testDataGen.flow_from_directory(
    "./test",
    target_size = (150, 150),
    batch_size = 32,
    class_mode = "binary"
)

train = os.listdir("./train/safe") + os.listdir("./train/notsafe")
validation = os.listdir("./test/safe") + os.listdir("./test/notsafe")

trainNew = [x for x in train if not ".gif" in x]
validationNew = [x for x in validation if not ".gif" in x]

model.fit(
    trainGenerator,
    steps_per_epoch = len(trainNew) // 32,
    epochs = 50,
    validation_data = validationGenerator,
    validation_steps = len(validationNew) // 32
)

model.save("model.h5")
