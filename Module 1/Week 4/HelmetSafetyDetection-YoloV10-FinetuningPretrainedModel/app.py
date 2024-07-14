import numpy as np
from PIL import Image
import streamlit as st
from ultralytics import YOLOv10

if __name__ == '__main__':
    st.title('Helmet Safety Detection Using YOLO V10')

    uploaded_file = st.file_uploader('Choose an image:', type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image = np.array(image)

        TRAINED_MODEL_PATH = 'best.pt'
        model = YOLOv10(TRAINED_MODEL_PATH)
        IMG_SIZE = 640
        IMAGE_URL = 'https://i.pinimg.com/originals/76/69/50/7669509c488cfd1ffea99a1406419fe1.jpg'

        CONF_THRESHOLD = 0.3
        results = model.predict(source=image,
                                imgsz=IMG_SIZE,
                                conf=CONF_THRESHOLD)

        annotated_img = results[0].plot()

        st.image(annotated_img, use_column_width=True)
