import streamlit as st
import torchvision.transforms as T
from PIL import Image

from src.models.detector import (convert_image_to_bytes, detect_objects,
                                 draw_boxes, get_model)

# Streamlit app
st.set_page_config(layout="wide")  # Set the layout to wide

st.title("Object Detection System")

st.sidebar.title("Settings")
model_name = st.sidebar.selectbox("Choose a model", ["ResNet50", "MobileNetV3"])
confidence_threshold = st.sidebar.slider('Confidence Threshold', 0.0, 1.0, 0.5, 0.01)

uploaded_files = st.file_uploader("Choose image files...", type=["jpg", "jpeg", "png", "bmp"], accept_multiple_files=True)

if uploaded_files:
    model = get_model(model_name)
    
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file).convert("RGB")
        
        # Adjusted columns to occupy more space
        col1, col2 = st.columns(2)
        
        with col1:
            with st.expander("Uploaded Image", expanded=True):
                st.image(image, use_column_width=True)
        
        transform = T.Compose([T.ToTensor()])
        image_tensor = transform(image)

        predictions = detect_objects(model, image_tensor)

        boxes = predictions['boxes'].detach().cpu().numpy()
        labels = predictions['labels'].detach().cpu().numpy()
        scores = predictions['scores'].detach().cpu().numpy()

        # Drawing boxes and labels
        processed_image = draw_boxes(image, boxes, labels, scores, threshold=confidence_threshold)
        
        with col2:
            with st.expander("Processed Image", expanded=True):
                st.image(processed_image, use_column_width=True)
        
        # Download button
        result_image = Image.fromarray(processed_image)
        byte_im = convert_image_to_bytes(result_image)
        st.download_button(label="Download Processed Image", data=byte_im, file_name="processed_image.jpg", mime="image/jpeg")
else:
    st.write("Please upload image files.")