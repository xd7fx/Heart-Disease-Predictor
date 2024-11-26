import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2

# Define Video Processor class
class VideoProcessor(VideoTransformerBase):
    def __init__(self):
        self.device_index = 0  # Default camera index

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return img

# Streamlit App UI
st.title("Webcam Streamlit App")
st.markdown("Select a camera device index:")

# Add a number input to let user specify the device index
device_index = st.number_input("Camera Device Index", min_value=0, max_value=10, value=0, step=1)

# Validate the selected camera index
cap = cv2.VideoCapture(device_index)
if not cap.isOpened():
    st.error(f"Camera with device index {device_index} is not available.")
else:
    cap.release()
    webrtc_streamer(key="example", video_transformer_factory=VideoProcessor)
