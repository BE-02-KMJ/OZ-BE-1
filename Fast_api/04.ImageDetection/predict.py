# Tensorflow -> Image Model 불러오기
# Pillow -> Image 관련 Module

from PIL.Image import Image
import numpy as np
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from model_loader import model


# AI가 이해할 수 있는 데이터로 변경
def predict(image: Image):
    image = np.asarray(image.resize((224, 224)))[..., :3]  # RGB
    image = np.expand_dims(image, 0)  # 차원 확장
    image = image / 127.5 - 1.0  # Scaler(정규화) -> 이미지 데이터가 -1 ~ 1 형태 값으로 정규화
    results = decode_predictions(model.predict(image), 3)[0]
    print("results: ", results)
    result_list = []
    for i in results:
        result_list.append({"class": i[1], "confidence": f"{i[2]*100:0.2f} %"})
    return result_list
