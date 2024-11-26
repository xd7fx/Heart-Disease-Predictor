from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

class VideoProcessor(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return img

import streamlit as st

st.title("Webcam Streamlit App")
st.markdown("Select the correct camera.")

# اختر رقم الكاميرا بناءً على المخرجات من الكود السابق
device_index = st.number_input("Camera Device Index", min_value=0, max_value=10, value=0, step=1)

webrtc_streamer(key="example", video_transformer_factory=VideoProcessor, video_device_index=device_index)
