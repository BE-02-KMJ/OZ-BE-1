# ts에서 model 불러오기
import tensorflow as tf


def load_model():
    model = tf.keras.applications.MobileNetV2(weights="imagenet")
    print("Model Load Successfully")
    return model


model = load_model()
