from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2

class VideoProcessor(VideoTransformerBase):
    def __init__(self):
        self.device_index = 0  # استخدم الكاميرا الأولى

    def set_device_index(self, index):
        self.device_index = index

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return img

# اختيار الكاميرا
import streamlit as st

st.title("Webcam Streamlit App")
st.markdown("Select a camera device index:")

# واجهة لاختيار رقم الكاميرا
device_index = st.number_input("Camera Device Index", min_value=0, max_value=10, value=0, step=1)
processor = VideoProcessor()
processor.set_device_index(device_index)

# تشغيل الكاميرا
webrtc_streamer(key="example", video_transformer_factory=lambda: processor)
