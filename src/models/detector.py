from io import BytesIO

import cv2
import numpy as np
import streamlit as st
import torch
from torchvision.models.detection import (fasterrcnn_mobilenet_v3_large_fpn,
                                          fasterrcnn_resnet50_fpn)


# Function to get the model
@st.cache(allow_output_mutation=True)
def get_model(model_name):
    if model_name == "ResNet50":
        model = fasterrcnn_resnet50_fpn(pretrained=True)
    elif model_name == "MobileNetV3":
        model = fasterrcnn_mobilenet_v3_large_fpn(pretrained=True)
    model.eval()
    return model

# Function to detect objects
def detect_objects(model, image):
    with torch.no_grad():
        predictions = model([image])
    return predictions[0]

# Function to draw boxes and labels
def draw_boxes(image, boxes, labels, scores, threshold=0.5):
    np_image = np.array(image)
    for i, box in enumerate(boxes):
        if scores[i] > threshold:
            x1, y1, x2, y2 = box
            np_image = cv2.rectangle(np_image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            label = f"{labels[i]}: {scores[i]:.2f}"
            np_image = cv2.putText(np_image, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    return np_image

# Function to convert image to bytes
def convert_image_to_bytes(image):
    buf = BytesIO()
    image.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    return byte_im