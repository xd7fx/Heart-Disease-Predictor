import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2

# Define a class for video frame processing
class VideoProcessor(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        # You can add image processing here (e.g., grayscale)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img

# Streamlit app layout
st.title("Webcam Streamlit App")

st.markdown("This app captures video from your webcam.")

# Webcam Stream
webrtc_streamer(key="example", video_transformer_factory=VideoProcessor)
