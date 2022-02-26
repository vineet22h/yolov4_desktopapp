import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from utils import draw_bbox, get_detection_data, preprocess_img

# gpus = tf.config.experimental.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(gpus[0], True)

model = load_model('tf_yolov4_model/1')
class_names = [line.strip() for line in open('coco_classes.txt').readlines()]
class_color =  {name: list(np.random.random(size=3)*255) for name in class_names}

def predict(raw_img):
    img = preprocess_img(raw_img)
    imgs = np.expand_dims(img, axis=0)
    pred_output = model.predict(imgs)
    detections = get_detection_data(img=raw_img,
                                    model_outputs=pred_output,
                                    class_names=class_names)
    output_img = draw_bbox(raw_img, detections, cmap=class_color, random_color=True, figsize=(10, 10),
              show_text=True, show_img=False)
    return output_img

vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read()
    pred = predict(frame) 
    cv2.imshow('frame', pred)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()