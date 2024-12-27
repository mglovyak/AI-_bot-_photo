from keras.models import load_model
import numpy as np
from PIL import Image
def get_class(model_path, labels_path, image_path):
    # Загрузка модели
    model = load_model(model_path)

    # Загрузка и подготовка изображения
    image = Image.open(image_path)
    image = image.resize((224, 224))  # Измените размер в соответствии с вашей моделью
    image_array = np.array(image) / 255.0  # Нормализация
    image_array = np.expand_dims(image_array, axis=0)  # Добавление размерности

    # Предсказание
    predictions = model.predict(image_array)
    return np.argmax(predictions)